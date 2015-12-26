from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='admin/REST_API/book/', permanent=False), name='index'),
    url(r'^api/', include('REST_API.urls')),
]
