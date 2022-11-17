"""
    Programmer: Luis Fernado Javier Velazquez Sosa
    Course: CCOM 4205 - Computer Networks
    Project: Transport layer - TCP

"""


from struct import *
from socket import *
from time import *

#Adress to connect to the server
ADDRESS = "136.145.181.51"
PORT = 4205
serverAddrPort = (ADDRESS,PORT)
bufferSize = 4096
debug = 0
#=========================================================================
#creates the socket
s = socket(AF_INET,SOCK_DGRAM)
#=========================================================================
recvMsg = s.recv(bufferSize)
print("\n",recvMsg.decode())
num = 1
while (num <= 30):
    s.send(pack("B",num))
    
    try:
        s.settimeout(2) 
        r_pkt = s.recv(1024)
        s.settimeout(None)
    
    except socket.timeout:
        print("Timeout")
    num += 1


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