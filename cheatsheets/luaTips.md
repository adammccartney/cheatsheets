# Some lua tips

## lexical conentions

- identifiers are any string of letters, digits and underscores
- beginning with single underscores are usually reserved for dummy variables

### reserved words

| and | break | do | else | elseif
| end | false | for | function | goto
| if | in | local | nil | not
| or | repeat | return | then | true
| until | while

### Comments

```
--
--[[
print('will not print')
--]]

---[[
print('will print')
--]]
```

### Global variables

Don't need declarations
It's not an error to initialize uninitialized variables
The simply return nil

ccard
5266 2744 9378 6783
07/23

### Types and values

```
 > type(nil)           --> nil
 > type(true)          --> boolean
 > type(9.4 * 3)       --> number
 > type("Hello world") --> string
 > type(io.stdin)      --> userdata
 > type(print)         --> function
 > type(type)          --> function
 > type({})            --> table
 > type(type(X))       --> string
```

userdata is useful for c types ... see below!

### Booleans

```
 > 4 and 5       --> 5
 > nil and 13    --> nil
 > false and 13  --> false
 > 0 or 5        --> 0
 > false or "hi" --> "hi"
 > nil or false  --> false
```

### Useful idioms

```
x = x or v
if not x then x = v
```

Equivalence for ternary expressions in C

```
((a and b) or c)
a ? b : c
```

ternary expressions reminder:

```
#include <iostream>
using namespace std;
int main() {
   int a = 10;
   int b = 20;
   int max = a > b ? a : b;
   cout << "Maximum value = " << max << "\n";
   return 0;
}
```

Maximum value = 20

> not nil --> true
> not false --> true
> not 0 --> false
> not not 1 --> true
> not not nil --> false

### standalone interpreter

- run code directly
  `% lua -e "print(math.sin(12))" --> -0.53657291800043`

- Load a library
  `"% lua -i -llib -e "x = 10"`
