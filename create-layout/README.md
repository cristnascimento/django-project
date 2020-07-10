# Create a layout using django templates

In this tutorial we are going to show how to respond a request by rendering a html template and also how to create a layout so that we can extend it in other pages.

## Create a django project

```
$ cd django-workspace
$ django-admin startproject layout_project
```

## Create a django app

```
$ cd layout_project
$ python manage.py startapp hello
```
## Create routes

**_hello/urls.py_**

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

## Create views

**_hello/views.py_**

```python
from django.shortcuts import render

# ...
def detail(request, question_id):
	obj = {'name': 'john'}
    return render(request, 'hello/hello.html', data )

```


## Add new routes to the project

Edit **_project/urls.py_**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
]
```

## Create a base template

create a folder that will keep the templates
```
$ cd hello
$ mkdir -p templates/hello
```

**_hello/templates/hello/base.html_**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Django app</title>
  </head>
  <body>
    {% block content %}
    {% endblock %}
  </body>
</html>
```

## Extend the base template

create **_hello/templates/hello/hello.html_**

```html
{% extends 'hello/base.html' %}

{% block content %}
	<h1>Hello layout!</h1>
{% endblock %}
```

## Activate app in the project

**_django_project/settings.py_**

```
INSTALLED_APPS = [
    'hello.apps.HelloConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Include templates path in the project

**_django_project/settings.py_**

```
import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## Folder structure

```
django_workspace/
	ENV/
	layout_project/
		layout_project/
		hello/
		    __init__.py
		    admin.py
		    apps.py
		    migrations/
		        __init__.py
		    models.py
		    templates/
		    	hello/
		    		base.html
		    		hello.html
		    tests.py
		    views.py
		manage.py	 
```
## Try

Go to project folder

```
$ cd django_workspace/layout_project
```

run the server

```
$ python3 manage.py runserver
```

Check it out [http://localhost:8000/hello](http://localhost:8000/hello){target="\_blank"}

## Learn More

Congratulations! You have finished this tutorial.

Continue improving your skills by reading:

* [Django Getting Started](https://docs.djangoproject.com/en/3.0/intro){target="\_blank"}