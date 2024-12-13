#!/bin/bash

set -e

./build_mqtt_ros_programs.sh

docker run --network host --rm -it ros_v2 /bin/bash -c '. /source/app/devel/setup.bash; /source/app/src/monster/scripts/writer.py'
# docker run --network host --rm -it ros_v2 /bin/bash