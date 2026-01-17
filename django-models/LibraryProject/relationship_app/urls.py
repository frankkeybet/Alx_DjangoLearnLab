from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view
from .views import add_book, edit_book, delete_book

from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path( 'login/',LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('register/', views.register, name='register'),
    
     path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

   path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
