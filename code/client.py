
#! usr/bin/python3
import socket
import fcntl
import struct

"""
This is the script for asking for data from server.
"""
def clientfunction(host, port):
  s = socket.socket()
  host = host
  port = port
  s.connect((host, port))
  print(s.recv())
  s.close()
def printme(name):
  x = 'hello {}'.format(name)
  print(x)


def get_ip_address(ifname):
  s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  return socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),0x8915,struct.pack('256s', 'enp0s31f6'[:15].encode('utf-8')))[20:24])
