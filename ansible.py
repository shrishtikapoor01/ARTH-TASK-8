#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi
y = cgi.FieldStorage()
ip=y.getvalue("ip")
user = y.getvalue("user")
passwd = y.getvalue("passwd")
uc = y.getvalue("uc")

out = subprocess.getoutput("sudo chmod g=rw /inv.txt")
out = subprocess.getoutput("echo \"{} ansible_ssh_user={} ansible_ssh_pass={}\"  > /inv.txt".format(ip,user,passwd))

if uc == 'yum':
	out = subprocess.getoutput("ansible-playbook yum_config.yml")
	p = "YUM IS CONFIGURED !!!!"
elif uc == 'httpd':
	out = subprocess.getoutput("ansible-playbook httpd.yml")
	p = "HTTPD IS CONFIGURED !!!!"

out = subprocess.getoutput("sudo rm -rf /inv.txt")
out = subprocess.getoutput("sudo touch /inv.txt")

print(p)
