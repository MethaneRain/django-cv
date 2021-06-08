```django-admin startproject ________```

```python manage.py runserver```
There will be warnings, just ignore those for now. There should be a local web address given to show the django project.

access http://127.0.0.1:8000/ in web browser to see if the Django project has been set up correctly.

** Every Django project has a secret key, unique to the project **

*** in settings.py make sure to turn DEBUG to False when going public!! ***

```python manage.py migrate```
This syncs the settings from the django project to the django apps. 

This will also update or create the database if it doesn't exist. In seetings.py, check out the DATABASES dictionary and change the name to understand more.


Check admin

Create superuser

```python manage.py createsuperuser```

Update admin
http://127.0.0.1:8000/admin/
---

Creating the first app

```python manage.py startapp _____```


Open models.py

