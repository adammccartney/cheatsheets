# Cheat shee for gitlab running in container 


## Setup procedure
After installation / launch with the automated commands (ansible,
docker-compose), a log in as root is needed. After this initial login, we can
reconfigure the default password. To get this default password in the first
place, run: 

```
sudo docker exec -it <container> grep 'Password:' /etc/gitlab/initial_root_password
```



