import os
import socket
"""
this is the server docstring
"""
def serverfunction(host, port, listen):
  s = socket.socket()
  s.bind((host, port))
  s.listen(listen)
  while True:
    c, addr = s.accept()
    print('Got connection from',addr)
    print(type(c))
    print(c)
    c.send('Thank you for connecting')
    c.close()
