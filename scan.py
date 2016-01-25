#!/usr/bin/env python

import re
from sys import version_info
#from commands import getstatusoutput
from pprint import pprint
from sys import stdout
from os import linesep
from platform import system as getsystem
ver = version_info[0]
getstatusoutput=None
plat=getsystem() # Windows or not
if ver ==2 :
    getstatusoutput = __import__("commands").getstatusoutput
else:
    getstatusoutput = __import__("subprocess").getoutput

def echo(*args):
    stdout.write(' '.join([ str(a) for a in args])+linesep)

def scan_interface():
    def get_interfaces(plat):
        cmd_ret=None
        rets=None
        pprint(plat+" detected")
        if plat=="Windows":
            cmd_ret = getstatusoutput("ipconfig")
            rets = re.findall(":\s(\d+\.\d+\.\d+\.\d+)",cmd_ret,re.MULTILINE)
            rets = [ ("unknown",i,".".join(i.split(".")[0:3]+["255"]) ) for i in rets if "255" not in i ]
        else:        
            cmd_ret = getstatusoutput("ifconfig")
            rets = re.findall("""(\w+):\s+flags(?:.(?!\n\w+: ))+inet\s+([0-9\.]+)(?:.(?!\n\w+: ))+broadcast\s+([0-9\.]+)""",str(cmd_ret),re.DOTALL|re.MULTILINE)
        return rets
        # [(name,broadcast_addr),...]   
    rets = get_interfaces(plat)
    if len(rets)==0:
        echo( "No valid interface found, exit" )
        exit()
    echo( "interface(s) found" )
    return rets