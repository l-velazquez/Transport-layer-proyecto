from struct import *
from socket import *
import sys

#print(sys.argv[1])

#Calculate checksum
def checksum(sq,msgLen,bMsg):
    chksum = sq + msgLen + bMsg
    return chksum

#Pack the package to send to the server
def packP(ack,checksum,msgLen,message):
    p1 = pack('B',ack)#send ack
    p2 = pack('I',checksum)#checksum
    p3 = pack('H',msgLen)#message length
    p4 = message.encode()#message encode

    #print("sending", ack,checksum,msgLen,message)
    pf = p1 + p2 + p3 + p4
    return pf

#Byte representation
def byteR(i):
    msgB = bytes(i,'ascii')
    MsgBsum = sum(msgB)
    lenMsg = len(i)
    return MsgBsum,lenMsg


ADDRESS = "136.145.181.51"
PORT = 4206
serverAddrPort = (ADDRESS,PORT)
bufferSize = 4096
debug = 0

s = socket(AF_INET,SOCK_DGRAM)

#Initializing sequence number and cheaksum
seq = 0
chksum = 0

#opening file
f = open("Message.txt",'r')
rfile = f.readlines()
print(rfile)

for i in rfile:
    #sum of the byte representation and length
    MsgBsum ,lenMsg = byteR(i) 
    #print("Hello",type(seq),type(lenMsgB),type(lenMsg))
    chksum = checksum(seq,lenMsg,MsgBsum)
    pack2send = packP(seq,chksum,lenMsg,i)
    #print(pack2send)
    s.sendto(pack2send,serverAddrPort)
    x = s.recv(bufferSize)
    #print(x)
    msgUnpacked = unpack("B",x)
    print("ACK:",msgUnpacked[0])
    seq += 1
        
        


for i in rfile:
    checksum = ack + len(i)   
    send2server.append(packP(ack,checksum))
    ack+=1
        
    
  
print(send2server)
for i in send2server:
    print("Sending",i)
    