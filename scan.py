#!/usr/bin/env python

import re
from sys import version_info
#from commands import getstatusoutput
from pprint import pprint
from sys import stdout
from os import linesep

ver = version_info[0]
getstatusoutput=None
if ver ==2 :
    getstatusoutput = __import__("commands").getstatusoutput
else:
    getstatusoutput = __import__("subprocess").getoutput

def echo(*args):
    stdout.write(' '.join([ str(a) for a in args])+linesep)

def scan_interface():
    cmd_ret = getstatusoutput("ifconfig")
    rets = re.findall("""(\w+):\s+flags(?:.(?!\n\w+: ))+inet\s+([0-9\.]+)(?:.(?!\n\w+: ))+broadcast\s+([0-9\.]+)""",str(cmd_ret),re.DOTALL|re.MULTILINE)
    if len(rets)==0:
        echo( "No valid interface found, exit" )
        exit()
    echo( "interface(s) found" )
    return rets
