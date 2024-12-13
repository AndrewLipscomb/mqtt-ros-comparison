#!/bin/bash

set -e

docker pull eclipse-mosquitto

docker run --rm -it --network host eclipse-mosquitto