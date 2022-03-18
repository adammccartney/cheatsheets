# tips and tricks for working with nodejs

# Event Loop Phases

## Poll

Executes I/O related callbacks. This is the phase that application code is most
likely to execute in. When your main application code starts running, it runs
in this phase.

## Check

Here the callbacks that are triggered via `setImmediate()` are executed

## Close

Here the callbacks triggered via EventEmitter close events. For example, when a
net.Server TCP server closes, it emits a close event that runs a callback in
this phase.

## Timers

Callbacks scheduled using `setTimeout()` and `setInterval()` execute here

## Pending

Special system evens are run in this phase, like when a net.Socket TCP socket
throws an ECONNREFUSED error.

# Event Loop Tips

- _Don't starve the event loop_
  If you have to do a lot of processing within a certain stack, of say, 1000
  data records, consider making 10 batches of 100. Use `setImmediate()` at the
  end of each loop in order to continue and process the next batche.

- Never break up work with such work using `process.nextTick()` as this will
  lead to a microtask that never empties and the application will be trapped in
  this loop forever!

# Overview of Blocking

Be aware that most of the functionality of node is made to run in asynchronous
mode. This can lead to unpredictable behaviour if blocking (sync) and
non-blocking (async) modes are mixed.

# Filesystem operations

All functions are asynchronous by default, but many come with equivalent \*Sync
versions.

**fs module & POSIX**

- copy()
- unlink()
- chmod()
- mkdir()

## Two phases of a node.js program

### initialization phase

- sets up the program: loads modules, creates variables, reads config params
- if something goes wrong here, better to fail fast (and loud!)
- this is the only time you should consider synchronous file access

### operation phase

- program churns through the event loop
- given that many nodejs programs are networked, this means accepting
  connections, making requests and waiting on other kinds of I/O
- DO NOT USE synchronous file access methods during this phase!

**ex:** `require()` function is an example of this principle in action - it
synchronously evaluates the target module's code and returns the module object.
Either the module will successfully load or the program will not continue.

Generally, if the program could not possibly continue without the file then
it's OK to use synchronous file access.

# Installing packages

Typical dev install:

```
npm init -y
npm install --save-dev --save-exact <package>@v.x.x
```

**commit package-lock.json to version control**
