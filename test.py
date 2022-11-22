from struct import *
from socket import *
import sys

#print(sys.argv[1])

def checksum(sq,msgLen,byteMsg):
    chksum = sq + msgLen + byteMsg
    return checksum


def packP(ack,checksum,msgLen,message):
    p1 = pack('B',ack)#send ack
    p2 = pack('I',checksum)#checksum
    p3 = pack('H',msgLen)#
    p4 = message.ecode()

    print("sending", ack,checksum,msgLen,message)
    pf = p1 + p2 + p3 + p4
    return pf

ADDRESS = "136.145.181.51"
PORT = 4206
serverAddrPort = (ADDRESS,PORT)
bufferSize = 4096
debug = 0

s = socket(AF_INET,SOCK_DGRAM)

seq = 0
checksum = 0

f = open("Message.txt",'r')
rfile = f.readlines()
print(rfile)

for i in rfile:
    msgB = bytes(i,'ascii')
    lenMsgB = sum(msgB)
    lenMsg = len(i)
    print("Hello",type(seq),type(lenMsgB),type(lenMsg))
    chksum = checksum(seq,lenMsg,lenMsgB)
    toSend = packP(seq,chksum,lenMsg,i)
    print(toSend)
    s.sendto(toSend,serverAddrPort)
    print(s.settimeout(2))
    x = s.recv(bufferSize)
    print(x.decode())
    s.send(toSend,serverAddrPort)
        
        
    


p = bytes("Hello world!",'ascii')
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
    