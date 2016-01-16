#!/usr/bin/env python
#this is the udp broadcast lazy server
import socket, traceback
from time import sleep
from scan import scan_interface,echo
this_port = 2345
buffer_size = 4096

echo( "Server starting" )
ints = scan_interface()
reply = ' '.join([i[1] for i in ints])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

data = "Data from pc"
s.bind(("",this_port))
while True:
    try:
        data,address=s.recvfrom(buffer_size)
        echo ("server get request fromm", address, ":", data)
        s.sendto(reply, address)
        echo ("request handled")
    except (KeyboardInterrupt, SystemExit):
        s.close()
        echo ("server stopping")
        break
    except:
        traceback.print_exc()
    
    
print ("finish")
