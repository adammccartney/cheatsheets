
Some tips for working with Django (3.1)
=======================================

Notes from the book(s) by William Vincent

## A standard setup checklist
+ create new directory for code locally
+ install Django in a new virtual environment
  ```
  pipenv install django~=3.1.0 psycopg2-binary==2.8.5
  pipenv shell
  ```
+ create a new project called config
  `django-admin startproject config .`
+ create a new app called newapp
  `python manage.py startapp pages`
+ update `config/settings.py`
+ setup 
  `python manage.py migrate`
+ test that it all works 
  `python manage.py runserver`

## APIs

The only major difference in setting up django for APIs is the additional step
of adding a serializers.py file to the app and we don't need a template file.
Otherwise the urls.py and views.py files act in the same manner.


### app structure
```
.
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── pages
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── Pipfile
└── Pipfile.lock
```
+ `admin.py` config file for the built-in Django Admin app
+ `apps.py` config for the app itself
+ `migrations/` keeps track of changes to models.py file so that the database and
  `models.py` file stay in sync 
+ `models.py` this is where we define our database models which Django
  automatically translates into database tables 
+ `tests.py` is for our app-specific tests
+ `views.py` is where we handle the request/response logic for out web app 

### Tell django project about newly installed app
Open `config/settings.py` and add pages to `INSTALLED_APPS` 


### Django request response cycle
`URL -> View -> Model (typically) -> Template`


# Pattern for creating new functionality

*new: view && url && template*

# Database creation

Django can generate databases. The db model is set up in the app.

1. First, we create a migrations file with the makemigrations command.
   Migration files create a reference of any changes to the databse models
   which means we can track changes-and debug errors as necessary over time.
   ```
   python manage.py makemigrations <appname>
   python manage.py migrate <appname>
   
   ```

2. We build the db with the migrate command which executes the instructions on
   in our migrations file.  


## Models best practices

+ add a `__str__` method to each of your models to improve readability

### Register your models as they get create!
```
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

# Admin 

In order to access our data we need to create an admin account.
`python manage.py createsuperuser`


# URLs

We need to set up two files in order to display dynamic content.

## <app>/urls.py
Here we import whatever type of view object we want to display and use path
from `django.urls` to create the pattern. 

## congfig/urls.py
Here we use `include` from `django.urls` to  

# Views
We then import our `Post` object from the `.models` module into the
`blog/views.py`

+ aside: [functional approach](https://tutorial.djangogirls.org/en/)

# Templates

Use a custom structure for adding templates. In the project's base directory
simply add `templates/`
Make sure to apply the following update:

```
# config/settings.py
TEMPLATES = [
{
...
'DIRS': [str(BASE_DIR.joinpath('templates'))], # new
...
},
]
```
### Standard base pattern for blog
```
<!-- templates/base.html -->
<html>
<head>
<title>Django blog</title>
</head>
<body>
<header>
<h1><a href="{% url 'home' %}">Django blog</a></h1>
</header>
<div>
{% block content %}
{% endblock content %}
</div>
</body>
</html>
```


# Static content 
Add `static/` to our base dir.
This can contain css and javascript

Update `config/settings.py` with
`STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]

Stylesheets can be added to correspond to our templates.
example:
`touch static/css/base.css`
add some style!

This style is then loaded into our template using Django's own markup language. 

### Rundown of steps leading to deployment
+ create top-level static folder and update STATICFILES_DIRS to point to it
+ add config for STATIC_ROOT and STATICFILES_STORAGE before running
  `collectstatic` for the first time (this compiles all static files into a
single staticfiles folder
+ install `whitenoise`, update INSTALLED_APPS, MIDDLEWARE and
  STATICFILES_STORAGE and then re-run collectstatic

## Django won't serve static files in production

Instead, the collectstatic command compiles all static files throughout the
project into a single directory suitable for deployment.
+ run collectstatic
+ set STATIC_ROOT
+ set STATICFILES_STORAGE

`collectstatic` must be run before each deployment. There are a number of ways
to serve these files. We're using the WhiteNoise package in this project.

# Deployment Checklist
+ install Gunicorn
  `pipenv install gunicorn==19.9.0`
+ add a Procfile file
  `touch Procfile && echo web: gunicorn config.wsgi --log-file - | tee ./Procfile`
+ update ALLOWED_HOSTS
+ add & commit lastest to git
+ `git push heroku master`
+ DEBUG set to FALSE
+ SECRET_KEY actually kept a secret
+ a production database, not SQLite

# Forms 

## Pattern 
+ update templates/<name>_detail.html page template
+ create <name>_<function> page template
+ update views.py by creating new class that represents our new view
+ udpate urls


# User accounts 

## Standard User authentication 
Django installs the auth app by default, this provides a user object with:
+ username
+ password
+ email
+ first_name
+ last_name

### Log In
+ Default view for log in page via LoginView


## Create a specific app for user accounts 
`python manage.py startapp accounts`

Like any newly added app, we have to add this to the installed apps list in
`config/settings.py`


Then we reapply the pattern that we have seen when creating functionality in
other apps.

+ Add url patterns to accounts/urls.py
+ Create views
+ Create page template


## Custom user model
+ update config/settings.py
+ create a new CustomUser model
+ create new forms for UserCreationForm and UserChangeForm
+ update accounts/admin.py
+ `makemigrations`
+ `migrate`

## User Authentication

+ Set up templates
+ Set urls

## Password Reset 

```
touch templates/registration/password_change_form.html
touch templates/registration/password_change_done.html
```
See examples for code!

Initially on our local example, we can use the Django console backend to "send
the email". In production we use SendGrid.

```
# config/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Custom templates
```
touch templates/registration/password_reset_form.html
touch templates/registration/password_reset_done.html
touch templates/registration/password_reset_confirm.html
touch templates/registration/password_reset_complete.html
```
See examples for code!


# Security 

## Forms
+ use `{% csrf_token %}` to protect form from cross-site request forgery 


# Testing

## Ideal times to write tests
+ before you right any code (TDD)
+ right after you've added new functionality and it's clear in your mind 
