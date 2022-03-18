# Docker cheat sheet

## Debian install

### add gpg key

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

###

echo \
 "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
 $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

## Build with tag within directory

`docker build -t <mytag> .`

## To find docker port

```
$ docker ps
> containerID
$ containerip containerID
```

## Easier way to find port: use docker --publish

`docker run --publish 5000:5000 myapp-docker`

## Run in detached mode

`docker run -d -p 5000:5000 myapp-docker`

# Run a shell in the container

sudo docker exec -it 26c781b35c67 /bin/bash

# Volumes

A specific use case for volumes is that we want to run a containerized django
app with a postgres db. The app is complex enough that it's not possible to
initialize a fresh db from the container. So instead, we want to mount a
dummy/test db in order to get the container running. In this case we would
create a docker-compose file as follows:

```
version: "3.9"
services:
  web:
    build: ./src
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/src
    ports:
      - 8000:8000

  db:
    image: postgres:11
    restart: always
    ports:
      - 5432
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
      - ./postgres-data:/.local/var/lib/postgresql/scheitarchiv
```

Local ./postgres-data directory is now used by the postgres container.

mount your volume to droplet

make a symbolic link to volume mount

`ln -s /mnt/<volume_name> ./postgres-data`

start the container
`docker-compose up -d`

# Build Args

## Out of source builds

Sometimes it is useful to be able to pass the Dockerfile as an arg on the
command line.

```
docker build -f ./docker/Dockerfile -t mytag:latest
```

## Package managers who expect DNS

If you're trying to install packages from pypi, you'll need to make sure there
is adequate DNS resolution happening. For this to be the case, the container
needs to have an IP that is visible to external services. In some cases when
there is an external build tool involved, docker-compose or gitlab runner, this
seems to happen automatically. The builder seems to wrap the image in a network
context. Othertimes, you will need to explicitly pass a network flag when
running the build command.

```
docker build --network host -f ./docker/Dockerfile -t mytag:latest
```
