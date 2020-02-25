import os
import socket
import takeapicture

"""
jan20,2020-this is the server script which is located on, and runs from, the pi(bobo).it was created/modified on jan13.

"""
def serverfunction(host, port, listen, name):
  s = socket.socket()
  s.bind((host, port))
  s.listen(listen)
  while True:
    c, addr = s.accept()
    print('Got connection from',addr)
    print(type(c))
    print(c)
    takeapicture.takeapicture(name)
    c.send(b'Welcome back again!')
    c.close()
