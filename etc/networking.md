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
*   Trying 193.171.88.72:80...
* Connected to repo.mdw.ac.at (193.171.88.72) port 80 (#0)
```


