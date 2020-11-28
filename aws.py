#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess

out = subprocess.getoutput("aws ec2 run-instances --image-id ami-0e306788ff2473ccb   --key-name keyhadoop --instance-type t2.micro --count 1  --subnet-id subnet-4e757c26")
print("AWS INSTANCE LAUNCHED")

