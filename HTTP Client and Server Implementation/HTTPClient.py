# Name: Raja Harsha Chinta
# UIN : 01043488
# Class: (CS 455 or CS 555), Spring 2014
# Program: HTTPClient.py

import os
import sys
import socket
import webbrowser
from urlparse import urlparse

# Validating Input Server Address Values from User

def verify_adr(Server_Address):
    url =  urlparse(Server_Address)
    if (str(url.scheme) + '://' != 'http://'):
       print "ERROR - Arg 1 Server Address should start with http://"
       sys.exit(0)
    else:
        host_name = url.hostname
    # Set Default Port as 80 if NULL
    if (url.port == None):
        port = 80 
    else:
        port = url.port
    file_path = url.path
    return host_name,port,file_path

# Function to perform GET request    
def get_request(host_name,port,file_path):
    if file_path == "":
        file_path = "/"
    skt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Set Timeout as 20 seconds at Client end.
    skt.settimeout(20)
    try:
        skt.connect((host_name, port))
        skt.send('GET '+ file_path +' HTTP/1.0\r\n')
        skt.send('HOST: '+ host_name + ' \r\n')
        skt.send('User-Agent:ODU-CS455/555\r\n\r\n')
        resp_data = ''
        while True:
            data = skt.recv(1024)
            resp_data = resp_data + data
            if not data:
                break
        resp_data = resp_data.split('\r\n\r\n')
        headers = resp_data[0]
        server_html_data = ' '.join(resp_data[1:])
        print headers
        # Open and Write the Server Response into page.
        f = open('Web_Page.html','w')
        f.write(server_html_data)
        f.close()
        # Open local file on browser.
        webbrowser.open('file://' + os.path.realpath('./Web_Page.html'))
        skt.close()
        return
    except socket.error, exc:
        print "Caught exception socket.error : %s" % exc

# Function to perform PUT request    
def put_request(host_name, port, file_path):
    file_path = './'+sys.argv[3]
    
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Display Host & Request Details.
        print 'PUT '+ file_path +' HTTP/1.0'
        print 'HOST: '+ host_name
        print 'USER-AGENT:ODU-CS455/555'

        skt.connect((host_name, port))
        skt.send('PUT '+ file_path +' HTTP/1.0\r\n')
        skt.send('User-Agent:ODU-CS455/555\r\n')
        skt.send('HOST: '+ host_name + '\r\n\r\n')
        try:
            data = ''
            resp_data = ''
            with open(file_path, 'rb') as send_file:
                for data in send_file:
                    skt.sendall(data)
            data = skt.recv(1024)
            resp_data = resp_data + data
            print '-'*40
            print 'Response from Server : ' + resp_data
            print '-'*40
        except Exception as error: 
            print 'ERROR - File to PUT is not found'       
        skt.close()
        return
    except socket.error, exc:
        print 'ERROR - Received Socket Error while performing PUT'

if len(sys.argv) == 2: 
    Server_Address = sys.argv[1]
    host_name,port,file_path = verify_adr(Server_Address)
    # Call GET Function
    get_request(host_name,port,file_path)
  
elif len(sys.argv) == 4:
    if sys.argv[1] == 'PUT': 
        Server_Address = sys.argv[2]
        host_name,port,file_path = verify_adr(Server_Address)
        # Call PUT Function  
        put_request(host_name,port,file_path)
    else:
        print 'ERROR - Please use PUT command.'
else:
    print 'ERROR - Incorrect number of arguements passed'
