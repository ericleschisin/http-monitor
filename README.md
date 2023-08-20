## dependencies
A docker daemon will be needed, either from [Docker desktop](https://www.docker.com/products/docker-desktop/)
or an opensource tool like [podman](https://podman.io/)

## Local dev
Build project with:
```
./build.sh
```

quickly run project with.
```
./dev_up.sh
```
or provide alternate config file to python and mount to container
```
docker run -v $(pwd):/config monitor /config/alternate_config.yaml
```

quickly connect to running container's standard out with.
```
./logs.sh
```

stop running container with.
``````
./dev_down.sh