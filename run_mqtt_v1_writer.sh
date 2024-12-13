#!/bin/bash

set -e

./build_mqtt_ros_programs.sh

docker run --network host --rm -it mqtt_v1 /source/app/writer.py