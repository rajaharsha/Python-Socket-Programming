Programming Assignment #3
=========================

Author: Raja Harsha Chinta
   UIN: 01043488
 Email: rchin001@odu.edu

This package implements Programming Assignment #3

SETUP
=====

 1. Install the Python 2.7.12 or Anaconda 4.1.1 (64-bit)

 2. Transfer the files named below into Python installed directory:

	a) HTTPClient.py
	b) HTTPServer.py
	c) Readme.txt

 3. Please Place HTTPServer.py file on a separate folder away from HTTPClient.py to help during PUT Validation.

EXECUTION PROCEDURE
===================

 1. Migrate the 2 Python script files.
 2. Firstly, execute the script HTTPServer.py using the below syntax.

    "python HTTPServer.py <server port no>"

For example:

    "python HTTPServer.py 10005"

 3. Secondly, Execute the script HTTPClient.py using below syntax.

    GET request:
    "python HTTPClient.py http://www.google.com"
	
    PUT request:
    "python HTTPClient.py PUT http://atria.cs.odu.edu:10005 Test.html"

 4. Observe the print statements for each script execution.
 5. Exit the python console.