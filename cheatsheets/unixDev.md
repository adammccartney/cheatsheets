# Notes from the art of unix programming

Seperate out a programs parts and connect them using a simple command stream or
application protocol.

Design for simplicity not for ornateness or complexity.

# use unix as ide

# editing

- created a little script for running ctags on a source directory
  located at [[~/bin/maketags]]

Once the tags file is created, open vim in the root directory of the project
and use the commands `:tag /class/` to visit source listings. use `:tn | :tp`
to move forward or backward

# linting

gcc: it's possible to compile the program and cache the errors to an error.log
`g++ example.c -o example > error.log > 2&1`

error log can be opened in vim:
`vim -q error.log`

## vim QuickFix

global list

_Almost_ too lazy to read the docs. This tool/workflow is based around using
vimgrep to generate a list of search results

```
:vimgrep /^\#include/j ./*.c
```

This command allows you to jump to results that are found anywhere in the
directories specified in the grep search path

The results of this search are safed to the quickfix buffer, which you can
view in the quickfix window by running `:copen` and close again with `:cclose`.

To view what particular search is currently being viewed, run `:chistory`

The easiest way to cycle through history (meaning error lists) seems to be to
use `cnew[er]` `cold[er]`

### Location list

local list
Similar to quickfix lists, but it's possible to have multiple location lists
open at once.

# Compiling

# generating assembler output

`$ objdump -D example.o`

or

`$ gcc -c -S example.c -o example.s`

_there is a way to generate assembler output alongside c code_

# Building

# makefiles

Either all objects can be specified

```
all: example

example: main.o example.o library.o
    gcc main.o example.o library.o -o example

main.o: main.c
    gcc -c main.c -o main.o

example.o: example.c
    gcc -c example.c -o example.o

library.o: library.c
    gcc -c library.c -o library.o

clean:
    rm *.o example

install: example
    cp example /usr/bin
```

Or a more generic structure can be used

```

CC = gcc
OBJECTS = main.o example.o library.o
BINARY = example

all: example

example: $(OBJECTS)
    $(CC) $(OBJECTS) -o $(BINARY)

clean:
    rm -f $(BINARY) $(OBJECTS)

install: example
    cp $(BINARY) /usr/bin
```

# debugging

gdb can be run from within emacs in a way that looks really like a modern ide

it can also be run from the command line however and is quite effective in this
way

run it like this:
`gdb example`

once in the gdb session, run as normal...

```
(gdb) run


...
#if error

(gdb) backtrace


#then use
(gdb) step

```

Can even be used on a program that is running:

```
$ pgrep example
1524
$ gdb -p 1524
```

# Valgrind

a newer debugging tool see "learn c the hard way" for more info

# ltrace

`$ ltrace example`

produces all the system calls a program is making. useful for diagnosing
linkage problems. here's how to use it with an output file:

`$ ltrace -o example.ltrace ./example`

# track open files with lsof

```
$ pgrep example
1234
lsof -p 1234
```

another way to do this is to check the files open for a process in the dynamic
/proc directory

`ls -l /proc/1234/fd`

# view memory allocations with pmap

`# pmap 1234`
