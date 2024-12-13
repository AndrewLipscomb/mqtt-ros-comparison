FROM ubuntu:20.04

RUN apt-get update && apt-get install -y curl gnupg2
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" | tee /etc/apt/sources.list.d/ros-latest.list \
    && apt update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ros-noetic-roslaunch ros-noetic-catkin

CMD /bin/bash -c "source /opt/ros/noetic/setup.bash && /opt/ros/noetic/bin/roscore"
