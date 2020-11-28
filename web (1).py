#!/usr/bin/python3
print("content-type: text/html")
print()


import subprocess
out=subprocess.getoutput("sudo yum install httpd  -y")
out=subprocess.getoutput("sudo systemctl stop firewalld")
out=subprocess.getoutput("sudo systemctl start httpd")
out="YOUR WEB SERVER HAS STARTED!!!!!"
print(out)
