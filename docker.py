#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi
y = cgi.FieldStorage()
osn = y.getvalue("os_name")
q = y.getvalue("que")
n = y.getvalue("name")
if q == 'n':
	out = subprocess.getoutput("sudo docker pull {}".format(osn))	
out = subprocess.getoutput("sudo docker run -i -t --name {} {}".format(n,osn))
out = "YOUR CONATINER HAS BEEN LAUNCHED !!!!"
print(out) 
