#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def chatter_callback(msg):
   rospy.loginfo("RECEVIED: %s" % msg.data)
   

def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("chatter", String, chatter_callback)
    rospy.spin()

if __name__ == "__main__":
   listener()
