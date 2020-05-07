# Workflow for Score Packages
-------------------------------------------------------------------------------

Create two eponymous directories. 
 + Top level is wrapper 
 + Bottom level is contents


# wrapper
 + `reamde.md`
 + `setup.py`
 + `.travis.yml`
 + `test.py`
 + `.gitignore`
 + `./contents`

# contents

Give minimal overview of contents. 
```
   ./segments             # Contains all score segments 
    |_ __init__.py
    | |_ ./A
      | |_ __init__.py
        |_ definition.py
        |_ illustration.ly  # lilypond score
        |_ illustration.ily # lilypond music expressions (voices)
        |_ layout.py
        |_ .log             # seg, lilypond, capture timing, date stamp
        |_ .optimization

    ./materials             # Contains materials used to build segments
    |_ __init__.py
    | |_ ./instruments
      | |_ __init__.py
        |_ definition.py`
      |_./instrumentX-pitches
      | |_ __init__.py
        |_ definition.py
```

# Installing or adding to PYTHONPATH
==============================================================================

Possible to install package using `setup.py` file, but as we are usually
building only on personal computer, it makes more sense to simply add the
directory to the PYTHONPATH. Simple append the path of the new package to the
following command in the `.bashrc`

```
export PYTHONPATH=/home/user/newpackage1:/home/user/newpackage2
```

