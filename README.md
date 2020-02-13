# sockets
The communication part of the Owl Box Project, here we establish the prototypes' network communication sockets with 
Python 3.5 and 3.6.



two RPi 3 model B running Raspian
one picamera
and one laptop running "Ubuntu 18.10"

Identical environments were set up on each device using Pipenv v2018.11.26
From within the virtual environment, all subsequent work is done, on every device, from just the laptop via ssh.
The devices hostnames and fallback static ip addresses were written to the DHCPD.conf files.
The RPi3Bs were selected considering:

Economy- at 32$ each, plus 25$ for camera component, and another 20$ for the pair of microSD cards.

Utility- built-in wifi, bluetooth, 4 usb ports, 24 GPIO pins, ethernet port.

