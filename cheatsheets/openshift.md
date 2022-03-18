# Some notes on developing with openshift

## some oc commands

to view all apps currently deployed:

`oc get all -o name`

to determine what resources may have been added to resources:

oc describe route/blog-django-py

depending on what way the app was deployed, it will receive a name from
openshift.

`oc get all --selector app=blog-django-py -o name`

to delete this app:

`oc delete all --selector app=blog-django-py`

## Deploying a new app from oc command line

`oc new-app python:latest~https://github.com/openshift-katacoda/blog-django-py`

`oc logs bc/blog-django-py --follow`

Once the build is complete, you can view the status of a project deployed to
the project with:
`oc status`

The application needs to be exposed manually (unlike the web console)
`oc expose service/blog-django-py`

To get the url, run:
`oc get route/blog-django-py`

## configure http route

https://docs.openshift.com/container-platform/4.9/networking/routes/route-configuration.html#nw-path-based-routes_route-configuration
