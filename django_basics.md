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

Anytime you modify models.py you <em>must</em> run makemigrations and migrate!

```python manage.py makemigrations```

```python manage.py migrate```

I've put these into a shell script that can be run after every update to the models.py file.

admin.py
add relative import of the new app (Project in models.py)
```from .models import Project```

```admin.site.register(Project)```

Everything has now been saved to the database

---
Django-Python shell

```python manage.py shell```
Inside the shell:
```from projects.models import Project```
```Project.objects.all()```
>>> <QuerySet [<Project: Project object (1)>]>

The idea is we can create new objects of our models via the shell commands:

```Project.objects.create(title='',description='New object number 2',price='100',summary='ok, this was done in the shell prompt')```

New Model Fields 

Changing objects one can simply delete the sqlite db and migration directory items. THen change the objects and recreate the superuser. The new objects should be in updated in the app.

One can modify the objects without having to go through this above process. Check it out:

blank is for field is rendered -. False is required field
null has to do with the database -> True means database can be empty

---

Create custom home page

<a >View</a>

Start ne app for html pages
```python manage.py startapp pages```

Go to pages dir and find the views.py file

```from django.http import HttpResponse```
HttpResponse

Go to main project dir and open the urls.py file

import the new home page view function in the  views.py file above.
```from pages import views```

under urlpatterns list, add the following line

```path('',views.home_view,name="home")```

