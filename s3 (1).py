#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi
y = cgi.FieldStorage()
nn=y.getvalue("name")
out = subprocess.getoutput("aws s3 mb s3://{} --region ap-south-1".format(nn))
out="YOUR S3 BUCKET WITH NAME: {} CREATED !!!!".format(nn)
print(out)
