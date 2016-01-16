#!/usr/bin/env python2

import re
from commands import getstatusoutput
from pprint import pprint

def scan_interface():
    cmd_ret = getstatusoutput("ifconfig")
    rets = re.findall("""(\w+):\s+flags(?:.(?!\n\w+: ))+inet\s+([0-9\.]+)(?:.(?!\n\w+: ))+broadcast\s+([0-9\.]+)""",str(cmd_ret),re.DOTALL|re.MULTILINE)
    if len(rets)==0:
        print "No valid interface found, exit"
        exit()
    print "interface(s) found"
    return rets
