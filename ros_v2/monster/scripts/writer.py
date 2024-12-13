#!/usr/bin/env python3

import rospy
from monster.msg import Monster, Tail

def monster_publisher():
    rospy.init_node('monster_publisher_v1', anonymous=True)
    pub = rospy.Publisher('monster', Monster, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        monster_msg = Monster()
        monster_msg.name = "Goblin"
        monster_msg.hp = 300
        monster_msg.angry = True
        monster_msg.tail.length = 200
        rospy.loginfo(f"Publishing Monster: {monster_msg.name} with HP: {monster_msg.hp}")
        pub.publish(monster_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        monster_publisher()
    except rospy.ROSInterruptException:
        pass