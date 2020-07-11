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

**_contact/urls.py_**

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
    urls.py
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

## Create mock data

create **_contact/mock_data.py_**

```python
import copy

class Contact:

  def __init__(self):
    self.id = 0
    self.firstName = ""
    self.lastName = ""
    self.email = ""
    self.phone = ""
    self.phoneCategory = "" 
    self.address = ""
    self.city = ""
    self.state = ""
    self.zip = ""
    self.closeFriend = ""

  def setFromForm(self, request):
    self.firstName = request.POST['firstName']
    self.lastName = request.POST['lastName']
    self.email = request.POST['email']
    self.phone = request.POST['phone']
    self.phoneCategory = request.POST['phoneCategory']
    self.address = request.POST['address']
    self.city = request.POST['city']
    self.state = request.POST['state']
    self.zip = request.POST['zip']
    self.closeFriend = request.POST['closeFriend']

...

mock_contacts = []

zapata = Contact()
zapata.id = 1
zapata.firstName = "Natasha"
zapata.lastName = "Zapata"
zapata.email = "zapata@blindspot.com"
zapata.phone = "+1 728 68768778"
zapata.phoneCategory = "Home"
zapata.address = "876 5th Av"
zapata.city = "New York"
zapata.state = "SP"
zapata.zip = "1323543"
zapata.closeFriend = "on"

mock_contacts.append(zapata)
...
```

## Create a service

create **_contact/services.py_**

```python
from .mock_data import Contact, mock_contacts, nextId
import copy 

class ContactService:

  def __init__(self):
    self.contacts = mock_contacts
    self.nextId = nextId

  def getContacts(self):
    return copy.deepcopy(self.contacts)

  def getContact(self, id):
    return next(contact for contact in self.contacts if contact.id == id).copy()

  def createContact(self, contact):
    contact.id = self.nextId
    self.nextId += 1
    self.contacts.append(contact)

  def updateContact(self, contact):
    index = next(i for i, contactOld in enumerate(self.contacts) if contactOld.id == contact.id)
    self.contacts[index] = contact

  def deleteContact(self, id):
    index = next(i for i, contact in enumerate(self.contacts) if contact.id == id)
    contact = self.contacts.pop(index)
```

## Create routes

edit **_contact/urls.py_**

```python
from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('add', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('view/<int:id>', views.view, name='view'),
    path('post', views.post, name='post'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('', views.index, name='index'),
]
```

## Create views

edit **_contact/views.py_**

```python
from django.shortcuts import render, redirect
from .services import ContactService
from .mock_data import Contact

service = ContactService()

def index(request):
    return render(request, 'contact/home.html')

def list(request):
    contacts = service.getContacts()
    data = {"contacts": contacts}
    return render(request, 'contact/list.html', data)

def add(request):
    data = { "mode": "add", "action": "/contact/post/", "readonly": "", "disabled": "", "contact": Contact()}
    return render(request, 'contact/contact.html', data)

def edit(request, id):
    contact = service.getContact(id)
    data = { "mode": "view",  "action": "/contact/post/"+str(id), "readonly": "", "disabled": "", "contact": contact}
    return render(request, 'contact/contact.html', data)

def view(request, id):
    contact = service.getContact(id)
    data = { "mode": "view",  "action": "/contact/post/"+str(id), "readonly": "readonly", "disabled": "disabled", "contact": contact}
    return render(request, 'contact/contact.html', data)

def post(request):
    contact = Contact()
    contact.setFromForm(request)
    service.createContact(contact)
    return redirect("/contact/list")

def update(request, id):
    contact = Contact()
    contact.setFromForm(request)
    contact.id = id
    service.updateContact(contact)
    return render("/contact/edit/"+id)

def delete(request, id):
    service.deleteContact(id)
    return rendirect("/contact/list")
```

## Create more templates

**_templates/home.html_**

```html
{% extends 'contact/base.html' %}

{% block content %}
    <h1>Home</h1>
{% endblock %}
```

**_templates/list.html_**

```html
{% extends 'contact/base.html' %}

{% block content %}
    <h1>List</h1>
{% endblock %}
```

Now you have

```
templates/contact/
  base.html
  contact.html
  home.html
  list.html
```  

## Try

Now try to access those pages

* [localhost:8000/contact](http://localhost:8000/contact)
* [localhost:8000/contact/add](http://localhost:8000/contact/add)
* [localhost:8000/contact/edit/1](http://localhost:8000/contact/edit/1)
* [localhost:8000/contact/view/1](http://localhost:8000/contact/view/1)
* [localhost:8000/contact/list](http://localhost:8000/contact/list)

Wow! This is wonderful !!! Now lets create our interface and connect it with our data.

## Copy HTML content to templates

You can find these files [here](./html/). Copy their content to its respective template

**_templates/base.html_**

```xml
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
        <title>Contact list</title>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <a class="navbar-brand" href="/contact">CristNascimento</a>
          ...

          {% block content %}
          {% endblock %}

          ...
    <body>
</html>

```

**_templates/home.html_**

```xml
{% extends 'contact/base.html' %}

{% block content %}
<div class="container col-md-6" >
  <br/>
  <h2>Welcome to home page!</h2>
  <br/>
</div>
{% endblock %}
```

**_templates/contact.html_**

```xml
{% extends 'contact/base.html' %}

{% block content %}
    <div class="container col-md-6" >
      <br/>
      <h1>Add/Edit/View Contact</h2>
      <br/>
      <form>
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="inputFirstName">First name</label>
            <input type="text" class="form-control" id="inputFirstName" name="firstName">
          </div>
          ...
      </form>
    </div>
{% endblock %}
```
**_templates/list.html_**

```xml
{% extends 'contact/base.html' %}

{% block content %}
<div class="container col-md-8" >
    <br/>
    <h3>List of contacts</h3><br/>
    <table class="table table-striped table-hover">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">E-mail</th>
          <th scope="col">Action</th>
        </tr>
        ...
    </table>
</div>
{% endblock %}
```

Finally, we need to bind the data to the form controls.

## Bind data to form controls

**_templates/contact.html_**

1. Set form action attribute
```xml
<form method="post" action="{{action}}">
```
1. Set csrf control
```python
{% csrf_token %}
```
1. Set value attribute for each control
```xml
<input type="text" class="form-control" id="inputFirstName" name="firstName" value="{{contact.firstName}}">
```
1. Set readonly and disabled attributes
```xml
<input ... name="firstName" value="{{contact.firstName}}" {{readonly}}>
...

```
1. Set checked option for select controls
```xml
<option {% if contact.phoneCategory == "Mobile" %} selected {% endif %}>Mobile</option>
...
<input ... {{% if contact.closeFriend == "on" %} checked {% endif %}>
...
```
1. Set submit and cancel buttons

```xml
{% if mode == "add" %}
  <button type="submit" class="btn btn-primary">Add</button>
  <a href="/contact/list" class="btn btn-warning">Cancel</a>
{% endif %}
```

**_templates/list.html_**

loop through contact list

```xml
{% for contact in contacts %}
    <tr>
      <th scope="row">1</th>
      <td>{{contact.firstName}}</td>
      <td>{{contact.lastName}}</td>
      <td>{{contact.email}}</td>
      <td>
        <a class="btn btn-success" href="/contact/view/{{contact.id}}" role="button">View</a>
        <a class="btn btn-warning" href="/contact/edit/{{contact.id}}" role="button">Edit</a>
        <a class="btn btn-danger" href="/contact/delete/{{contact.id}}" role="button">Remove</a>
      </td>
    </tr>
{% endfor %}
```
## Everything is working: try again

[localhost:8000/contact](http://localhost:8000/contact)

Try to use the form to create a new contact and then navigate on list to view, edit and remove contacts.

## Congratulations

You have completed this tutorial.

Here are some of the main concepts that you have covered:

* Create a django project
* Create a django app
* Create routes
* Create views
* Use mock data
* Create a service
* Render templates
* Handle form submission
* Binding data to form controls

Learn more

* [Django website](http://djangoproject.com)
* [Django Template Syntax](https://docs.djangoproject.com/en/3.0/topics/templates/#the-django-template-language)