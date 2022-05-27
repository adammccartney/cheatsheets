# commonlisp

## setup for sbcl and quicklisp


### sbcl 

Get the right distribution of steel bank common lisp
[](http://www.sbcl.org/platform-table.html)

grab the binary
```
tar -xfv sbcl-2.2.4-x86-linux-binary.tar.bz2
```
install it
```
cd sbcl-2.2.4-x86-linux
sh install.sh
```

### quicklisp

install via package manager
```
apt-get install cl-quicklisp
```

load from repl
```
(load "/usr/share/common-lisp/source/quicklisp/quicklisp.lisp")
(quicklisp-quickstart:install)
```

set to load by default (adds to ~/.sbclrc
```
(ql:add-to-init-file)
```



