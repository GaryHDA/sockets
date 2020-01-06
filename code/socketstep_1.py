#! /usr/bin/python3

# A script for creating socket objects.

import socket

# We provide two parameters, and set their values to the default settings.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use some methods to open a connection, send data,receive data and then close connection.

# Connect to an IP with Port, could be a URL
sock.connect(('192.168.1.87', 22))

# Send some data, this method can be called multiple times
sock.send("Twenty-five bytes to send")

# Receive up to 4096 bytes from a peer
sock.recv(4096)

# Close the socket connection, no more data transmission
sock.close()
