# Name: Raja Harsha Chinta
# UIN : 01043488
# Class: (CS 455 or CS 555), Spring 2014
# Program 1: HTTPServer.py

import sys
import socket
from os.path import basename

port = ''  
host_name = 'atria.cs.odu.edu' #default host_name

# check the number of arguments passed.          
if len(sys.argv) == 2:
    if int(sys.argv[1]) in range(10000,11001):
        port = int(sys.argv[1])
    else: 
        print 'ERROR - Arg 1 Port number is not in between 10000 and 11000' 
        sys.exit(0)
else: 
    print 'ERROR - Arg 1 Number of arguments'
    sys.exit(0)

# Print Server Listening Details.
print 'Server is started'
print '-'*30
print 'HostName :' + host_name
print 'PortNumber :' + str(port)
print '-'*30

try:
    try:
        # socket is created and assigned
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        skt.bind((host_name, port))
        # listening started on given Host and Port name.
        skt.listen(1) 
        
        while (1):
            conn, addr = skt.accept()
            Client_Command = conn.recv(1024)
            print Client_Command
            Client_Command_List = Client_Command.split(' ', 2)
            # printing command from client
            print basename(Client_Command_List[1]) 
            file_name = './'+basename(Client_Command_List[1])
            print socket.gethostbyname(socket.gethostname())+':'+str(port) + ':' + Client_Command_List[0]
            # GET request from Client.
            if (Client_Command_List[0] == 'GET'): 
                try:
                    GET_File = 'index.html'
                    with open(GET_File, 'rb') as file_to_send:
                        # Send Request Successful Code to Client.
                        conn.send('HTTP/1.0 200 OK\r\n\r\n') 
                        for data in file_to_send:
                            conn.send(data)
                except Exception as error:
                    # Send Error Code to Client.
                    conn.send('HTTP/1.0 404 Not Found\r\n\r\n') 
                    print GET_File + ' Requested file not found'                
            # PUT request from Client.
            elif (Client_Command_List[0] == 'PUT'): 

                try:                 
                    conn.send('HTTP/1.0 200 OK\r\n\r\n')
                    # Create File to write PUT file.
                    with open(file_name, 'wb') as file_to_write: 
                        data = conn.recv(1024)
                        while True:
                            if not data:
                                break
                            file_to_write.write(data)
                            file_to_write.close()
                            print ('File Created on Server')
                            break
                except Exception as error:
                    # Exception and Error message code sent to client.
                    conn.send('HTTP/1.0 606 FAILED File NOT Created\r\n\r\n')
                    print 'ERROR - Unable to create client from file'
            else:
                print 'ERROR - Invalid Client Request'
    
            conn.close()
        s.close()
    except socket.error,(value,message):
        message = ''
        if s: 
            s.close() 
        print "Could not open socket: "+message 
        sys.exit(1)
except KeyboardInterrupt:
    sys.exit()
