from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from REST_API import views

urlpatterns = [
    url(r'^book/$', views.BookList.as_view()),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
