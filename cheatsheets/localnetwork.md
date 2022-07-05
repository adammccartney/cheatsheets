some debugging tips for local network on laptop
===============================================

Word of warning, the orchestration of docker networks is tricky. Every time you
run a cluster with docker-compose to test something locally, this process will
leave behind a zombie network. For some reason these networks appear to
interfere with other network operations, like connection to the vpn. I'm not
exactly sure why this is happening. It could have something to do with resource
allocation to the network namespaces where the processes run. Possibly all
networks run within the tree of some namespace whose resources are ultimately
limited. If there are too many, there could be problems with connectivity. 

To see what network services the network manager is currently managing, run: 
```bash
ncli dev status
```



