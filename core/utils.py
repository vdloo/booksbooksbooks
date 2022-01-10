from contextlib import suppress

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError


class AutomaticLoginMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path_info.startswith('/admin') and not request.user.is_authenticated:
            with suppress(IntegrityError):
                User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            user = authenticate(username='admin', password='admin')
            login(request, user)
        return self.get_response(request)
