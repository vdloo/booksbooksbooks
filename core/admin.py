from django.contrib import admin
from REST_API.models import Book
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'year', 'extension')
    list_filter = ('extension',)
    search_fields = ('author', 'title')

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js',
            'js/utils.js'
        )
        css = {'all': ('css/hide_admin.css',)}


admin.site.register(Book, BookAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
