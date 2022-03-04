---
title: "Django REST framework"
date: 2021-10-14T11:40:24+02:00
draft: false

tags: ["Python", "django", "REST", "api"]
series: ["notes"]
---

Notes on a [tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)
on the django-rest-framework. 

There are a number of interesting examples in this tutorial that show how the
django-rest-framework leverages core django functionality.

* API work begins with the definition of a Serializer class. This is analogous
  to django's form mode of working with user input via the browser. While
  django core has Form and ModelForm classes that are defined as a way to
  interact with the database backend via a html form submitted through a
  web-browser, django-rest-framework defines Serializer and ModelSerializer classes
  that make available similar functionality to those wishing to access the same
  data via the API.

`Request` and `Response` Objects are offered by the django-rest-framework as
extensions of `HttpRequest` and `TemplateResponse` respectively. The tutorial
then steps through the definition of a `snippets/views.py` module. A View class, 
of one description or another, is typically used to populate a http
request/response. The tutorial example defines a number of refactoring steps
that show the different ways that views can be implemented. Django supports
everything from simple decorator, class, mixin and genric style definitions. With the
latter being the more economical in terms of lines of code.




