from REST_API.models import Book
from REST_API.serializers import BookSerializer
from rest_framework import generics

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
