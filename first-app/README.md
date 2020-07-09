# Create your first app in a Django project

First, create your project as explained [here](../){target="\_blank"}. Then proceed according with the following tutorial.

## Create app

Inside your django project dir (same as manage.py) run

```
$ python manage.py startapp hello_app
```

your app will look like

```
hello_app/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## Write a view

Change dir 

```
$ cd django_workspace/django_project/hello_app
```

edit **_views.py_**

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")
```

create and edit **_urls.py_**

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

finally, edit **_django_workspace/django_project/django_project/urls.py_**

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hello_app/', include('hello_app.urls')),
    path('admin/', admin.site.urls),
]
```

Change dir

```
cd django_workspace/django_project
```

Run the server

```
$ python manage.py runserver
```

Check it out [http://localhost:8000/hello_app](http://localhost:8000/hello_app){target="_blank"}