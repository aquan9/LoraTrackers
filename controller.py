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
            print(output)

    

if __name__ == "__main__":
    main()
