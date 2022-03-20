## pythonTips.md

- Always feed python live mice

# Classes & Inheritance

Use helper classes

- these are a good alternative to bookkeeping with dictionaries and tuples

Use functions to simplify interfaces instead of classes

- for instance, include a hook to report on operations being performed as
  part of a built in algorithm run (like sort) this hook can be a lamda
  expression that reports these can sort side effects from deterministic behaviour

# Decorators

_see also: first class functions, closures_

A decorator is a function that takes another function as an argument, adds some
kind of functionality and then returns another function. All of this without
altering the source code of the original function that gets passed in.

```
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before{}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
   print('display function ran')

display()

>>> wrapper executed this before display
... display function ran


```

If we want to pass a number of positional or keyword arguments to a wrapper
function, we need to specify this in the def of wrapper_function()

```
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before{}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
   print('display function ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)

>>> wrapper executed this before display
... display_info ran with arguments (John, 25)

```

# Decorator Class

```

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before{}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

class DecoratorClass(object):

    def __init__(self, original_fucntion):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before{}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
   print('display function ran')

>>> call method executed this before display
... display_info ran with arguments (John, 25)


```

##Practical Examples for decorators##

+Logging
+Timing

# Docstrings

Document

- all modules
- classes & functions exported by a module
- Public methods
- A package can be documented in the `__init__.py` in the package directory.

Format
`"""always use triple double quotes"""`
`r"""raw triple double quotes""" if srtring contains backslash`
`u"""Unicode triple-quoted strings"""`

One line dostrings

- describes function or method's effect as a command

```
def function(a, b):
"""Do X and return as list."""
```

Mult-line Docstrings

## for a class

- should summarize behavior and list the public methods and instance
  variables.

# Imports

_notes from pep8_

The relatively obvious:

- imports are always put at the top of the file, after any module comments
  /docstrings and before module globals and constants.

  1. Stdlib imports
  2. Third party
  3. Local / application specific

```
import math

import abjad

import frog
```

Absolute imports are recommended (see PEP8).

Explicit relative imports are an acceptable alternative.
For instance, any score package that uses abjad is a relatively complex
package, there for using the explicit relative import model is acceptable.

```
from .RhythmDefinition import RhythmDefinition
from .ScoreTemplate import ScoreTemplate
```

Imports from a class-containing module (i.e. many of the abjad modules)

```
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

or incase of a name clash, spell them explicitly:

```
import myclass
import foo.bar.yourclass
```

and use "myclass.MyClass" and "foo.bar.yourclass.YourClass" in the module.

- Avoid wildcard imports.

# iPython tips

- Good tip for testing is to enable the autoreload function

```
[1] %run  "foo.py"
[2] %load_ext autoreload
[3] %autoreload 2
[4] foo.f
...42
#[4] change foo.f
[5] foo.f
...43
```

# List Comprehensions

Use a list comprehension instead of filter and map.

```
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

squares = map(lambda x: x ** 2, a)

evensquares = [x**2 for x in a if x % 2 == 0]

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

```

Dictionaries and sets have their own equivalents of list comprehensions

```
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)
```

## Keep the number of expressions in a list comprehension down to two

Useful for laying a matrix flat, i.e. running nested for loops

```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)
```

If you want to replicate the two-level deep layout of the input list.
e.g. squaring each value in each cell of a 2d matrix

```
squared = [[x**2 for x in row] for row in matrix]
print(squared)
```

Also supports multiple if statements:

```
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x <= 4 if x % 2 == 0]
c = [x for x in a if x >= 4 and x % 2 == 0]
```

If they start to look like this, avoid

```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
```

PI\*Thumb Rule for list comprehensions

- Avoid using more than two expressions in a list comprehension. This cany be
  any combination of two conditions and/or loops.

_List comprehensions create new lists for each value in the input seqeunce_

# Use Generator Expressions for Large Comprehensions

_List comprehensions create new lists for each value in the input seqeunce_
This means memory useage can grow out of control and crash a program.

```
value = [len(x) for x in open('/tmp/my_file.txt')]
print(value)
```

To solve this, Python provides generator expressions, a generalization of list
comprehensions and generators. Generator expressions don’t materialize the whole
output sequence when they’re run. Instead, generator expressions evaluate to
an iterator that yields one item at a time from the expression.

```
it = (len(x) for x in open('/tmp/my_file.txt'))
print(it)
>>>
<generator object <genexpr> at 0x101b81480>
```

next function can be used to step through the generator function, always
picks up where it left off

```
print(next(it))
print(next(it))
>>>
1
2
```

Generator functions

```
def rgb():
    for r in range(256):
        for g in range(256):
            for b in range(256):
                yield r, g, b

it = rgb()
for x in range(5):
    print(next(it))
```

# Lists and Mutability

In stark contrasts to tuples, lists are mutable.

# Packaging

Package imports a few notes from Mark Lutz.

In order to import modules from a package, first set the PYTHONPATH
to look in the directory where the modules are stored.
To do this

- on linux: to .bashrc, add export PYTHONPATH=/home/user/directoryToFind

- on windows: append directory path to PYTHONPATH

* Formal structure:

  - /dir0/dir1/dir2/mod
    - dir1 & dir2 require `__init__.py`
    - dir0 does not require `__init__.py` (will be ignored if present)
    - dir0, not dir0/dir1, must be listed on the module search path sys.path

Package initialization

The first time python imports through a directory, it automatically runs all
the code in the modules' `__init__.py` files. Because of this fact, it's a useful
place to initialize a state required by files in the package. (Think about it
like a loadbang message in max).

Module usability declarations
Another use for the `__init__.py` files is that they declare the directory as a
python package.

Module namespace initialization

# PEP-8 Styleguide

- <https://www.python.org/dev/peps/pep-0008/>

# Slicing

A few tips from _effective python_

```
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle two:', a[3:-3])

>>>
First four: ['a', 'b', 'c', 'd']
Last four:  ['e', 'f', 'g', 'h']
Middle two: ['d', 'e']
```

Omit zeros from the start of slice commands in order to reduce visual noise

Cheatsheet:

```
a[:]      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:5]     # ['a', 'b', 'c', 'd', 'e']
a[:-1]    # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a[4:]     #                     ['e', 'f', 'g', 'h']
a[-3:]    #                          ['f', 'g', 'h']
a[2:5]    #           ['c', 'd', 'e']
a[2:-1]   #           ['c', 'd', 'e', 'f', 'g']
a[-3:-1]  #                          ['f', 'g']
```

Slicing returns a new list, reference to the original objects are maintained.

**Stride**
Used to iterate over a list, taking every _nth_ item

Could be useful for creating arpegio seqeunces from a given scale:

```
scale = ['c','d','e','f','g','a','b','c','d','e','f','g']
arpIMaj = scale[::2]
arpIIMi = scale[1::2]
```

Don't get too clever though! see also `itertools.islice`

# Virtual Environments

Install

cd '~/.virtualenvs'
`python3 -m venv %name`

To add a directory to PYTHONPATH go to bin/activate and append as if in .bashrc
`export PYTHONPATH=/user/home/directoryToFind`

# Using requirements

- run venv
- `python -m pip install -r requirements.txt

# Vim pequiliarities

- in order to run Jupyter-Vim you need the following packages:
  - PyQt5==5.14.0
  - PyQt5-sip

## Using pipenv to manage virtualenvs

```
mkdir ~/<somewhere>/django
cd django

pipenv install django~=3.1.0
```

To activate the environment: `pipenv shell`

`(django) $ django-admin startproject config .`
