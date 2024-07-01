from django.urls import path
from django.contrib.auth.views import LoginView
from .views import signup, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]