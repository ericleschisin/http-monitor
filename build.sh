#!/bin/bash
name="monitor"
version=${1:-latest}

docker build . -f Dockerfile -t ${name}:${version}