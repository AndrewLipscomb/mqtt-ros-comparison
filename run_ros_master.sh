#!/bin/bash

set -e

docker build -t mqtt_ros_master -f ./ros_master.dockerfile --progress plain .

docker run --rm -it --network host mqtt_ros_master