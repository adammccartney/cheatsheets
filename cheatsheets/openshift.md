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



## ssh into container

```
oc rsh <pod>
```

# Networking // enabling routes for a project

An openshift project will typically include services and controllers. 
A service is typically some sort of webservice that we are going to be
deploying. Controllers are actually also services but typically they are
*special* in that they run on the control plane and are used to control the
resources that a particular service gets, i.e. They communicate with the
apiserver.

## Configuring network interfaces in Linux Containers

CNI (Cloud Network Interface) is a network plugin for kubernetes. It strives to
make it possible to enable networking in and on kubernetes. Specifically, it
leverages linux network namespaces to accomplish this goal.

### network namespaces

Aims: 
+ bring network capabilities to containers
 - virtual network device(s) in each container
 - bindings to port-number space established per namespace
 - rules for routing make is possible to direct packets to virtual device of
   specific container 


### Typical client server communcation model
```                 __________                                    __________ 
                    |        |                                    |        | 
                 /` |   Web  | <----- application protocol -----> |   Web  | application
           user {   | client |                                    | server | layer
           proc  \, |________|                                    |________|
                           ^                                       ^   ^
                         | :                                       :   |
                         V .                                       .
                    _______:___                                   _:_________
                 /` |      .  |                                   |.        |
                /   |   TCP:  | <-------- tcp protocol ----->     |:  TCP   | transport 
               /    |______.__|                                   |.________| layer
              [          | :                                       :  ^
     kernel   {     _____V_.___                                   _.__|______
     space    [     |      :  |                                   |:        |
               \    |   IP .  | <-------- tcp protocol ----->     |.  IP    | network
                \   |______:__|                                   |:________| layer
                 \,      | .                                       .  ^
                         V :                                       :  |
                    _______.___                                   _._________
                    |      :  |                                   |:        |
                    | Ethernet| <---- ethernet protocol ----->    |.Ethernet| datalink 
                    | Driver  |                                   |:Driver  | layer
                    |______.__|                                   |.________|
                         | :                                       :  ^
                         | .........................................  |
        _________________v____________________________________________|___________
                                     Ethernet

```

