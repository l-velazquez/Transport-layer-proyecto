from struct import *

f = open("Message.txt",'r')
rfile = f.readlines()

def packP(ack,checksum):
    p1 = pack('B',ack)#send ack
    p2 = pack('I',checksum)#checksum
    pf = p1 + p2
    return pf


ack = 0
checksum = 0
sum = 0
send2server = []

for i in rfile:
    checksum = ack + len(i)   
    send2server.append(packP(ack,checksum))
        
    
  
print(send2server)
for i in send2server:
    print("Sending",i)
    