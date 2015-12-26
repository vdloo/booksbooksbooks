Simple epub indexer

Expect nothing fancy here, just an exercise for me to get a feel for the Django REST framework. 

- no tests. no proper logging. no nice exception handling. spaghetti and duct tape all around.
- scans a given path for epub files and registers them in a database
- browse the database for books at ```http://localhost:8001/admin/REST_API/book/```
- retrieve on book object detail page returns the book as an attachment download ```http://localhost:8001/api/book/1/```
- download link button on book object pages ```http://localhost:8001/admin/REST_API/book/1/change/```

Make sure you system has:
- python (2 that is)
- python-dev
- libxml2-dev
- libxslt1-dev
- libz-dev
- build-essential
- pip


Installlation:
```
mkvirtualenv booksbooksbooks
pip install -r requirements/dev.txt
./manage.py migrate
```

Activate the virutalenv if you haven't already
```
workon booksbooksbooks
```

Run the webserver:
```
./manage.py runserver 8001
```

Index a directory that contains epubs
```
 python importer/main.py /your/path/that/contains/epubs
```

PROTIP: If you're in the US check out [Project Gutenberg's](https://www.gutenberg.org/) giant collection of free epubs in the public domain.


Django admin panel with auto admin login at:
```
http://localhost:8001/admin/
```

For the API, point your browser to:
```
http://localhost:8001/api/book/
```
