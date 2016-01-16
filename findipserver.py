#!/usr/bin/env python2
# this is the udp broadcast client
import socket, traceback
from time import sleep
from pprint import pprint
from scan import scan_interface

host = '' # Bind to all interfaces
this_port = 5441 # Can be any
server_port = 2345
buffer_size = 4096

ints = scan_interface()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, this_port))
print "all interfaces:"
pprint(ints)
while True:
    try:
        for (ifname,ip,broadcast) in ints:
            print "sending to:",broadcast,server_port
            s.sendto("hello?",(broadcast, server_port))   
        message, address = s.recvfrom(buffer_size)
        print "Got reply from server:\n\t", address,":",message 
        break
    except (KeyboardInterrupt, SystemExit):
        print "exiting .."
        break
    except:
        traceback.print_exc()
        print "exception happened"
    sleep(0.5)
    
s.close()


