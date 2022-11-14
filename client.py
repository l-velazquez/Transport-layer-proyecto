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
#=========================================================================
#creates the socket
s = socket(AF_INET,SOCK_STREAM)
s.connect(serverAddrPort)
s.settimeout(1)

#=========================================================================
recvMsg = s.recv(bufferSize)
print("\n",recvMsg.decode())

try:
    s.settimeout(2) 
    r_pkt = s.recv(1024)
    s.settimeout(None)
 
except socket.timeout:
    print("Timeout")


'''
ack = 1
x = pack("i",ack)
print(x)

s.send(x)
rMsg = s.recv(bufferSize)
unpackedMsg = unpack('b',rMsg)
print(rMsg)

if unpackedMsg == ack+1:
    ack += 1
    packedMsg = pack('i',ack)
    s.send(packedMsg)

rMsg = s.recv(bufferSize)
print(rMsg)'''