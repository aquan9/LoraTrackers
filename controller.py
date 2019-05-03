#A program to control coordinate gathering and transmission
#Arguments are as follows: python controller.py <ID> <Mode>
#Mode can be either transmitter or reciever.
import os
import sys
import subprocess
from gps_python import getGPS

def main():
    if(len(sys.argv) != 3):
        print("Incorrect number of arguments")
        print("Arguments are as follows: python controller.py <ID> <Mode>")
        return

    node_id = sys.argv[1]
    node_mode = sys.argv[2]
    if(node_mode != "sender" and node_mode != "reciever"):
        print("Mode must be either sender or reciever")
        return

    if(node_mode == "sender"):
        while(1):
            gps_info = getGPS()
            gps_info = str(sys.argv[1]) + ": " + gps_info
            print(gps_info)
            subprocess.call(["sudo", "./dragino_lora_app", "sender", gps_info])

    if(node_mode == "reciever"):
        while(1):
            output = subprocess.check_output(["sudo", "./dragino_lora_app", "rec"])
            longitude = 0
            latitude = 0
            time = 0
            node = 0
            node_tracking = {}
            output = output.split("\n")
            for line in output:
                if("longitude" in line):
                    line = line.split(" ")
                    node = line[1]
                    latitude = line[2]
                    longitude = line[3]
                    time = line[4]
                    print(line)
                    print(node)
                    print(latitude)
                    print(longitude)
                    print(time)
                    status = [latitude, longitude, time]
                    node_tracking[node] = status
                    print node_tracking
                    with open("locations.txt", 'w') as f:
                        for key in node_tracking:
                            f.write(str(key) + str(node_tracking[key]))



    

if __name__ == "__main__":
    main()
