#A script to get the current GPS location

from gps import *
import time

def getGPS():
    gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

    actual_value = False

    while 1:
        time.sleep(1)
        report = gpsd.next()
        latitude = getattr(report, 'lat', 0.0)
        longitude = getattr(report, 'lon', 0.0)
        times = getattr(report, 'time', '')

        #Verify that we're getting a real value from gpsd
        if(latitude == 0.0):
            actual_value = False
        else:
            actual_value = True

        if(actual_value == True):
            return("latitude:" + str(latitude) + " longitude:" + str(longitude) + " time:" + str(times))

if __name__ == "__main__":
    print(getGPS())
