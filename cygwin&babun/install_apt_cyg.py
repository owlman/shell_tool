#! /usr/bin/env python
'''
    Created on 2016-4-29
    
    @author: lingjie
    @name:   install_apt_cyg
'''

import os
import sys

title = "= Starting " + sys.argv[0] + "... ="
n = len(title)
print n*'='
print title
print n*'='

cmds = [
		"lynx -source rawgit.com/transcode-open/apt-cyg/master/apt-cyg > apt-cyg",
	    "install apt-cyg /bin"
]

for cmd in cmds:
	print cmd
	os.system(cmd)

print n*'='    
print "= Done!" + (n-len("= Done!")-1)*' ' + "="
print n*'='
