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
p = y.getvalue("port")


out = subprocess.getoutput("sudo chmod g=rw /inv.txt")
out = subprocess.getoutput("echo \"{} ansible_ssh_user={} ansible_ssh_pass={}\"  > /inv.txt".format(ip,user,passwd))
out = subprocess.getoutput("sudo touch hdfs-site.xml")
out = subprocess.getoutput("sudo touch core-site.xml")
out = subprocess.getoutput("sudo chmod g=rw hdfs-site.xml")
out = subprocess.getoutput("sudo chmod g=rw core-site.xml")
out = subprocess.getoutput("sudo echo -e \"<configuration>\\n<property>\\n<name>dfs.name.dir</name>\\n<value>/nn</value>\\n</property>\\n</configuration> \" > hdfs-site.xml")
out = subprocess.getoutput("sudo echo -e \"<configuration>\\n<property>\\n<name>fs.default.name</name>\\n<value>hdfs://{}:{}</value>\\n</property>\\n</configuration> \" > core-site.xml".format(ip,p))
out = subprocess.getoutput("ansible-playbook hadoop_namenode.yml")
out = subprocess.getoutput("sudo rm -rf /inv.txt")
out = subprocess.getoutput("sudo rm -rf hdfs-site.xml")
out = subprocess.getoutput("sudo rm -rf core-site.xml")
out = subprocess.getoutput("sudo touch /inv.txt")
p="Name node configured"
print(p)

