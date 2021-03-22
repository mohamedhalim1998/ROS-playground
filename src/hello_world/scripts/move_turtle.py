#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from sys import argv


def pose_callback(pose):
   rospy.loginfo("Robot pose: %s", pose)


def controller(linear, angle):
   rospy.init_node("turtle_control", anonymous=True)
   pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
   rospy.Subscriber("/turtle1/pose",Pose, pose_callback)
   rate = rospy.Rate(10)
   msg = Twist()
   msg.linear.x = linear
   msg.angular.z = angle
   while not rospy.is_shutdown():
      rospy.loginfo("Linear Vel = %f: Angular Vel =%f",linear,angle)
      pub.publish(msg)
      rate.sleep()

if __name__ == "__main__":
   try:
      controller(float(argv[1]), float(argv[2]))
   except rospy.ROSInterruptException:
      pass