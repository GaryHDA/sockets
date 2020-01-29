import os
import socket

"""
jan20,2020-this is the server script which is located on, and runs from, the pi(bobo).it was created/modified on jan13.

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
    c.send(b'Thank you for connecting')
    c.close()
