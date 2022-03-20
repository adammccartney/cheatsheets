# Notes on using gnu make

# Targets

# Rules

# Include

- It is possible to call make recursively to make subdirectories

# Dependencies

It is quite often the case that source files that get made into object files
will depend on some header. This means that a there will be many instances of
writing a rule to make a specific file in this rule, the dependencies will be
specified. For single use cases, something like the following is practical:

```
main.o: defs.h
    #some compilation stuff
```

For projects that include a lot of targets and dependencies this is
impractical. Modern c compilers include the option for addint the `-M` flag
that automatically looks for the `#include `

There is a pattern that is common for automatically including
prerequisites...actually by creating another makefile for them.

This example is for the c compiler

```
%d: %.c
    @set -e; rm -f $@ \
    $(CC) -M $(CPPFLAGS) $< > $@.$$$$: \
    sed 's,\($*\)\.o[ :]*,\1. $@ : ,g' < $@.$$$$ > $@; \
    rm -f $@.$$$$
```

# Shared Libraries

Although static libraries are quite useful, they can produce large executable
files if there is a sufficiently large number of objects to be compiled.
The way around this is to use so called "shared" or "dynamic" libraries. You
have to watch out for the different naming conventions on the different
platforms:

```
# linux
SHARED_LIBRARY_EXTENSION = so
SHARED_LIBRARY_FLAGS = -shared

# macos
SHARED_LIBRARY_EXTENSION = dylib
SHARED_LIBRARY_FLAGS = -dynamiclib

# windows
SHARED_LIBRARY_EXTENSION = dll
SHARED_LIBRARY_FLAGS = ?

```

# gnu autoconf && gnu autotools

Started out as a way to set the variables that are machine dependent with make
