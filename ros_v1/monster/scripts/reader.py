#!/usr/bin/env python3

import rospy
from monster.msg import Monster

def callback(monster_msg):
    rospy.loginfo(f"Received Monster: {monster_msg.name} with HP: {monster_msg.hp}")

def monster_listener():
    rospy.init_node('monster_listener', anonymous=True)
    rospy.Subscriber('monster', Monster, callback)
    rospy.spin()

if __name__ == '__main__':
    monster_listener()