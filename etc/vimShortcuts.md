Vim cheatsheet
==============================================================================

## Search and replace

search for term in specific range: 

`:5,12s/foo/bar/g`


## Splitting windows

Opening ( :sp, :split, :vs, :vsplit, CTRL-W_s, CTRL-W_v )
Closing ( :q, :quit, <Leader>q )
Focusing ( :on, :only, <Leader>o )


# QuickFix
global list 

*Almost* too lazy to read the docs. This tool/workflow is based around using
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
Similar to quickfix lists, but it's possible to have multiple location  lists
open at once. 


# Creating an error log

using the compiler: 
`g++ file.c > error.log 2>&1`

using make:
`make > error.log 2>&1`


This error log can be opened using the -q flag:
`vim -q error.log`