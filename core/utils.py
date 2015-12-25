from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class AutomaticLoginMiddleware(object):
    def process_request(self, request):
        if request.path_info.startswith('/admin') and not request.user.is_authenticated():
            try:
                User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            except:
                pass
            user = authenticate(username='admin', password='admin')
	    login(request, user)

