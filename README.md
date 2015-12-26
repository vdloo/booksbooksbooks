Simple epub indexer
===================

Expect nothing fancy here, just an exercise for me to get a feel for the Django REST framework. 

- No tests. No proper logging. No nice exception handling. Spaghetti and duct tape all around.
- Scans a given path for epub files and registers them in a database.
- Browse the database for books at ```http://localhost:8001/admin/REST_API/book/```
- Retrieve on the book object detail page returns the book as a download ```http://localhost:8001/api/book/1/```
- Download link button on book object pages ```http://localhost:8001/admin/REST_API/book/1/change/```


Installation
-------------

Make sure your system has:
- python (2 that is)
- python-dev
- libxml2-dev
- libxslt1-dev
- libz-dev
- build-essential
- pip


Ensure that you have the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html) sourced into your environment.
On Ubuntu you can put something like this in your ```.bashrc```:
```
export WORKON_HOME=$HOME/.virtualenvs
VEW='/usr/share/virtualenvwrapper/virtualenvwrapper.sh'
[ -f "$VEW" ] && source "$VEW"
```


Clone the repo, install the deps and set up the db:
```
git clone https://github.com/vdloo/booksbooksbooks; cd booksbooksbooks
mkvirtualenv booksbooksbooks
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

Index a directory that contains epubs
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
http://localhost:8001/admin/REST_API/book/
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
