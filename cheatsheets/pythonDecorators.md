# Decorators and Scoping

Python has some really great features in and around decorators. At first glance
they appear to be somehow superfluous type of syntactic sugar or something
along those lines. This is not the case.

There are a number of great use cases for decorators:

- tidier class interfaces with better encapsulation
- any sort of measurement, whether of time or space complexity
  space complexity refers to the number of calls that a recursive
  routine or loop will make. Wheras time complexity refers to the speed that
  these calls (or the routine as a whole) will take to complete.

## Measurement Tools

There are class based ways to do these sorts of things also, but generally
speaking these types of functions with nested scope seems to work a bit more
readily. Mark Lutz has loads of great code examples, that's where the ones
below are taken from.

### Tracer

```
def tracer(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"call {calls} to {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@tracer
def fib(n):
    if (n < 0):
        print("Incorrect value for arg")
    elif (n == 0):
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


```

### Timer

```
def timer(label='', trace=True):             # On decorator args: retain args
    def onDecorator(func):                   # On @: retain decorated func
        # clk id for monotonic (RAW hardware based time) clock
        clk_id = time.CLOCK_MONOTONIC
        def onCall(*args, **kargs):          # On calls: call original
            nonlocal clk_id
            start   = time.clock_gettime(clk_id)           # State is scopes + func attr
            result  = func(*args, **kargs)
            elapsed = time.clock_gettime(clk_id) - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator

@timer('==>')
def fib(n):
    if (n < 0):
        print("Incorrect value for arg")
    elif (n == 0):
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```
