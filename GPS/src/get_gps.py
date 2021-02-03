#!/usr/bin/env python
# -*- coding:utf-8 -*-


import time
import rospy
from sensor_msgs.msg import NavSatFix


gps_data = None
prev_gps_data = None

def gps_callback(data):
    global gps_data
    global prev_time

    prev_time = time.time()
    gps_data = (data.latitude, data.longitude)  # 위도, 경도


def start():
    global gps_data
    rospy.init_node("getGps")
    rospy.Subscriber("/gps_front/fix", NavSatFix, gps_callback)

    while not rospy.is_shutdown():
        if gps_data == None: continue

        if prev_time != None and time.time()-prev_time >= 5:
            print('GPS get data Finished')
            break

        # kml data append

        time.sleep(0.5)

    # save kml
    print("helloworld")



if __name__ == '__main__':
    start()

