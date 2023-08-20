#!/bin/bash

container_id=$(docker ps -aqf "name=^monitor$")
docker logs -f ${container_id}