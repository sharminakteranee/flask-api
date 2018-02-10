#!/bin/bash

echo "Stopping and removing the running container"
docker stop flask-one || true && docker rm -f flask-one || true
