# dependency / config list for remote supercollider isntance

## Supercollider:
+ CTK quark
```
sclang>
Quarks.install("https://github.com/supercollider-quarks/UnitTesting.git");
```


## Docker 

+ run docker build

```
local> ssh adam@$REMOTE1
remote> docker build -t scnrtcloud .
remote> docker run -it -d --name scnrt scnrtcloud
```


## Docker volumes 

We're going to need to use docker volumes to manage the score file
i.e. the container only ever has one state and this does not get modified 

