
Getting Autocomplete to work in Vim with OpenFrameworks 
===============================================================================


In order to create new project first run: 

`source of/projectGenerator-linux64/projectGenerator --help`

(if you want to see how to set the paths again!) 


otherwise 

`source of/projectGenerator-linux64/projectGenerator -o"../"
../apps/myApps/newExample`

Once a "~/of/apps/myApps/newExample" is created

```
(plot)$:~/of/apps/myApps/newExample compiledb make
```

This will generatre a json make config file that YouCompleteMe can read. 

Keep a copy of this config handy when copying new projects. 
