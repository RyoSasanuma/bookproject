from django.urls import path
from books import views

urlpatterns = [
    path('', views.book_list, name='list'),
    path('<int:pk>/edit/', views.book_edit, name='edit'),
    path('<int:pk>/delete/', views.book_delete, name='delete'),
    path('fetch/', views.fetch_book, name='fetch'),
    path('add/', views.book_add, name='add'),
]

"""
表示するhtmlファイルは同じでも、URLは違うケースもあるのか？
"""
