


Model View Controller
======================


A useful table found on stackexchange that documents how the mvc pattern is
implemented in django.

| Idiomatic term | Django term | Meaning
|----------------|-------------|---------------------------------------------------------------------------------------------------|
| Model          | Model       | Contains all the business logic. At the very least the database access logic
| View           | Template    | Responsible for generating the HTML and other UI
| Controller     | View        | Contains the logic to tie the other parts together and to generate a response to a user request


Note that there is close interaction between the View and Controller
components. User interaction with an app, means that multiple components are
affected by changes stemming from the user interaction. As tends to be the
case, computer scientists opted to manage this additional complexity by
introducing a layer of abstraction. Below are two brief references to how these
types of interactions are managed in other systems/languages (c++ and
smalltalk). And then some links to further reading on how these interactions
are managed in django.

In c++ this would traditionally have been handled by introducing an observer class 
(see observer pattern) with a single update method. This is discussed by Buschmann 
et al (p. 129), where they point out that smalltalk does not need to use this 
additional pattern because in smalltalk, classes inherit from Object, which has the 
necessary bindings predefined. In django, this type of interaction is handled by 
[signals][]. Here is a [signal example][]. Signals appear to be very useful for
cases where it is necessary to manage some state that involves multiple
components. 

[signals]: https://docs.djangoproject.com/en/3.2/topics/signals/
[signal example]: http://www.koopman.me/2015/01/django-signals-example/
