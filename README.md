## Docker Flask

This is a simple example of how create a container for a Python Flask Web Application using Docker.

### Installation

```shell
docker build -t docker-flask .
docker run --publish 3000:3000 --name docker-flask docker-flask
```

or run container in interactive mode:

```shell
docker exec -it docker-flask bash
```

or in detach mode:

```shell
docker run --name docker-flask -p 3000:3000 -d docker-flask 
```