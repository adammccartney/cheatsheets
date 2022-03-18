# asynchronous javascript

Talk about complicated...

So here are some notes on various strategies pertaining to the use of
asynchronous javascript.

There is a well thought out chapter in [eloquent javascript](https://eloquentjavascript.net/code/#11.1)
on the topic that goes into some detail. Asynchronous code is hairy no matter what way you look
at it. The first example below `locateScalpel` is defined as an async function,
it's rolling out and infinite loop to iterate through nodes on a network.
The second function `locateScalpel2` avoids explicit use of async declaration

the second somehow makes more sense to me at the moment. It's a bit trickíer to
follow, but it avoids explicit use of async declarat

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

Let's break down the call stack for the second function. The interpreter reads
the `localScalpel2(nest)` block until it reaches the tail call
`loop(nest.name)` this is pushed onto the call stack

```
call stack list: loop(nest.name)
```

it then enters the loop and begins to resolve the call to `anyStorage`

```
call stack list: loop - anyStorage
```

If we further trace `anyStorage`, we see that the function contains two conditional
branches, depending on the values passed in as arguments the call stack list
will continue to grow as follows:

```
call stack list (branch1):
loop - anyStorage - storage
loop - anyStorage - storage - Promise
loop - anyStorage - storage - Promise - readStorage
loop - anyStorage - storage - Promise - readStorage - resolve

```

```
class stack list (branch2):
loop -anyStorage - routeRequest
loop -anyStorage - routeRequest - request
loop -anyStorage - routeRequest - request - Promise
loop -anyStorage - routeRequest - request - Promise - attempt
loop -anyStorage - routeRequest - request - Promise - attempt - send
loop -anyStorage - routeRequest - request - Promise - attempt - send - reject | resolve
```

```
function anyStorage(nest, source, name) {
  if (source == nest.name) return storage(nest, name);
  else return routeRequest(nest, source, "storage", name);
}
```

Here is one of the fundamental routines from the same library from eloquent js.
Nest is referring to the specific construct that has been put in place for
explaining the logic of (crow) networks within the chapter.

```
var Timeout = class Timeout extends Error {}

function request(nest, target, type, content) {
  return new Promise((resolve, reject) => {
    let done = false;
    function attempt(n) {
      nest.send(target, type, content, (failed, value) => {
        done = true;
        if (failed) reject(failed);
        else resolve(value);
      });
      setTimeout(() => {
        if (done) return;
        else if (n < 3) attempt(n + 1);
        else reject(new Timeout("Timed out"));
      }, 250);
    }
    attempt(1);
  });
}
```

Interesting also is the definition of Node within the same library (this is
what the nest instances are made of)

Note the use of the javascript `Symbol` primitive in order to establish a kind
of weak encapsulation [mdn docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)

```
  const $storage = Symbol("storage"), $network = Symbol("network")

  function ser(value) {
    return value == null ? null : JSON.parse(JSON.stringify(value))
  }

  class Node {
    constructor(name, neighbors, network, storage) {
      this.name = name
      this.neighbors = neighbors
      this[$network] = network
      this.state = Object.create(null)
      this[$storage] = storage
    }

    send(to, type, message, callback) {
      let toNode = this[$network].nodes[to]
      if (!toNode || !this.neighbors.includes(to))
        return callback(new Error(`${to} is not reachable from ${this.name}`))
      let handler = this[$network].types[type]
      if (!handler)
        return callback(new Error("Unknown request type " + type))
      if (Math.random() > 0.03) setTimeout(() => {
        try {
          handler(toNode, ser(message), this.name, (error, response) => {
            setTimeout(() => callback(error, ser(response)), 10)
          })
        } catch(e) {
          callback(e)
        }
      }, 10 + Math.floor(Math.random() * 10))
    }

    readStorage(name, callback) {
      let value = this[$storage][name]
      setTimeout(() => callback(value && JSON.parse(value)), 20)
    }

    writeStorage(name, value, callback) {
      setTimeout(() => {
        this[$storage][name] = JSON.stringify(value)
        callback()
      }, 20)
    }
  }
```
