"""
    Programmer: Luis Fernado Javier Velazquez Sosa
    Course: CCOM 4205 - Computer Networks
    Project: Transport layer - TCP

"""


from struct import *
from socket import *
from time import *

#Adress to connect to the server
ADDRESS = "lagrange.ccom.uprrp.edu"
PORT = 4205
serverAddrPort = (ADDRESS,PORT)
bufferSize = 4096
debug = 0

s = socket(AF_INET,SOCK_STREAM)
s.connect(serverAddrPort)
s.settimeout(1)

#s.bind(serverAddrPort)
recvMsg = s.recv(bufferSize)
print("\n",recvMsg.decode())

x = pack("i",1)
print(x)


s.send(x)
rMsg = recv(bufferSize)

print(rMsg)
