from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import capfirst
from .models import User

UserModel = get_user_model()

""" ログイン認証画面用カスタムフォーム """  # これは必要か？『実践本』の意図がわからない
class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

    error_messages = {'invalid_login': "Eメールアドレス または パスワードに誤りがあります。",
                      'inactive': "This account is inactive.",
                      }
    
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        # Set the label for the "email" field
        self.email_field = UserModel._meta.get_field("email")
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.email_field.verbose_name)
        
""" ユーザー登録用カスタムモデルフォーム """        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')