#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker_node():
   rospy.init_node("talker", anonymous= True)
   pub =  rospy.Publisher("chatter", String, queue_size=10)
   rate = rospy.Rate(10)
   while not rospy.is_shutdown():
      s = "hello real world : %s" %rospy.get_time() 
      rospy.loginfo(s)
      msg = String()
      msg.data = s
      pub.publish(msg)
      rate.sleep()
if __name__ == "__main__":
   try:
      talker_node()
   except rospy.ROSInterruptException:
      pass