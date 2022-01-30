Don't forget your sockets
=========================

```
fd = socket(domain, type, protocol)
```

See the man page for a list of all the different available types of socket,
these are listed in the typical constant/enum style.

# Types 

Every socket provides at least two types -> stream and datagram
                               
| property                     | stream   | datagram   |
| ------------                 | -------- | ---------- |
| Reliable delivery?           | y        | n          |
| Message boundaries prserved? | n        | y          |
| Connection oriented?         | y        | n          |

### jargon
+ peer socket: refers to the socket at the other end of the connection
+ peer address: denotes the application utilizing the peer socket

### Protocols
In the internet domain, datagram sockets employ the User Datagram Protcol
(UDP), and stream sockets (usually) employ the Transmission Control Protocol
(TCP). The terms UDP socket and TCP socket refer to the terms Internet domain
datagram socket and internet domain stream socket respectively.


### API / syscalls

| call        | functionality                                          |
|-------------|--------------------------------------------------------|
| `socket()`  | create new                                             |
| `bind()`    | bind socket to addr                                    |
| `listen()`  | allows a stream socket to accept incoming connections  |  
| `accept()`  | accepts a connection from a peer on a listening stream |
| `connect()` | establish a connection with another socket             |


## Stream Sockets

### Active and passive
+ Typically client is active because is calls `socket()` to open the connection, 
  this is referred to as performing and active open.
+ Contrastingly, a server will simply perform `listen()`, which is referred to
  as a passive open.

