from struct import *
from socket import *
import sys

print(sys.argv[1])


def packP(ack,checksum,message):
    p1 = pack('B',ack)#send ack
    p2 = pack('I',checksum)#checksum
    p3 = pack('H',message)
    print("sending", ack,checksum,message)
    pf = p1 + p2 + p3
    return pf

ADDRESS = "136.145.181.51"
PORT = 4206
serverAddrPort = (ADDRESS,PORT)
bufferSize = 4096
debug = 0

s = socket(AF_INET,SOCK_DGRAM)


x = int(input("What is the seq num?:"))
y = int(input("What is the chcksum"))
z = int(input("What is the message len?"))
p = packP(x,y,z)

s.sendto(p,serverAddrPort)

msg = s.recv(bufferSize)

print(msg.decode())