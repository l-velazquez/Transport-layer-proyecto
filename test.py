from struct import *

f = open("Message.txt",'r')
rfile = f.readlines()

def packP(ack,checksum,payload):
    p1 = pack('B',ack)#send ack
    p2 = pack('I',checksum)#checksum
    p3 = pack('H',ord(payload))#message
    pf = p1 + p2 +p3
    return pf


ack = 0
checksum = 0
send2server = []
while True:
    for i in rfile:
        checksum = ack + len(i)
        print(i)
        print(type(i))
        send2server.append(packP(ack,checksum,i))
print(send2server)