#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi
y = cgi.FieldStorage()
vi=y.getvalue("vid")
ii=y.getvalue("id")
out = subprocess.getoutput("aws ec2 attach-volume --instance-id {}  --volume-id {} --device /dev/sdc".format(ii,vi))
out="YOUR VOLUME WITH id={}Gb ATTACHED TO INSTANCE WITH id={}!!!".format(vi,ii)
print(out)
