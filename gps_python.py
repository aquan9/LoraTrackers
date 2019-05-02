#A script to get the current GPS location

from gps import *
import time

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

while 1:
    time.sleep(1)
    report = gpsd.next()
    latitude = getattr(report, 'lat', 0.0)
    longitude = getattr(report, 'lon', 0.0)
    times = getattr(report, 'time', '')
    print("latitude: " + str(latitude))
    print("longitude: " + str(longitude))
    print("time: " + str(times))
