# pythonTips.md
---------------

+ Always feed python live mice



Docstrings
=============================================================================

Document 
   + all modules
   + classes & functions exported by a module
   + Public methods
   + A package can be documented in the `__init__.py` in the package directory.

Format
   + """always use triple double quotes"""
   + r"""raw triple double quotes""" if srtring contains backslash
   + u"""Unicode triple-quoted strings"""


One line dostrings
   + describes function or method's effect as a command
   ```
   def function(a, b):
   """Do X and return as list."""
   ```
   
Mult-line Docstrings
   ## for a class 
   + should summarize behavior and list the public methods and instance
     variables. 

Imports 
==============================================================================
*notes from pep8*

The relatively obvious: 
  + imports are always put at the top of the file, after any module comments
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

* Avoid wildcard imports.

Packaging
==============================================================================

Package imports a few notes from Mark Lutz.

In order to import modules from a package, first set the PYTHONPATH
to look in the directory where the modules are stored. 
To do this 

   * on linux: to .bashrc, add export PYTHONPATH=/home/user/directoryToFind

   * on windows: append directory path to PYTHONPATH 

+ Formal structure: 
  
   * /dir0/dir1/dir2/mod
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


PEP-8 Styleguide
==============================================================================

                                                                              
* <https://www.python.org/dev/peps/pep-0008/>


Slicing
==============================================================================

A few tips from *effective python*

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
Used to iterate over a list, taking every *nth* item

Could be useful for creating arpegio seqeunces from a given scale: 
```
scale = ['c','d','e','f','g','a','b','c','d','e','f','g']
arpIMaj = scale[::2]
arpIIMi = scale[1::2]
```

Don't get too clever though! see also `itertools.islice`



