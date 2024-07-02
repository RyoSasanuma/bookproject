from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignUpView, logout_view
from .forms import EmailAuthenticationForm

urlpatterns = [
    # path('signup/', signup, name='signup'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(form_class=EmailAuthenticationForm,    # カスタムフォームクラスの指定
                                     redirect_authenticated_user=True,      # この属性は、既に認証されたユーザーがログインページにアクセスしたときの挙動を制御するためのものです。False に設定するとログインページが表示され、True に設定するとリダイレクトが行われます。
                                     template_name='accounts/login.html'
                                     ),name='login'),
    path('logout/', logout_view, name='logout'),
]