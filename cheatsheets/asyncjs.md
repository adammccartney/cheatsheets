# asynchronous javascript

## Notes to future self (executed asynchronously)

Keep in mind that anything that we are doing in an asynchronous manner means
that we want the jobs to execute in a non-blocking manner. This doesn't
necessarily mean at the same time -> but really it pretty much does.

+ Synchronously = jobs executes sequentially like a pipeline, in order, 
  one after the other
+ Asynchronously = jobs execute in some manner that does not obey the same
  rules of sequential ordering. 

## Talk about complicated...

So here are some notes on various strategies pertaining to the use of
asynchronous javascript.

There is a well thought out chapter in [eloquent javascript](https://eloquentjavascript.net/code/#11.1)
on the topic that goes into some detail. Asynchronous code is hairy no matter what way you look
at it. The first example below `locateScalpel` is defined as an async function,
it's rolling out and infinite loop to iterate through nodes on a network.
The second function `locateScalpel2` avoids explicit use of async declaration

Both blocks have positive attributes that we'd like to use for our own
approach. The first block uses `async` and `await` keywords, which also means
that it avoids having to chain together callbacks with lots of dots...because
who needs dots, right? The second somehow made more sense to me initially because 
I'm learning scheme. It avoids explicit use of async declaration and makes use of 
javascript closures.

```
// example from eloquent javascript chpt. 11
// (relies on predefined function anyStorage)
async function locateScalpel(nest) {
  let current = nest.name;
  for (;;) {
    let next = await anyStorage(nest, current, "scalpel");
    if (next == current) return current;
    current = next;
  }
}


function locateScalpel2(nest) {
  function loop(current) {
    return anyStorage(nest, current, "scalpel").then(next => {
      if (next === current) return current;
      else return loop(next);
    });
  }
  return loop(nest.name);
}
```


Whatever way we go, we arrive at a commond call to `anyStorage`.


### Beginning of call stack list
```
anyStorage
```

If we further trace `anyStorage`, we see that the function contains two conditional
branches, depending on the values passed in as arguments the call stack list
will continue to grow as follows:

### call stack list (branch1):

This branch is chosen if the source is equal to the name of the nest (node) currently
being audited. Basically it means that we've found what we're looking for, so the
contents of the readStorage call becomes the result that is passed to the
`Promise`'s `resolve` method.

```
anyStorage - storage
anyStorage - storage - Promise
anyStorage - storage - Promise - readStorage
anyStorage - storage - Promise - readStorage - resolve

```

### class stack list (branch2):

The second branch is executed if the source and nest name differ. In this case,
the current nest (node) is set as the origin of the request for a route and the
source is set as the target. The request function explicity seeks a route
to the node pointed to by source.

```
anyStorage - routeRequest
anyStorage - routeRequest - request
anyStorage - routeRequest - request - Promise
anyStorage - routeRequest - request - Promise - attempt
anyStorage - routeRequest - request - Promise - attempt - send
anyStorage - routeRequest - request - Promise - attempt - send - reject | resolve
```

It's necessary to dig in to Marin Haverbeke's code in order to undestand
exactly what's going on. There's more complexity to the example he is showing
here, particularly in and around the model of network that he is constructing.
I highly recommend reading his book, it encourages the reader to dig in to core 
concepts and practices at work in javascript. 

## A simple use case

Okay, so the whole reason why I started looking into asynchronous javascript in
the first place was because I have to design a couple of simple web clients at
work. A typical situtaion is that I want to handle some authentication, and
then go on to make some requests to an API while passing the token in the
request headers. Just to get a handle on exactly what is going on when we
perform such requests, I used this fairly standardized function to query a
dummy endpoint that is set up on my local machine. This is pretty much all
there is to it for the time beeing, but see the code on [github](https://github.com/adammccartney/adapi-client) 
if you want to play around with it yourself.

```
async function fetchToken () {
    try {
        const response = await fetch("http://127.0.0.1:9001/tok.json");
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        const json = await response.json();
        console.log(json[0].GITLAB_API_TOKEN);
    }
    catch (error) {
        console.error(`Could not retrieve token: ${error}`);
    }
}

fetchToken();
```


# guidelines on callbacks sync and async

## Notes from: 
+ [havoc's blogpost](https://blog.ometer.com/2011/07/24/callbacks-synchronous-and-asynchronous/)

### choose sync or async but not both
Stay consistent with the API. Even if the data might be available immediately
in some instances, it's better to have a consistent API than to get exactly
what you want all the time.
**If the callback must be deffered in any situation, always defer it.**

### synchornized resources should defer all callbacks they invoke
Likely, you'll need to invoke some existing design pattern as a way to manage this

## Notes from:
+ [do not release zalgo](https://blog.izs.me/2013/08/designing-apis-for-asynchrony/)

### if the result is usually available right now, and performance matters a lot:
1. check if the result is available
2. if it is, return it
3. if it is not, return an error code, set a flag ...
4. provide some zalgo-safe mechanism for handling the error case and awaiting
   future availability.

### node.js callback pattern
1. Async function take a single callback function as their final argument
2. that callback is called in the future with the first argument set to an
   error object in the case of a failure, and any additional results as the
   subsequent arguments.


# node.js callback conventions

Continuation-passing style (CPS) is a technique from functional programming.
It's pretty intense, here are some scheme examples from wikipedia:

```
direct style:

(define (pyth x y)
 (sqrt (+ (* x x) (* y y))))


cps style:
(define (*& x y k)
  (k (* x y)))

(define (+& x y k)
  (k (+ x y)))

(define (pyth& x y k)
  (*& x x (lambda (x2)
          (*& y y (lambda (y2)
                  (+& x2 y2 (lamda (x2py2)
                            (sqrt& x2py2 k))))))))

```

## There are rules dear ...

Example from node.js
```
readFile(filename, [options], callback)
```

### any error always comes first 
in CPS style, errors are propegated like any other type of result, which means
using callbacks.

```
readFile('foo.txt', 'utf-8', (err, data) => {
    if (err) {
      handleError(err)
    } else {
      processData(data)
    }
})
```


# The observer pattern

built in to javascript by way of the EventEmitter object. Essential methods of
the EventEmitter object are:

+ `on(event, listener)`: with this it's possible to register a new listener (a
  function) for the given event type (a string)
+ `once(event, listener)`: registers a new listener, which is promptly removed
  once the event is emitted for the first time.
+ `emit(event, [arg1], [...])`: produces a new event and provides additional
  arguments to be passed to the listeners
+ `removeListener(event, listener)`: removes listener for a specific event type

## Event Emitters or Callbacks?

+ generally, callbacks don't handle multiple events as elegantly as
  EventEmitters
+ an `EventEmitter` should be used when the same event can occur multiple
  times. A callback is expected to be invoked exactly once, whether the
  operation is successful or not. (callbacks have a result to be returned,
  events are something that need to be communicated)
+ an API using callbacks can notify only one particular callback,
  `EventEmitter` we can register multiple listeners for the same event. 

# Patterns 
+ from node.js design patterns 

* Use blocking APIs sparingly and only when they don't affect the ability of
  the application to handle concurrent asynchronous operations.
* You can guarantee that a callback is invoked asynchronously by deferring its
  execution using process.nextTick()


# Callback best practices and control flow patterns

* Exit as soon as possible. This is context dependent, but basically you will
  want to exit the current statement by way of `return`, `continue`, or `break`
  as an alternative to writing complete `if...else` statements.
* Give callback functions names, keep them out of closures and pass
  intermediate results as arguments. Names will make stack traces easier to
  comprehend.
* Keep the code compact and modular, create small reusable functions wherever
  possible.



## How to avoid race conditions (it's easier than you might think)


# Resources

When it comes to the bricks and mortar stuff of javascript, I find the
[mdn](https://developer.mozilla.org/en-US/docs/Web/JavaScript) pretty great.
In particalar, they have a nice series on [asynchronous javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)


