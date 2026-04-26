from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),

    # CRUD
    path('book/<int:bookId>/', views.bookDetails, name='book_detail'),
    path('add_book/', views.addBook, name='add_book'),
    path('edit_book/<int:bookId>/', views.editBook, name='edit_book'),
    path('delete_book/<int:bookId>/', views.deleteBook, name='delete_book'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]