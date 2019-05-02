import socket

s = socket.socket()

port = 9999

s.connect(('192.168.1.10', port))

print s.recv(1024)
s.close()


