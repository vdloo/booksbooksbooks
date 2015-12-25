from django.contrib import admin
from REST_API.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'path')

admin.site.register(Book, BookAdmin)
