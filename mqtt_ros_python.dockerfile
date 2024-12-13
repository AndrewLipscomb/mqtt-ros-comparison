FROM ubuntu:20.04 AS build_base

RUN apt-get update && apt-get install -y curl gnupg2
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" | tee /etc/apt/sources.list.d/ros-latest.list \
    && apt update

RUN apt-get install -y python3-pip
RUN apt-get install -y flatbuffers-compiler
RUN pip3 install flatbuffers paho-mqtt

FROM build_base AS mqtt_v1

RUN --mount=target=/source/mqtt_v1,type=bind,source=mqtt_v1,rw \
    mkdir -p /source/app \
    && flatc --python -o /source/app /source/mqtt_v1/message.fbs \
    && cp /source/mqtt_v1/*.py /source/app

FROM build_base AS mqtt_v2

RUN --mount=target=/source/mqtt_v2,type=bind,source=mqtt_v2,rw \
    mkdir -p /source/app \
    && flatc --python -o /source/app /source/mqtt_v2/message.fbs \
    && cp /source/mqtt_v2/*.py /source/app

FROM build_base AS ros_base

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ros-noetic-message-generation ros-noetic-rospy ros-noetic-catkin

FROM ros_base AS ros_v1

RUN --mount=target=/source/ros_v1,type=bind,source=ros_v1,ro \
    mkdir -p /source/app/src \
    && cp -r /source/ros_v1/* /source/app/src \
    && . /opt/ros/noetic/setup.sh \
    && cd /source/app \
    && catkin_make

FROM ros_base AS ros_v2

RUN --mount=target=/source/ros_v2,type=bind,source=ros_v2,ro \
    mkdir -p /source/app/src \
    && cp -r /source/ros_v2/* /source/app/src \
    && . /opt/ros/noetic/setup.sh \
    && cd /source/app \
    && catkin_make