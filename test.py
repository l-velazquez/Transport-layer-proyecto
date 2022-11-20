from struct import *
from socket import *


def packP(ack,checksum,message):
    p1 = pack('B',ack)#send ack
    p2 = pack('I',checksum)#checksum
    p3 = message.encode()
    pf = p1 + p2 + p3
    return pf

ADDRESS = "136.145.181.51"
PORT = 4205
serverAddrPort = (ADDRESS,PORT)
bufferSize = 4096
debug = 0

s = socket(AF_INET,SOCK_DGRAM)

seq = 0
checksum = 0

f = open("Message.txt",'r')
rfile = f.readlines()
for i in rfile:
    checksum = seq + len(i)
    s.sendto(packP(seq,checksum,i),serverAddrPort)
    x = s.recv(bufferSize)
    print(x)
    


p = bytes("Hello world!",'utf-8')
print(p)
print(len(p))

ack = 0
checksum = 0
sum = 0
send2server = []

for i in rfile:
    checksum = ack + len(i)   
    send2server.append(packP(ack,checksum))
    ack+=1
        
    
  
print(send2server)
for i in send2server:
    print("Sending",i)
    