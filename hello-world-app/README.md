# Django Project Quick Start

## Install

1. Install Python
1. Install MySQL
1. Install Python lib for MySQL
1. Install Django

## Setup

1. Create Django Project
1. Create Django App
1. Create View
1. Create Model
1. Create Templates

## Create Django Project

```console
$ python3 -m pip install virtualenv
$ cd myproject
$ mkdir ENV
$ python3 -m virtualenv ENV
$ python3 -m pip install Django
$ python3 -m django --version
$ django-admin startproject mysite
$ cd mysite
$ django-admin startproject mysite
$ curl 127.0.0.1:8000
```

## Create Django App


## MySQL + Python + Django
Crie DB <nome> e usuário <user>

sudo apt install default-libmysqlclient-dev
python3 -m pip install mysqlclient

Diretório do projeto, settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': 'django_pwd',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py migrate

Depois crie um Model.

## Create Model

No diretório do seu <app>, models.py:

```python
from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=200)
    recorded_date = models.DateTimeField('date recorded')
```

Inclua seu <app> no settings.py do <proj>:

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

$ python manage.py makemigrations <app> # cria o schema
$ python manage.py sqlmigrate <app> 0001 # visualize as alterações
$ python manage.py migrate # aplica alterações no DB

## Using Model

```python
from polls.models import Choice

Question.objects.all()
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id

```
## Create a Template

mkdir <app>/templates/<app>
touch <app>/templates/<app>/index.html

Referencie no Django como <app>/index.html

Como escrever o index.html

```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Escreva a view como:

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

Ou como uma versão simplificada:

```python
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

## Styles and Images

Crie seu CSS dentro do diretório static:

touch  <app>/static/<app>/styles.css

Depois o utilize dentro de um template:

```index.html
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
```

Adicione imagens:

<app>/static/<app>/images/background.gif

Depois as utilize dentro de um CSS:

```css
body {
    background: white url("images/background.gif") no-repeat;
}
```

## Static Files

https://docs.djangoproject.com/en/3.0/howto/static-files/

https://docs.djangoproject.com/en/3.0/howto/static-files/deployment/

https://docs.djangoproject.com/en/3.0/howto/static-files/

### MySQL recover root password

$ sudo /etc/init.d/mysql stop
$ sudo mkdir /var/run/mysqld
$ sudo chown mysql:mysql /var/run/mysqld
$ sudo mysqld_safe --skip-grant-tables &
$ mysql -uroot

> use mysql;
> update user set authentication_string=PASSWORD("mynewpassword") where User='root';
> update user set plugin="mysql_native_password" where User='root';
> flush privileges;
> quit

### MySQL adicionar novo usuário

mysql -u root -p

> create database django_db;

CREATE USER 'novousuario'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'novousuario'@'localhost'; # ou...
GRANT ALL PRIVILEGES ON django_db . * TO 'novousuario'@'localhost';
FLUSH PRIVILEGES;

ALL PRIVILEGES- como vimos anteriormente, isso daria a um usuário do MySQL todo o acesso a uma determinada base de dados (ou se nenhuma base de dados for selecionada, todo o sistema)
CREATE- permite criar novas tabelas ou bases de dados
DROP- permite deletar tableas ou bases de dados
DELETE- permite deletar linhas das tabelas
INSERT- permite inserir linhas nas tabelas
SELECT- permite utilizar o comando Select para ler bases de dados
UPDATE- permite atualizar linhas das tabelas
GRANT OPTION- permite conceder ou revogar privilégios de outros usuários

GRANT [tipo de permissão] ON [nome da base de dados].[nome da tabela] TO ‘[nome do usuário]’@'localhost’;

REVOKE [tipo de permissão] ON [nome da base de dados].[nome da tabela] FROM ‘[nome do usuário]’@‘localhost’;

DROP USER ‘demo’@‘localhost’;

Lembre-se FLUSH PRIVILEGES;

## Django + React

https://www.youtube.com/watch?v=F9o4GSkSo40

## Django Deployment: Nginx + GUnicorn

https://www.youtube.com/watch?v=_MbZSSXdM8s

## Django + Supervisor

## Tutorial

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-pt

https://medium.com/@luciohenrique/realizando-o-deploy-com-python-django-virtualenv-gunicorn-systemd-nginx-https-221a1424763d

## Virtual Env

https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais

## Prompt

PS1='\u\W $ '
