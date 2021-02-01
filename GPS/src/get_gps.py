#!/usr/bin/env python
# -*- coding:utf-8 -*-


import roslib
import sys
import rospy
from sensor_msgs.msg import NavSatFix


gps_data = None

def gps_callback(data):
    global  gps_data
    gps_data = (data.latitude, data.longitude)  # 위도, 경도


def start():
    rospy.init_node("getGps")
    rospy.Subscriber("/gps_front/fix", NavSatFix, gps_callback)

    while not rospy.is_shutdown():
        if gps_data == None:
            continue


        print(gps_data)



if __name__ == '__main__':
    start()

