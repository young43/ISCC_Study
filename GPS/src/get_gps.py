#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import datetime
import simplekml


import rospy
from sensor_msgs.msg import NavSatFix

# MODE==1) create kml files
# MODE==2) just show data

kml = simplekml.Kml()
save_path = '/home/young/catkin_ws/src/ISCC_Study/GPS/kml/kml_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".kml"

gps_data = None
prev_time = None

def gps_callback(data):
    global gps_data
    global prev_time

    gps_data = (data.latitude, data.longitude)  # 위도, 경도
    prev_time = time.time()

def start():
    global kml
    global prev_time
    rospy.init_node("getGps")
    rospy.Subscriber("/gps_front/fix", NavSatFix, gps_callback)

    while not rospy.is_shutdown():
        if gps_data == None:
            continue

        if prev_time != None and time.time()-prev_time > 2:
            break

        print(gps_data)
        latitude, longitude = gps_data
        kml.newpoint(name="(lat/long)", description="lt/longt", coords=[(longitude, latitude)])
        time.sleep(0.5)

    kml.save(save_path)
    print('-------- Save KML files({}) --------'.format(save_path.split('/')[-1]))

if __name__ == '__main__':
    start()

