from django.contrib import admin
from REST_API.models import Book
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'published')
    search_fields = ('author', 'title')
    class Media:
        js = ('js/utils.js',)

admin.site.register(Book, BookAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
