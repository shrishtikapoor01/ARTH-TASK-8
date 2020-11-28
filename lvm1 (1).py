#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi

y=cgi.FieldStorage()
vg=y.getvalue("vg")
lv=y.getvalue("lv")
s=y.getvalue("size")
uc=y.getvalue("uc")
	
if uc == '1':
	out= subprocess.getoutput("sudo lvextend --size +{} /dev/{}/{}".format(s,vg,lv))
	out=subprocess.getoutput("sudo resize2fs /dev/{}/{}".format(vg,lv))
	p="LVM SIZE SUCCESSFULLY EXTENDED !!!!!\n "
	print(p)
else:
	out=subprocess.getoutput("sudo e2fsck -f /dev/{}/{}".format(vg,lv))
	out=subprocess.getoutput("sudo lvreduce -f --size -{} /dev/{}/{}".format(s,vg,lv))
	p="LVM SIZE SUCCESSFULLY REDUCED !!!!!\n "
	print(p)
