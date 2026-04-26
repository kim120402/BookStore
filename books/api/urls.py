from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='api_routes'),
    path('books/', views.getBooks, name='api_books'),
    path('books/<int:bookId>/', views.getBook, name='api_book'),
]