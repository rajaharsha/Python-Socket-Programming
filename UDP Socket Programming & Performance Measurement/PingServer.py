# Name: Raja Harsha Chinta
# UIN : 01043488
# Class: (CS 455 or CS 555), Spring 2014
# Program 1: PingServer.py

import random
import sys
import time
from socket import *

print ("Usage: python PingServer.py <server port no> <seed(optional)>")

# Check command line arguments
if len(sys.argv) > 3:
	print "Incorrect number of arguments passed.\nCorrect Usage: python PingServer.py <server port no> <seed(optional)>"
	sys.exit()

port_number = sys.argv[1]


# Assign user defined Seed
if len(sys.argv)>2:
        ip_seed = sys.argv[2]
        random.seed(ip_seed)

# Input Port Validation     
if port_number < 10001 and port_number > 11000:
    print "ERROR at Argument 1 - Enter a port address within range 10001 and 11000"
    sys.exit()

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', int(sys.argv[1])))

# Assign Default Average Delay Value
average_delay = 150


while True:
    # Generate random number in the range of 0 to 1
    rand = random.random()

    # Receive the client packet
    message, address = serverSocket.recvfrom(12000)
    recdTime = time.time() * 1000
    # Capitalize the message from the client
    message = message.upper()
    # If rand is less is than 0.26, we consider the packet lost and do not respond
    if rand < 0.26:
        print address[0]+":"+str(address[1])+">",message, "ACTION: not sent"
        continue
    # Otherwise, the server responds
    delay = (rand * 2 * average_delay)
    time.sleep(delay/1000.0)
    serverSocket.sendto(message, address)
    sendTime = time.time() * 1000
    rtt = int((sendTime-recdTime))
    print address[0]+":"+str(address[1])+">",message, "ACTION: delayed", rtt, "ms"
