# networking stuff (because docker is confusing)

## Statement of problem

Running a piece of software called Virtuoso on a virtual machine. Virtuoso is a
pretty fancy semantic web thingy that claims to be a universal server. It looks
really great. We're running it from a docker container with some volumes to
handle whatever is getting written to the db on the server side. Problem is
that we want to serve it on a domain with a bunch of other stuff, so we need to
create another service that maps incoming http requests from their incoming
domain/directory structure to the version running on our localhost. The
incoming requests are being dealt with by haproxy.

What is the structure of an incoming request? If we query the domain with curl,
we see that the URI resolves to a websocket. 

```
>$curl -v repo.mdw.ac.at
=======
# Some (more) notes on networking 

## Statement of problem: 

Trying to run a copy of virtuoso server from within a container on a virtual
machine.

1. Web facing frontend using haproxy to serve contanet from the dynamic backend
2. an apache2 using mod substitude to rewrite the requests
3. a virtuoso server that is serving the application endpoints

```
>$curl -v repo.mdw.ac.at/virtuoso
*   Trying 193.171.88.72:80...
* Connected to repo.mdw.ac.at (193.171.88.72) port 80 (#0)
```


=======
## Haproxy config 

Haproxy is handling the actualy routing of webtraffic. In the config we are
specifying that it listen for incoming http requests on port 80. It should use
a frontend called virtuoso in that binds to and unspecified ipv6 address and
port 9080. It also uses virtuoso as a backend which is a server running on
127.0.0.1:8890. 

## Logging on haproxy

Running a status check on the haproxy service with systemd shows how the
haproxy service behaves when it is set up. It clearly shows that the service
sees the backend and the backend is up and running: 

```
● haproxy.service - HAProxy Load Balancer
     Loaded: loaded (/usr/lib/systemd/system/haproxy.service; enabled; vendor preset: disabled)
     Active: active (running) since Mon 2021-11-15 14:36:16 CET; 19h ago
    Process: 23850 ExecStartPre=/usr/sbin/haproxy -Ws -f $CONFIG -c -q $EXTRAOPTS (code=exited, status=0/SUCCESS)
   Main PID: 23861 (haproxy)
      Tasks: 25
     CGroup: /system.slice/haproxy.service
             ├─23861 /usr/sbin/haproxy -Ws -f /etc/haproxy/haproxy.cfg -p /run/haproxy.pid -S /run/haproxy-master.sock
             └─23863 /usr/sbin/haproxy -Ws -f /etc/haproxy/haproxy.cfg -p /run/haproxy.pid -S /run/haproxy-master.sock

Nov 15 22:48:56 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Health check for server virtuoso_back/virt_01 succeeded, reason: Layer4 check passed, check duration: 0ms, status: 3/3 UP.
Nov 15 22:48:56 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Server virtuoso_back/virt_01 is UP. 1 active and 0 backup servers online. 0 sessions requeued, 0 total in queue.
Nov 16 09:26:50 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Health check for server virtuoso_back/virt_01 failed, reason: Layer4 connection problem, info: "Connection refused", check duration: 0ms, status: 2/3 UP.
Nov 16 09:26:52 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Health check for server virtuoso_back/virt_01 failed, reason: Layer4 connection problem, info: "Connection refused", check duration: 0ms, status: 1/3 UP.
Nov 16 09:26:54 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Health check for server virtuoso_back/virt_01 failed, reason: Layer4 connection problem, info: "Connection refused", check duration: 0ms, status: 0/2 DOWN.
Nov 16 09:26:54 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Server virtuoso_back/virt_01 is DOWN. 0 active and 0 backup servers left. 0 sessions active, 0 requeued, 0 remaining in queue.
Nov 16 09:26:54 repo-conv1 haproxy[23863]: [ALERT]    (23863) : backend 'virtuoso_back' has no server available!
Nov 16 09:27:22 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Health check for server virtuoso_back/virt_01 succeeded, reason: Layer4 check passed, check duration: 0ms, status: 1/2 DOWN.
Nov 16 09:27:24 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Health check for server virtuoso_back/virt_01 succeeded, reason: Layer4 check passed, check duration: 0ms, status: 3/3 UP.
Nov 16 09:27:24 repo-conv1 haproxy[23863]: [WARNING]  (23863) : Server virtuoso_back/virt_01 is UP. 1 active and 0 backup servers online. 0 sessions requeued, 0 total in queue.
```

It doesn't give us any information on incoming requests beyond this. 


## Virtuoso service 

Virtuoso is being started as a service with systectl. The service is launching
a docker network that contains two containers: one containing the virutoso
application and another containing an apache2 reverse proxy server that
*should* handle rewrites for incoming requests. It's worth mentioning that the
virtuoso service is running in its own container. 


## apache2

Apache2 is running inside a container. In order to patch in our user defined
config, we are copying in a custom config file during the docker build process. 
Currently there is an issue around finding the modules shared library files
within the container. 
