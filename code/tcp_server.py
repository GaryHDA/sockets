#! /usr/bin/python3

import socket

TCP_IP = ["192.168.1.87"]
TCP_PORT = 22
BUFFER_SIZE = 100
def bob(x,TCP_PORT):
    print(x)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(type(s))
    s.bind((x, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection address: ', addr )
    while 1:
        data=conn.recv(BUFFER_SIZE)
        if data:
            print("Received data: ", data)
            conn.send(data)  #echo
        else:
            break
    conn.close