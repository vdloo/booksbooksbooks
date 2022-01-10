Simple ebook indexer
===================

Expect nothing fancy here, just an exercise for me to get a feel for the Django REST framework. 

- No tests. No proper logging. No nice exception handling. Spaghetti and duct tape all around.
- Scans a given path for epub and pdf files and registers them in a database.
- Browse the database for books at ```http://localhost:8001```
- Retrieve on the book object detail page returns the book as a download ```http://localhost:8001/api/book/1/```
- Download link button on book object pages ```http://localhost:8001/admin/REST_API/book/1/change/```


Installation
-------------

Make sure your system has:
- python3
- python3-dev
- libxml2-dev
- libxslt1-dev
- libz-dev
- build-essential
- pip3


Clone the repo, install the deps and set up the db:
```
git clone https://github.com/vdloo/booksbooksbooks; cd booksbooksbooks
python3 -m venv venv
. venv/bin/activate
pip install -r requirements/dev.txt
./manage.py migrate
```


Run the webserver
-----------------
Activate the virutalenv if you haven't already
```
workon booksbooksbooks
```

Start the webserver. ```0.0.0.0``` binds on all interfaces.
```
./manage.py runserver 0.0.0.0:8001
```

Index a directory that contains ebooks (epub or pdf)
-------------------------------------
protip: If you're in the US check out [Project Gutenberg's](https://www.gutenberg.org/) giant collection of free epubs in the public domain.

```
$ python importer/main.py ~/Downloads/ebooks/
{"id":1,"title":"The Idiot","author":"Dostoyevsky, Fyodor","path":"/home/vdloo/Downloads/ebooks/pg2638-images.epub"}
{"id":2,"title":"The Brothers Karamazov","author":"Dostoyevsky, Fyodor","path":"/home/vdloo/Downloads/ebooks/pg28054-images.epub"}
{"id":3,"title":"The Grand Inquisitor","author":"Dostoyevsky, Fyodor","path":"/home/vdloo/Downloads/ebooks/pg8578-images.epub"}
```

Browse the Database
-------------------

Django admin panel with auto admin login at:
```
http://localhost:8001
```

List of books
<p align="center">
  <img src="https://raw.githubusercontent.com/vdloo/booksbooksbooks/master/docs/screenshots/list.png" alt="List of books"/>
</p>

Download from object view
<p align="center">
  <img src="https://raw.githubusercontent.com/vdloo/booksbooksbooks/master/docs/screenshots/download.png" alt="Download from object view"/>
</p>


For the API, point your browser to:
```
http://localhost:8001/api/book/
```


Use MySQL instead of sqlite3
---------------------------
First make sure your system has ```libmysqlclient-dev```, 
then ```pip install MySQL-python``` in your virtualenv.

Create a local_settings.py in core/ that looks something like this:
```
from settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'name of your db',    # Create this yourself first
        'USER': 'name of your db user',
        'PASSWORD': 'password for that db user',
        'HOST': 'host or ip where your db is at',
        'PORT': '3306',    # MySQL default port
    }
}
```

Perform the migration: ```./manage.py migrate --setings=core.local_settings```

Run the server: ```./manage.py runserver 0.0.0.0:8001 --settings=core.local_settings```
