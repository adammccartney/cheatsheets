# API tips & tricks

Bunch of tips and tricks for writing web APIS

# Basic Overview of web APIs

## HTTP Verbs

| crud HTTP verbs
|----- -----
| Crete <----------> POST |
| Read <----------> GET |
| Update <----------> PUT |
| Delete <----------> DELETE |

## Endpoints

Whereas a website consists of web pages with HTML, CSS and JavaScript, etc. a
web API will have endpoints instead. These endpoints are URLs with a list of
available actions (HTTP verbs) that expose data (typically JSON)

```
https://www.mysite.com/api/sounds         # GET returns all sounds
https://www.mysite.com/api/sound/<id>     # GET returns single sound
```

The first type of request is known as a **collection**.

Creating an API ultimately amounts to creating a series of endpoints: URLs with
associated HTTP verbs.

A webpage consists of HTML, CSS, sounds, etc. An endpoint is _just_ a way to
access data via the available HTTP verbs.

## HTTP

- request-response protocol
- occurs within a TCP connection between a client and server

### Basic HTTP message contents

**typical request**

```
GET / HTTP/1.1
Host: google.com
Accept_Language: en-us
```

**possible response**

```
HTTP/1.1 200 OK
Date: Mon, 03 Aug 2020 23:26:07 GMT
Server: gws
Accept-Ranges: bytes
Content-Length: 13
Content-Type: text/html; charset=UTF-8

Hello, world!
```

**abstraction of http message format**

```
Response/request line
Headers...

(optional) Body
```

Caveat: each resource requires one HTTP request/response cycle

## Status Codes

- 2xx Success - the action requested by the client was received, understood,
  and accepted
- 3xx Redirection - the requested URL has moved
- 4xx Client Error - there was an error, typically a bad URL request by the
  client
- 5xx Server Error - the server failed to resolve a request

**There are only four potential outcomes to any given HTTP request**

- it worked (2xx)
- it was redirected (3xx)
- client made an error (4xx)
- server made an error (5xx)

## Statelessness

- HTTP is a stateless protocol!
- each request/response pair is completely independent of the previous one.
- no stored memory of past interactions

This has certain benefits. HTTP is a really robust distributed protocol as a
result. Electronic communication systems are ultimately subject to signal loss
over time.

The downside is that this makes managing state really, really important in web
applications. Historically this was managed on the server, but more recently it
has moved into the browser with the advent of JavaScript frameworks like React,
Angular and Vue.

HTTP is really good at sending information between computers but terrible at
remembering anything outside of each individual request/response pair.

## REST

Representational State Transfer

- is stateless, like HTTP
- supports common HTTP verbs (GET, POST, PUT, DELETE, etc)
- returns data in either JSON or XML format

## Serializers

A serializer translates data into a format that is easy to consume over the
itnernet, typically JSON, and is displayed at an API endpoint.

## Cross-Origin Resource Sharing (CORS)

Basically, we need to specify the ports that will be open and then use
middleware to only allow traffic from these two sockets.
