#!/usr/bin/env bash

set -e

docker run -d --name flask-one -p 8088:8080 flask-one
