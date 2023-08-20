#!/bin/bash
file=${1:-docker-compose.yml}

docker-compose -f ${file} down
