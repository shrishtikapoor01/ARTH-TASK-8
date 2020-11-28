#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi
y = cgi.FieldStorage()
vi=y.getvalue("id")
out = subprocess.getoutput("aws ec2 delete-volume --volume-id {}".format(vi))
out="YOUR VOLUME WITH size= {}Gb DELEATED!!!".format(vi)
print(out)
