#! usr/bin/python3

import socket

def clientfunction(host, port):
  """
  This is the script for asking for data from server.
  """
  s = socket.socket()
  s.connect((host, port))
  print(s.recv(4096))
  s.close()
  
 