#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi
y = cgi.FieldStorage()
n = y.getvalue("name")

out = subprocess.getoutput("sudo docker rm -f {}".format(n))
out = "YOUR CONATINER HAS BEEN REMOVED !!!!"
print(out) 
