#!/bin/bash

set -e

docker build -t mqtt_v1 --target mqtt_v1 -f ./mqtt_ros_python.dockerfile --progress plain .
docker build -t mqtt_v2 --target mqtt_v2 -f ./mqtt_ros_python.dockerfile --progress plain .
docker build -t ros_v1 --target ros_v1 -f ./mqtt_ros_python.dockerfile --progress plain .
docker build -t ros_v2 --target ros_v2 -f ./mqtt_ros_python.dockerfile --progress plain .

# docker run --rm -it mqtt_ros_master