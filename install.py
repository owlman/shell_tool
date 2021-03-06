#! /usr/bin/env python
"""
    Created on 2016-5-31

    @author: lingjie
    @name:   install
"""

import os
import sys
import shutil
import platform

if not len(sys.argv) in range(2,3):
    print("Usage: install.py <install_dir>")
    exit(0)

title = "=    Starting " + sys.argv[0] + "......    ="
n = len(title)
print(n*'=')
print(title)
print(n*'=')

my_dir = sys.path[0]
files = os.popen("find " + my_dir + " -name '*.py'").readlines()
template_file = os.popen("find " + my_dir + " -name '*.zip'").readlines()

os.chdir(sys.argv[1])
print("PWD: " + os.popen("pwd").readline())
if not os.path.exists("tmp"):
    os.mkdir("tmp")

if not os.path.exists("template"):
    os.mkdir("template")
    for file in template_file :
        filename = os.path.split(os.path.realpath(file[0:-1]))[1]
        print("copying..." + filename)
        shutil.copy(file[0:-1],"template/"+filename)

for file in files:
    filepath = os.path.split(os.path.realpath(file[0:-1]))[0]
    dirname = filepath.split("/")[-1]
    filename = os.path.split(os.path.realpath(file[0:-1]))[1]
    if (filename == "install.py" or filename == "uninstall.py"):
       continue
    if (platform.platform() != "darwin" and dirname == "macos_tools"):
       continue
    if (platform.platform() != "Windows" and dirname == "win_tools"):
       continue

    print("copying..." + filename)
    shutil.copy(file[0:-1],filename)
    os.system("chmod +x " + filename)

print(n*'=')    
print("=     Done!" + (n-len("=     Done!")-1)*' ' + "=")
print(n*'=')
