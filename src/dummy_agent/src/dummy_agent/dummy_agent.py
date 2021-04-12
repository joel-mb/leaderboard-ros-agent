#!/usr/bin/env python

import rospy

from std_msgs.msg import Bool
from carla_msgs.msg import CarlaEgoVehicleControl


def dummy_agent():
    rospy.init_node("dummy_agent")
    rate = rospy.Rate(20) # 20hz

    publisher = rospy.Publisher("/carla/hero/vehicle_control_cmd", CarlaEgoVehicleControl, queue_size=1)
    ready = rospy.Publisher("/carla/hero/status", Bool, latch=True, queue_size=1)
    ready.publish(True)

    while not rospy.is_shutdown():
        control_msg = CarlaEgoVehicleControl()
        control_msg.header.stamp = rospy.Time.now() 
        control_msg.throttle = 1.0
        publisher.publish(control_msg)

        rate.sleep()


if __name__ == '__main__':
    try:
        dummy_agent()
    except rospy.ROSInterruptException:
        pass
