"""
    Programmer: Luis Fernado Javier Velazquez Sosa
    Course: CCOM 4205 - Computer Networks
    Project: Transport layer - TCP

    Discription: 
    This program will send a packege to a server
    that will act as a tcp connection. This client
    will send the sequence number, checksum and
    payload length and the payload it self. 

"""

from struct import *
from socket import *
import sys

#print(sys.argv[1])
#when final the user need to input the file it wants
if len(sys.argv) < 2:
    print("You need to insert the file to send")

#static variables
ADDRESS = "136.145.181.51"
PORT = 4206
serverAddrPort = (ADDRESS,PORT)
bufferSize = 4096
debug = 0

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
    msgBsum = sum(msgB)
    lenMsg = len(i)
    return msgBsum,lenMsg

s = socket(AF_INET,SOCK_DGRAM)

#Initializing sequence number and cheaksum
seq = 0
chksum = 0

#opening file
f = open("Message.txt",'r')
rfile = f.readlines()
#print(rfile)

for i in rfile:
    #sum of the byte representation and length
    msgBsum ,lenMsg = byteR(i) 
    chksum = checksum(seq,lenMsg,msgBsum)
    ack = 0

    #print("Packing:",seq,chksum,lenMsg,i)
    pack2send = packP(seq,chksum,lenMsg,i)

    if debug:
        print("Elements to calculate checksum:",seq,lenMsg,msgBsum)
        print("Checksum =",chksum)
        print("Package to send:",pack2send)

    #print(pack2send)
    while True:
        s.sendto(pack2send,serverAddrPort)
        print("Sending package",seq)
        try:
            s.settimeout(2)
            x = s.recv(bufferSize)
        except:
            print("Timeout")
            s.sendto(pack2send,serverAddrPort)
            break
        #unpack the message that is an acknowlage 
        ack = unpack("B",x)[0]
        
        if ack == seq+1:
            print("ACK:",ack)
            seq += 1
            break
        #added this to make the code funtion
        elif ack > seq+1:
            seq += 1
            print("ack",ack)
        else: 
            print("Ack",ack)
            seq = ack
            continue


print("-"*75)     
print("\nThanks for using the UDP+ service. Reliably sending your message. Thanks!\n")
print("-"*75)           
        



    
  
