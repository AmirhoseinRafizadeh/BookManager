from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer






class BookListCreate(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

