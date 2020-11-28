#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi
y = cgi.FieldStorage()
i=y.getvalue("id")
out = subprocess.getoutput("aws ec2  terminate-instances --instance-ids {}".format(i))
out="YOUR INSTANCE WITH ID: {} DELETED!!!!".format(i)
print(out)

