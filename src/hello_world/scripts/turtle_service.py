#!/usr/bin/env python

import rospy
import random
from std_srvs.srv import Empty
def change_color():
   rospy.init_node("change_color", anonymous=True)
   rospy.set_param("turtlesim/background_r", random.randint(0, 255))
   rospy.set_param("turtlesim/background_b", random.randint(0, 255))
   rospy.set_param("turtlesim/background_g", random.randint(0, 255))
   rospy.wait_for_service("reset")
   try:
      serv = rospy.ServiceProxy("reset", Empty)
      serv()
      rospy.logwarn("reseting")
   except rospy.ServiceException:
      pass

if __name__ == "__main__":
   change_color()

