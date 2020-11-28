#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi

y=cgi.FieldStorage()
d=y.getvalue("hd")
pv=y.getvalue("pv")
vg=y.getvalue("vg")
lv=y.getvalue("lv")
s=y.getvalue("size")


out = subprocess.getoutput("sudo pvcreate {}".format(d))
out = subprocess.getoutput("sudo vgcreate {} {} ".format(vg,d))
out = subprocess.getoutput("sudo lvcreate --size {} --name {} {}".format(s,lv,vg))
out = subprocess.getoutput("sudo mkfs.ext4 /dev/{}/{}".format(vg,lv))
out = subprocess.getoutput("sudo lvdisplay /dev/{}/{}".format(vg,lv))
p="LVM SUCCESSFULLY CREATED !!!!!\n "
print(p)
print("\n\n")
print(out)

