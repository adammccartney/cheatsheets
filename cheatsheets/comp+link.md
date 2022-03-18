# A few notes on compiling and linking with gcc

# Building a static library with cpp

Good tutorial on using make to build a static library in the c++ cookbook.
The approach that I opted for was to follow their makefile recipe and adapt it
for use on my linux syste -> basically tayloring the install to suit a
build that starts in a $HOME/.local/src directory and leverages the typical
linux directory structure.

1. Teach make about the repo contents and target directories

2. define phony target for library

3. define recipe to build \*.a from source

4. leverage directory structure to make install, same for make clean

**Caveat emptor: make sure the custom directories are included in the $PATH**

# Recipe for building a complex application from the command line

1. build the static / dynamic library

2. compile the app's cpp file into object files
