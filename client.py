"""
    Programmer: Luis Fernado Javier Velazquez Sosa
    Course: CCOM 4205 - Computer Networks
    Project: Proyecto de Bono - Transport Layer

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

val = True

while val:
    #Print to terminal for the client
    print("Please choose one operation:\n\t1.Sum\n\t2.Substraction\n\t3.Muliplication\n\t4.Division\n\t5.Factorial\n\t6.Summatory")
    inp = int(input("\nOperation >>> "))
    #if the numbers are from 1-4, 2 inputs are necessary
    if (inp > 6):
        print("Please enter the correct value!!!\a")
        continue
    elif(inp < 5 and inp <= 6):
        print("Please add two inputs:")
        inp1 = pack("i",int(input("Input 1 >>> ")))
        inp2 = pack("i",int(input("Input 2 >>> ")))
        inp0 = pack("B", inp)
        inp2send = (inp0+inp1+inp2)
        #print(unpack("iii",inp2send))

    #else thier will only be one input
    else:
        print("Input one number")
        inp1 = pack("i", int(input("Input >>> ")))
        inp0 = pack("B",inp)
        inp2send = (inp0+inp1)
    print("Sending package...")
    s.send(inp2send)
    message = s.recv(bufferSize)
    #debugger
    #---------------------------------------------------------------------
    if debug:
        print(str(message))
        print(len(message))
        print("message[0] = ",message[0])
        #print(unpack("i",message[1:5]))
    #---------------------------------------------------------------------

    result = None
    if len(message)< 2:
        if message[0]==2:
            print("You can't divide by zero (0).")
        elif mesage[0]==3:
            print("Invalid command, please try again.")
        else:
            break

    else:
        result = message[0]
        result1 = (unpack("i",message[1:5]))[0]
        print("pack num:", result, "and the answer is:",result1)
   
    cont = input("\nDo you want to continue?(Y/n)")
    if cont == "y" or cont == "Y":
        val = True
    else:
        val = False


print("\n\nThanks for using the program. Good bye!")
