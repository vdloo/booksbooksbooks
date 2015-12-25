Simple ebook indexer

Expect nothing fancy here, I'm just trying to get a feel for the Django REST framework.

Make sure you system has:
- python (2 that is)
- python-dev
- libxml2-dev
- libxslt1-dev
- pip


Installlation:
```
mkvirtualenv booksbooksbooks
pip install -r requirements/dev.txt
./manage.py migrate
```


Run the webserver:
```
./manage.py runserver 8001
```


For the API, point your browser to:
```
http://localhost:8001/api/book/
```


Admin panel with auto admin login at:
```
http://localhost:8001/admin/
```
