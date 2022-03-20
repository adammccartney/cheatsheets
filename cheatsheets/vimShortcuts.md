# Vim cheatsheet

## Search and replace

search for term in specific range:

`:5,12s/foo/bar/g`

## Splitting windows

Opening ( :sp, :split, :vs, :vsplit, CTRL-W_s, CTRL-W_v )
Closing ( :q, :quit, <Leader>q )
Focusing ( :on, :only, <Leader>o )

# QuickFix

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

# Location list

local list
Similar to quickfix lists, but it's possible to have multiple location lists
open at once.

# Creating an error log

using the compiler:
`g++ file.c > error.log 2>&1`

using make:
`make > error.log 2>&1`

This error log can be opened using the -q flag:
`vim -q error.log`

# Migration from pathogen to vim-plug

1. Install vimplug
2. change vimrc file

```
call plug#begin('~/.vim/plugged')
Plug <link to plugin git>
class plug#end()
```

## Reflow a text

Select a block of text visually and invoke `gq`

## Jump to closing tag (html)

- enter visual mode
- select outer tag block `a t`, or inner tag block `i t`

`:help visual-operators`

## Search and replace across multiple buffers

```
:bufdo %s/rhythm/petunias/gce
```

then 

```
:bufdo wq!
=======
## Open a number of files in tabs

```
vim -p `find . -type f -name <filename>`
```
