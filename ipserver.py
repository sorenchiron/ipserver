#!/usr/bin/env python2
#this is the udp broadcast lazy server
import socket, traceback
from time import sleep
from scan import scan_interface
this_port = 2345
buffer_size = 4096

print "Server starting"
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
        print "server get request fromm", address, ":", data
        s.sendto(reply, address)
        print "request handled"
    except (KeyboardInterrupt, SystemExit):
        s.close()
        print "server stopping"
        break
    except:
        traceback.print_exc()
    
    
print "finish"
