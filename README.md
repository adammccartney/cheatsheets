Cheatsheets on a variety of topics
==================================

Just a single directory with a flat file hierarchy. Will eventually index and
make searchable. For the time being it's possible to use `grep` or some other
searcher: 

```
<p@q>$grep -Rn python cheatsheets/
cheatsheets/designPatternsPy.md:6:Overview of factory method implementation in python:
cheatsheets/designPatternsPy.md:7:<https://realpython.com/factory-method-python/>
cheatsheets/users+groups.md:28:universally used inteface and is offered by such implementations as python's
cheatsheets/webpackjs.md:53:other languages (like c or python). There seems slightly more emphasis on the
cheatsheets/webpackjs.md:71:I've built some fairly substantial projects in python, java, c and c++ but
cheatsheets/toDo.md:47:instances of a class. (see lutz, learning python p1031)
cheatsheets/questions.md:1:## General (python) programming questions ##
cheatsheets/questions.md:5:  Answer: Because of the nature of python namesspaces (one per module) each
cheatsheets/docker.md:51:    command: python manage.py runserver 0.0.0.0:8000
cheatsheets/emacsTips.md:9: + Run python file in venv Notebook: C-c C-c
cheatsheets/openshift.md:27:`oc new-app python:latest~https://github.com/openshift-katacoda/blog-django-py`
cheatsheets/djangoTips.md:17:  `python manage.py startapp pages`
cheatsheets/djangoTips.md:20:  `python manage.py migrate`
cheatsheets/djangoTips.md:22:  `python manage.py runserver`
cheatsheets/djangoTips.md:83:   python manage.py makemigrations <appname>
cheatsheets/djangoTips.md:84:   python manage.py migrate <appname>
cheatsheets/djangoTips.md:108:`python manage.py createsuperuser`
cheatsheets/djangoTips.md:233:`python manage.py startapp accounts`
cheatsheets/pythonTips.md:1:pythonTips.md
cheatsheets/pythonTips.md:4:+ Always feed python live mice
cheatsheets/pythonTips.md:346:The first time python imports through a directory, it automatically runs all
cheatsheets/pythonTips.md:353:python package.
cheatsheets/pythonTips.md:362:* <https://www.python.org/dev/peps/pep-0008/>
cheatsheets/pythonTips.md:368:A few tips from *effective python*
cheatsheets/pythonTips.md:417:`python3 -m venv %name`
cheatsheets/pythonTips.md:424:+ `python -m pip install -r requirements.txt
```
