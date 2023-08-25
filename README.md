## dependencies
A docker daemon will be needed, either from [Docker desktop](https://www.docker.com/products/docker-desktop/)
or an opensource tool like [podman](https://podman.io/)

## Local dev
Build project with:
```
make build
```

quickly run project with.
```
make
```
or provide alternate config file to python and mount to container
```
docker run -v $(pwd):/config monitor /config/alternate_config.yaml
```

quickly connect to running container's standard out with.
```
make logs
```

stop running container with.
```
make down
```