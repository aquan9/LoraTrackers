#A Python socket server. For transmitting the positions recieved over wifi to a laptop.
import socket

s = socket.socket()

port = 9999

s.bind(('', port))

s.listen(5)

while True:
    connection, address = s.accept()
    connection.send("test message")
    connection.close()
