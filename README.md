You need docker installed, and for yourself to be part of the docker group so you can run these scripts without sudo

Both applications try to show the same process of evolution.

 - We start with V1 - a `Monster` definition, with a couple of scalar fields.
 - Then we evolve the requirements to needing an `angry` field, with a scalar bool, and a new tail type, with a length

You will want both the message brokers running first
In one terminal
```
./run_mqtt_broker.sh
```

Then

```
./run_ros_master.sh
```

For the flatbuffers + MQTT suite - you can hot swap in version 1 or 2 of either the reader or writer, at runtime, without any interruption. V1 readers can consume V2 writers without issue , and a V2 reader has the capacity to deal with things missing from a V1 message (the bool `angry` is defaulted to 0's - so false - the table `Tail` is how you'd better represent nullable fields)

For the ROS suite - trying to connect a V2 writer or reader to a V1 version results in failure, usually a silent one from the receiving end. Changing the definition of the message once established also requires a ROS master reboot.

Also consider the following

 - ROS is very heavy weight on the deployment side of things. The ROS versions here have nearly 2x the size of the MQTT versions, and this is with minimal deps from the ROS side.
```
ros_v2 latest a8bb35938c2a   22 minutes ago   880MB
ros_v1 latest 5e610f3de665   26 minutes ago   880MB
mqtt_v2 latest affbb9a4bb27   58 minutes ago   485MB
mqtt_v1 latest e8fc50535e99   3 hours ago      485MB
```
 - The amount of "stuff" involved to get ROS running is considerable. We have
   - Multiple apt packages from a thirdparty repository, needing to source environment variable "setup" files to both compile messages and run programs. It also requires a package.xml, 2x CMakeLists.txt and a very particular folder structure to get the ROS bit to work
   - MQTT + Flatbuffers requires installing `flatc` from Canonical and then running a single compile command once per build cycle - all without any environment variables.


