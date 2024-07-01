from django.contrib import admin
from django.urls import path, include
from books.views import top


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top, name='top'),
    #path('books/', include('books.urls')),
    path('accounts/', include('accounts.urls')),
]