import os
from REST_API.models import Book
from REST_API.serializers import BookSerializer
from rest_framework import generics
from django.core.files import File
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, pk=None):
        book = get_object_or_404(self.queryset, pk=pk)
        fd = open(book.path, 'rb')
        filename = "%s-%s.%s" % (book.author, book.title, book.extension)
        if book.extension == 'epub':
            response = HttpResponse(File(fd), content_type='application/epub+zip')
        else:
            response = HttpResponse(File(fd), content_type='application/pdf')
        response['Content-Length'] = os.path.getsize(book.path)
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
