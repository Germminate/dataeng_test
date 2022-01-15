#!/bin/bash

# Prevent continuation if one step fails
set -euo pipefail

# Get current drive
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Building docker image ..."
sudo docker build --network=host \
    -t data_pipeline \
    -f $DIR/Dockerfile \
    $DIR/..


sudo docker run --privileged --rm -it --net=host --shm-size=1gb \
-e DISPLAY \
-e TERM=xterm-256color \
-e TZ="Asia/Singapore" \
$@ \
data_pipeline:latest