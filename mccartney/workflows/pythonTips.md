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

Package imports 

* The following are a few notes from Mark Lutz on Package Import.

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

