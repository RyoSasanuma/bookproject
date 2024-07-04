from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _
from .models import User

UserModel = get_user_model()

""" Eメール用のログイン認証画面用カスタムフォーム """  # これは必要か？『実践本』の意図がわからない ←　絶対必要
class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput)

    error_messages = {'invalid_login': "Eメールアドレス または パスワードに誤りがあります。",
                      'inactive': _("This account is inactive."),
                      }
    
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None  # 認証されたユーザーオブジェクトを一時的に保持するためのもの
        super().__init__(*args, **kwargs)
        # Set the label for the "email" field
        self.email_field = UserModel._meta.get_field("email")
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.email_field.verbose_name)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(self.error_messages['invalid_login'], code='invalid_login', params={'email': self.email_field.verbose_name})
            else:
                self.confirm_login_allowed(self.user_cache)
        
        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(self.error_messages['inactive'], code='inactive')
        
    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):         # 必須メソッド 疑問：何が必須なのかわからない
        return self.user_cache
        
""" ユーザー登録用カスタムモデルフォーム """        
class CustomUserCreationForm(UserCreationForm):
    """
    新しいユーザーを作成するためのフォーム。
    すべての必須フィールドと、繰り返し入力するパスワードフィールドを含みます。
    """
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)
    first_name = forms.CharField(label=_("first name"))
    last_name = forms.CharField(label=_("last name"))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
""" ユーザー編集用カスタムモデルフォーム """     
class CustomUserChangeForm(UserChangeForm):
    """
    ユーザーを更新するためのフォーム。
    ユーザーのすべてのフィールドを含みますが
    パスワードフィールドを管理者用のパスワードハッシュ表示フィールドに置き換えます。
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def clean_password(self):
        return self.initial["password"]