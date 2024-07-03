from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    """
    list_display 属性は、管理サイトのモデルリストページで表示するフィールドを指定します。
    これにより、管理者が一覧表示で確認したいフィールドを選択できます。
    """
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    
    """
    list_filter 属性は、管理サイトのモデルリストページで使用できるフィルタを指定します。
    これにより、管理者は特定の条件でモデルのレコードをフィルタリングできます。
    """
    list_filter = ('is_staff', 'is_active',)

    """
    fieldsets 属性は、管理サイトのユーザー編集ページでフィールドをセクションごとにグループ化して表示するためのものです。
    これにより、フィールドを論理的にグループ化し、ユーザーインターフェースを整理することができます。
    """
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields':  ('is_staff', 'is_active', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    """
    add_fieldsets 属性は、新規ユーザー作成ページでのフィールド表示をカスタマイズするためのものです。
    これにより、新規ユーザー作成フォームで表示するフィールドとその配置を指定します。
    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    admin.site.register(User)