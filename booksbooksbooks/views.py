from booksbooksbooks.models import Book
from booksbooksbooks.serializers import BookSerializer
from rest_framework import generics

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
