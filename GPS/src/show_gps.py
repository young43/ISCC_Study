#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import numpy as np
from pykml import parser
from pyproj import Proj, transform, itransform
import matplotlib.pyplot as plt

# GPS -> 평면계 좌표변환
proj_UTMK = Proj(init='epsg:5178')
proj_WGS84 = Proj(init='epsg:4326')

if __name__=='__main__':
    # python show_gps 경로1 경로2 ...
    # python show_gps.py ../kml/kml_notrk_20210201.kml ../kml/kml_rtk_20210201.kml
    if len(sys.argv) != 2:
        print('Non KML file''s directory...')
        pass

    for idx, path in enumerate(sys.argv[1:]):
        root = parser.fromstring(open(path, 'r').read())
        x_lst = []
        y_lst = []
        for place in root.Document.Placemark:
            x1, y1, _ = list(map(float, str(place.Point.coordinates).split(',')))

            x_lst.append(x1)
            y_lst.append(y1)

        # GPS(WGS84) -> UTM-K 변환
        coordinate = np.array([pt for pt in itransform(proj_WGS84, proj_UTMK, zip(x_lst, y_lst))])
        x_coord, y_coord = np.hsplit(coordinate, 2)

        file_name = path.split('/')[-1].split('.')[0]
        plt.plot(x_coord, y_coord, label=file_name)

    plt.title('KML(GPS) to UTM-K')
    plt.legend()
    plt.show()

