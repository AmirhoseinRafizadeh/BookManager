from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreate.as_view(), name='book_create'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
]
