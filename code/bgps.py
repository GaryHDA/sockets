#! /usr/bin/python3

"""
This will return basic info ('banner grabber')from each port number given in a list of 7 common ports, if open, on the server device. It is run from the client device. An excercise...

"""

import socket

Ports = [21,22,25,80,1180,1719,3306]

for i in range (0,6):

  s = socket.socket()
  
  Ports = Port[i]
  
  print ('This Is the Banner for the Port')
  
  print (Ports)
  
  s.connect (("192.168.1.91", Port))
  
  answer = s.recv (1024)
  
  print (answer)
  
  s.close () 