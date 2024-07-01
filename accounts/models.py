from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

""" カスタムユーザーマネージャー """
class UserManager(BaseUserManager):
    # Django管理画面のユーザーモデルデータ作成用メソッド？
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    # Django管理画面のスーパーユーザーモデルデータ作成用メソッド？
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
""" カスタムユーザーモデル """
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True) # 明示的にidフィールドを定義
    email = models.EmailField(unique=True)  # メールアドレス
    """ AbstractBaseUser.passward = password = models.CharField(_("password"), max_length=128)""" # パスワード
    first_name = models.CharField(max_length=30)        # 名
    last_name = models.CharField(max_length=30)         # 姓
    is_superuser = models.BooleanField(default=False)   # スーパーユーザー権限フラグ
    is_staff = models.BooleanField(default=False)       # 管理画面用権限フラグ
    is_active = models.BooleanField(default=True)       # アクティブ状態フラグ
    """ AbstractBaseUser.last_login = models.DateTimeField(_("last login"), blank=True, null=True) """ # 最終ログイン年月日
    date_joined = models.DateTimeField(auto_now_add=True) #　これは何のためのフィールドなのか？

    objects = UserManager() # Userマネージャーオブジェクトのコンポジション

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']   # 必須フィールドを指定

    def __str__(self):
        return self.email