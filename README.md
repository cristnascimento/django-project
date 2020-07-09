# Django Quick Start

## Description

This project contains simple and small django applications that show some essential features of the Django Web Framework. In each folder you will going go find a README file explaining what features will be used on that project.

 Here we are going to present a quick tutorial on how to set up and run a django web application.

## Install Virtualenv

Create a dir so that we can install virtualenv and the django project.

```code
$ mkdir django-workspace
$ cd django-workspace
```

Install virtualenv
```
$ python3 -m pip install virtualenv
$ mkdir ENV
$ python3 -m virtualenv ENV
```
With virtualenv you can install your python packages locally without interfering with python global installation.

Activate virtualenv
```
$ source ENV/bin/activate
```

Now you can install your python packages.

## Install Django

Activate virtualenv
```
$ cd django-workspace
$ source ENV/bin/activate
```

Then install Django

```
$ python3 -m pip install Django
```

Check django version

```
$ python3 -m django --version
```

## Create Django project

```
$ django-admin startproject django_project
```

We are naming the project as **django_project** but you can name it whatever you want.

The structure of a django project looks like this

```
django_project/
    manage.py
    django_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## Run the server

Change dir 

```
$ cd django-workspace/django_project
```

Run
```
$ python3 manage.py runserver
```

Check the website [http://localhost:8000](http://localhost:8000){:target="\_blank"} or
```
$ curl 127.0.0.1:8000
```

## Deactivate virtualenv

When you finish working on your project you can deactivate virtualenv

```
$ deactivate
```
## Congratulation

You have finished your first set up of a django project.

Now you can learn more by checking the applications inside this project:

1. [first-app](./first-app)

Other soucers