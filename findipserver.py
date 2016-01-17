#!/usr/bin/env python
# this is the udp broadcast client
import socket, traceback
from time import sleep
from pprint import pprint
from scan import scan_interface,echo

host = '' # Bind to all interfaces
this_port = 5441 # Can be any
server_port = 2345
buffer_size = 4096

ints = scan_interface()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, this_port))
while True:
    try:
        for (ifname,ip,broadcast) in ints:
            echo ("sending to:",broadcast,server_port)
            s.sendto(bytes("hello?"),(broadcast, server_port)) 
        echo("Waiting for reply")  
        message, address = s.recvfrom(buffer_size)
        echo("Got reply from server:\n\t", address,":",message )
        break
    except (KeyboardInterrupt, SystemExit):
        echo ("exiting ..")
        break
    except:
        traceback.print_exc()
        echo ("exception happened")
    sleep(0.5)

s.close()
echo("finished!")


