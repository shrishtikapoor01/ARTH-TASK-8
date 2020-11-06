import os
import getpass

os.system("tput setaf 3")
print("          Welcome to menu program           ")
os.system("tput setaf 7")

x=getpass.getpass("Enter your password :")
if x!='a':
	exit()
print()
while True:
	os.system("clear")
	os.system("tput setaf 2")
	r=input("Want to do remote login (y/n): ")
	os.system("tput setaf 7")

	if(r=="y"):
		ip=input("Enter the remote ip:\t")
		print()
		os.system("tput setaf 6")
		print("""
	1)Start Namenode
	2)Start Datanode
	3)Stop Namenode
	4)Stop Datanode
	5)Launch Docker container
	6)Change running container name
	7)Remove container
	8)Remove docker image
	9)Create physical volume
	10)Create volume group
	11)Create logical volume
	12)Display (pv/vg/lv)
	13)Logical volume extend
	14)Logical volume reduce
	15)Create AWS key-value pair
	16)Delete AWS key-value pair
	17)Launch AWS instance
	18)Delete AWS instance
	19)Display AWS information about all AWS instance
	20)Create S3 bucket
	21)Create EBS Volume
	22)Delete EBS Volume
	23)Attach EBS Volume
	24)Configure apache webserver""")
		os.system("tput setaf 7")
		uc=input("enter your choice:\t")
		os.system("tput setaf 7")
		if uc == '1':
			os.system("ssh {} systemctl stop firewalld".format(ip))
			os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
		elif uc == '2':
			os.system("ssh {} systemctl stop firewalld".format(ip))
			os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
		elif uc == '3':
			os.system("ssh {} hadoop-daemon.sh stop namenode".format(ip))
		elif uc == '4':
			os.system("ssh {} hadoop-daemon.sh stop datanode".format(ip))
		elif uc == '5':
			os.system("systemctl start docker\t")
			ost=input("Which os you want to launch\t")
			v=input("which version of {} you want to launch\t".format(ost))
			qq=input("Do you have docker image of {} {} (y/n)\t".format(ost,v))
			if qq == 'n':
				os.system("ssh {} docker pull {}:{}".format(ip,ost,v))
			os.system("ssh -t {} docker run -i -t {}:{}".format(ip,ost,v))
		elif uc == '6':
			os.system("ssh {} systemctl start docker".format(ip))
			en=input("Enter current name\t")
			nn=input("Enter new name\t")
			os.system("ssh {} docker rename {} {}".format(ip,en,nn))
		elif uc == '7':
			
			os.system("ssh {} systemctl start docker".format(ip))
			os.system("ssh {} docker ps -a".format(ip))
			cid=input("Give your container id or name from above\t")
			os.system("ssh {} docker container rm -f {}".format(ip,cid))
		elif uc == '8':
			os.system("ssh {} systemctl start docker;docker images;".format(ip))
			iid=input("give the image name from above\t")
			os.system("ssh {} docker rmi -f {}".format(ip,iid))
		elif uc == '9':
			os.system("ssh {} fdisk -l".format(ip))
			d=input("Enter hard disk name from above\t")
			os.system("ssh {} pvcreate {}".format(ip,d))
		elif uc == '10':
			n=input("Give volume group name\t")
			os.system("ssh {} pvdisplay".format(ip))
			pv=input("Give your pv name\t")
			os.system("ssh {} vgcreate {} {} ".format(ip,n,pv))
		elif uc == '11':
			n=input("Enter the logical volume name\t")
			vg=input("Enter volume group name\t")
			s=input("Enter size of logical volume (ex: 1G,1M)\t")
			os.system("ssh {} lvcreate --size {} --name {} {}".format(ip,s,n,vg) )
			os.system("ssh {} mkfs.ext4 /dev/{}/{}".format(ip,vg,n))
		elif uc == '12':
			n=input("Select (pv/vg/lv)\t")
			if n == 'lv':
				vg=input("Enter name of volume group\t")
				lv=input("Enter name of logical volume\t")	
				os.system("ssh {} lvdisplay /dev/{}/{}".format(ip,vg,lv))
			else:
				nn=input("Enter name of {}\t".format(n))
				os.system("ssh {} {}display {}".format(ip,n,nn))
		elif uc == '13':
			s=input("Enter the size to be extend (ex: 1G,1M)\t")
			lv=input("Enter name of logical volume\t")
			vg=input("Enter name of volume group\t")
			os.system("ssh {} lvextend --size +{} /dev/{}/{}".format(ip,s,vg,lv))
			os.system("ssh {} resize2fs /dev/{}/{}".format(ip,vg,lv))
		elif uc == '14':
			print("You might loose your data!!!")
			s=input("Enter the size to be extend (ex: 1G,1M)\t")
			lv=input("Enter name of logical volume\t")
			vg=input("Enter name of volume group\t")
			os.system("ssh {} lvreduce --size -{} /dev/{}/{}".format(ip,s,vg,lv))
		elif uc == '15':
			nn=input("Enter name for key-value pair\t")
			os.system("aws ec2 create-key-pair --key-name {}".format(nn))
		elif uc == '16':
			nn=input("Enter name for key-value pair\t")
			os.system("aws ec2 delete-key-pair --key-name {}".format(nn))		
		elif uc == '17':
			c=input("Enter the number of instance you want to launch\t")
			kv=input("Enter the name of key-value pair\t")
			os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb   --key-name {} --instance-type t2.micro --count {}  --subnet-id subnet-4e757c26".format(kv,c))
		elif uc == '18':
			i=input("Enter the instance id \t")
			os.system("aws ec2  terminate-instances --instance-ids {}".format(i))
		elif uc == '19':
			os.system("aws ec2 describe-instances")			
		elif uc == '20':
			nn=input("Enter unique name for S3 bucket\t")
			os.system("aws s3 mb s3://{} --region ap-south-1".format(nn))
		elif uc == '21':
			s=input("Enter size of EBS volume\t")
			os.system("aws ec2 create-volume --availability-zone ap-south-1a   --size {}".format(s))
		elif uc == '22':
			vi=input("Enter volume id\t")
			os.system("aws ec2 delete-volume --volume-id {}".format(vi))				
		elif uc == '23':
			ii=input("Enter instance id\t")
			vi=input("Enter volume id\t")
			os.system("aws ec2 attach-volume --instance-id {}  --volume-id {} --device /dev/sdc".format(ii,vi))
		elif uc == '24':
			os.system("ssh {} yum install httpd".format(ip))
			os.system("ssh {} systemctl start httpd".format(ip))
			os.system("ssh {} systemctl stop firewalld".format(ip))
			
		else:
			print("wrong input!!!!!!!!")
			exit()
	else:
		print()
		os.system("tput setaf 6")
		print("""
	1)start namenode
	2)start datanode
	3)Stop Namenode
	4)Stop Datanode
	5)Launch Docker container
	6)Change running container name
	7)Remove container
	8)Remove docker image
	9)Create physical volume
	10)Create volume group
	11)Create logical volume
	12)Display (pv/vg/lv)
	13)Logical volume extend
	14)Logical volume reduce
	15)Create AWS key-value pair
	16)Delete AWS key-value pair
	17)Launch AWS instance
	18)Delete AWS instance
	19)Display AWS information about all AWS instance
	20)Create S3 bucket
	21)Create EBS Volume
	22)Delete EBS Volume
	23)Attach EBS Volume
	24)Configure apache webserver""")
		os.system("tput setaf 7")
		uc=input("enter your choice:\t")
		os.system("tput setaf 7")
		if uc == '1':
			os.system("systemctl stop firewalld")
			os.system("hadoop-daemon.sh start namenode")
		elif uc == '2':
			os.system("systemctl stop firewalld")
			os.system("hadoop-daemon.sh start datanode")
		elif uc == '3':
			os.system("hadoop-daemon.sh stop namenode")
		elif uc == '4':
			os.system("hadoop-daemon.sh stop datanode")
		elif uc == '5':
			os.system("systemctl start docker\t")
			ost=input("Which os you want to launch\t")
			v=input("which version of {} you want to launch\t".format(ost))
			qq=input("Do you have docker image of {} {} (y/n)\t".format(ost,v))
			if qq == 'n':
				os.system("docker pull {}:{}".format(ost,v))
			os.system("docker run -i -t {}:{}".format(ost,v))
		elif uc == '6':
			os.system("systemctl start docker")
			en=input("Enter current name\t")
			nn=input("Enter new name\t")
			os.system("docker rename {} {}".format(en,nn))
		elif uc == '7':
			os.system("systemctl start docker")
			os.system("docker ps -a")
			cid=input("Give your container id or name from above\t")
			os.system("docker container rm -f {}".format(cid))
			os.system("docker rm -f {}".format(cid))
		elif uc == '8':
			os.system("systemctl start docker;docker images;")
			iid=input("give the image name from above\t")
			os.system("docker rmi -f {}".format(iid))
		elif uc == '9':
			os.system("fdisk -l")
			d=input("Enter hard disk name from above")
			os.system("pvcreate {}".format(d))
		elif uc == '10':
			n=input("Give volume group\t")
			os.system("pvdisplay")
			pv=input("Give your pv name\t")
			os.system("vgcreate {} {} ".format(n,pv))
		elif uc == '11':
			n=input("Enter the logical volume name\t")
			vg=input("Enter volume group name\t")
			s=input("Enter size of logical volume (ex: 1G,1M)\t")
			os.system("lvcreate --size {} --name {} {}".format(s,n,vg) )
			os.system("mkfs.ext4 /dev/{}/{}".format(vg,n))
		elif uc == '12':
			n=input("Select (pv/vg/lv)\t")
			if n == 'lv':
				vg=input("Enter name of volume group\t")
				lv=input("Enter name of logical volume\t")	
				os.system("lvdisplay /dev/{}/{}".format(vg,lv))
			else:
				nn=input("Enter name of {}\t".format(n))
				os.system("{}display {}".format(n,nn))
		elif uc == '13':
			s=input("Enter the size to be extend (ex: 1G,1M)\t")
			lv=input("Enter name of logical volume\t")
			vg=input("Enter name of volume group\t")
			os.system("lvextend --size +{} /dev/{}/{}".format(s,vg,lv))
			os.system("resize2fs /dev/{}/{}".format(vg,lv))
		elif uc == '14':
			print("You might loose your data!!!")
			s=input("Enter the size to be extend (ex: 1G,1M)\t")
			lv=input("Enter name of logical volume\t")
			vg=input("Enter name of volume group\t")
			os.system("lvextend --size -{} /dev/{}/{}".format(s,vg,lv))
		elif uc == '15':
			nn=input("Enter name for key-value pair\t")
			os.system("aws ec2 create-key-pair --key-name {}".format(nn))
		elif uc == '16':
			nn=input("Enter name for key-value pair\t")
			os.system("aws ec2 delete-key-pair --key-name {}".format(nn))		
		elif uc == '17':
			c=input("Enter the number of instance you want to launch\t")
			kv=input("Enter the name of key-value pair\t")
			os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb   --key-name {} --instance-type t2.micro --count {}  --subnet-id subnet-4e757c26".format(kv,c))
		elif uc == '18':
			i=input("Enter the instance id \t")
			os.system("aws ec2  terminate-instances --instance-ids {}".format(i))
		elif uc == '19':
			os.system("aws ec2 describe-instances")			
		elif uc == '20':
			nn=input("Enter unique name for S3 bucket\t")
			os.system("aws s3 mb s3://{} --region ap-south-1".format(nn))
		elif uc == '21':
			s=input("Enter size of EBS volume\t")
			os.system("aws ec2 create-volume --availability-zone ap-south-1a   --size {}".format(s))
		elif uc == '22':
			vi=input("Enter volume id\t")
			os.system("aws ec2 delete-volume --volume-id {}".format(vi))				
		elif uc == '23':
			ii=input("Enter instance id\t")
			vi=input("Enter volume id\t")
			os.system("aws ec2 attach-volume --instance-id {}  --volume-id {} --device /dev/sdc".format(ii,vi))
		elif uc == '24':
			os.system("yum install httpd")
			os.system("systemctl start httpd")
			os.system("systemctl stop firewalld")			
		else:
			print("wrong input!!!!!!!!")
			exit()


	input("Press enter to continue.....")


