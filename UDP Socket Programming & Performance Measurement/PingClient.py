# Name: Raja Harsha Chinta
# UIN : 01043488
# Class: (CS 455 or CS 555), Spring 2014
# Program 1: PingClient.py

import socket
import time
import sys
from socket import *

print "Usage: python PingClient.py <server ip address> <server port no>"

# Check command line arguments
if len(sys.argv) != 3:
    print "Incorrect number of arguments passed.\nCorrect Usage: python PingClient.py <server ip address> <server port no>"
    sys.exit()

host_name = sys.argv[1]
port_number = sys.argv[2]

# Host Name validation
if bool(host_name == gethostname() or host_name == 'localhost' or host_name == '127.0.0.1') == 0:
    print "ERROR at Argument 1 - Incorrect Host Name Entered"
    sys.exit()

# Input Port validation    
if port_number in range(10001, 11001):
    print "ERROR at Argument 2 - Incorrect Port Name Entered"
    sys.exit()
    
# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set waiting time of two seconds for reponse from server
clientSocket.settimeout(2)

# Declare server's socket address
remoteAddr = (sys.argv[1], int(sys.argv[2]))

s=0
f=0
Max_RTT = 0
Min_RTT = 0
Avg_RTT = 0
a_rtt = []

# Ping Server 10 times
for i in range(0,10):
    sendTime = time.time() * 1000
    message = 'PING ' + str(i) + " " + str(int(time.time()))
    clientSocket.sendto(message, remoteAddr)

    try:
        data, server = clientSocket.recvfrom(12000)
        recdTime = time.time() * 1000
        rtt = int(recdTime - sendTime)		
        print data, "RTT:", rtt , "ms"
        a_rtt.append(rtt)
        s=s+1
    except timeout:
        print data, "RTT: *"
        f=f+1

# Validate RTT Array Length
if len(a_rtt)>0:
    Max_RTT = max(a_rtt)
    Min_RTT = min(a_rtt)
    Avg_RTT = sum(a_rtt)/len(a_rtt) 

# Finally Print Statistics
print "---- PING Statistics ----"
print i+1, " packets transmitted, ", s, " packets received, ", (f*100)/(i+1), "% packets loss"
print "round-trip (ms) min/avg/max = ", Min_RTT , "/", Avg_RTT, "/", Max_RTT 
