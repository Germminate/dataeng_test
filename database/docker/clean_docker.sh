#!/bin/bash

# Prune all containrs and images that are unused
docker container prune && docker image prune