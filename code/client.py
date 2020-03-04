
#! usr/bin/python3

import socket
"""
This is the script for asking for data from server.
"""
def clientfunction(host, port):
  s = socket.socket()
  host = host
  port = port
  s.connect((host, port))
  print(s.recv(4096))
  s.close()
