from rest_framework import serializers
from booksbooksbooks.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'path')
