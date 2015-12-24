from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from booksbooksbooks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^booksbooksbooks/$', views.BookList.as_view()),
    url(r'^booksbooksbooks/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
