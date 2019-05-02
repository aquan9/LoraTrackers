#A Python socket server. For transmitting the positions recieved over wifi to a laptop.
import socket

#Setup the socket
s = socket.socket()
port = 9999
s.bind(('', port))
s.listen(5)

#The message we will be sending
#This message will update based on the locations.txt file produced by the LoRa code. 
transmit_message = "No Transmit message yet"

while True:
    try:
        transmit_file = open('locations.txt', 'r')
        transmit_message = transmit_file.read()
        transmit_file.close()
    except:
        transmit_message = "Waiting for locations.txt file to be produced"
        
    connection, address = s.accept()
    connection.send(transmit_message)
    connection.close()
