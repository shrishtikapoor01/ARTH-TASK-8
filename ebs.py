#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi
y = cgi.FieldStorage()
s=y.getvalue("size")
out = subprocess.getoutput("aws ec2 create-volume --availability-zone ap-south-1a   --size {}".format(s))
out="YOUR INSTANCE WITH size= {}Gb CREATED!!!".format(s)
print(out)
