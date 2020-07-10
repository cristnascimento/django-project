# Contact list with Django and Bootstrap

## Description

In this project we are going to show some essential features of the [Django Framework](https://www.djangoproject.com/) applying them to a contact list application.

## Dependencies

* [Ubuntu 18.04](https://ubuntu.com/)
* [Python 3](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)

## Install virtualenv

```
$ python3 -m pip install virtualenv
```

## Set up virtualenv

```
$ cd django-workspace
$ mkdir ENV
$ python3 -m virtualenv ENV
$ source ENV/bin/activate
```

To deactivate 

```
$ deactivate
```

## Install Django

with your virtualenv activated

```
(ENV) $ python3 -m pip install django
```

Check the version

```
(ENV) $ django-admin --version
3.0.8
```

## Create Django Project

in your **_django-workspace_** dir 

```
(ENV) $ django-admin startproject contact_list_project
```

Folder structure

```
django-workspace/
  contact_list_project/
    contact_list_project/
        asgi.py                                                            
        __init__.py                                                        
        settings.py                                                        
        urls.py                                                            
        wsgi.py 
    manage.py
  ENV/
```

## Create Django app

in **_django-workspace/contact_list_project_** dir

```
(ENV) $ django-admin startapp contact
```

new folder structure

```
django-workspace/
  contact_list_project/
    contact_list_project/
        asgi.py                                                            
        __init__.py                                                        
        settings.py                                                        
        urls.py                                                            
        wsgi.py 
    contact/
        admin.py                                                           
        apps.py                                                            
        __init__.py                                                        
        migrations                                                         
        models.py                                                          
        tests.py                
        views.py     
    manage.py
  ENV/
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

**_contact/views.py_**

```python
from django.http import HttpResponse

def index(request):
  return HttpResponse("It's working.")
```

## Add new routes to the project

Edit **_contact_list_project/urls.py_**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('contact/', include('contact.urls')),
  path('admin/', admin.site.urls),
]
```

## Try

Go to project folder

```
(ENV) $ cd django-workspace/contact_list_project
```

run the server

```
(ENV) $ python3 manage.py runserver
```

Check it out [http://localhost:8000/contact](http://localhost:8000/contact)

Excellent! Now lets move on and create a template.

## Rendering a template

1. Create templates dir
1. Create a base template
1. Extend the base template
1. Edit your views
1. Set up your project to use templates
1. Run

## Create templates dir

in your **_django-workspace/contact_list_project_**

```
(ENV) $ mkdir -p contact/templates/contact
```

## Create a base template

create **_your templates/contact/base.html_**

```xml
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

create **_contact/templates/contact/contact.html_**

```xml
{% extends 'contact/base.html' %}

{% block content %}
    <h1>Hello layout!</h1>
{% endblock %}
```

## Edit your views

edit **_contact/view.py_**

```python
from django.shortcuts import render

def index(request):
    data = {'name': 'john'}
    return render(request, 'contact/contact.html', data )
```

## Set up your project to use templates

edit **_contact_list_project/settings.py_**

```
INSTALLED_APPS = [
  'contact.apps.ContactConfig',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]
```

put this 

```python
import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
    {
    ...
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
    ...
```
in **_contact_list_project/settings.py_**

```python
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

your app folder will have the following structure

```
contact/
    admin.py                                                           
    apps.py                                                            
    __init__.py                                                        
    migrations                                                         
    models.py                                                          
    templates/
      contact/
        base.html
        contact.html
    tests.py                
    views.py     
```
## Run

try again

```
(ENV) $ python3 manage.py runserver
```

Check it out [http://localhost:8000/contact](http://localhost:8000/contact)

or try with curl

```html
(ENV) $ curl http://localhost:8000/contact/
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Django app</title>
  </head>
  <body>
    
    <h1>Hello layout!</h1>

  </body>
</html>
```

Congratulations! Now we are ready to edit the project and include our contact list code.