from django.contrib import admin
from REST_API.models import Book
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'year')
    search_fields = ('author', 'title')
    class Media:
        js = ('js/utils.js',)
        css = {'all': ('css/hide_admin.css',)}

admin.site.register(Book, BookAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
