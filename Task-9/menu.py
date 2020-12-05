import os
import getpass
import pip
import pyttsx3
import speech_recognition as sr


pyttsx3.speak("Hello ,welcome to Voice controled menu application")
pyttsx3.speak("I am your virtual assistant, BOT ALPHA")
pyttsx3.speak("The technologies, in which I can assist you are,")
pyttsx3.speak("Ha doop ")
pyttsx3.speak("Docker")
pyttsx3.speak("Amazon Web Services A W S ")
pyttsx3.speak("Logical volume managment ")
pyttsx3.speak("Configuring yum in newly installed instance")
pyttsx3.speak("You just simply need to speak out your task")

while True:		
		print("""		1)Configure Namenode
		2)Configure Datanode
		3)Launch Docker container
		4)Remove container
		5)Remove docker image
		6)Create logical volume
		7)Display logical volume information
		8)Extend logical volume 
		9)Launch Amazon cloud instance
		10)Delete AWS instance
		11)Create S3 bucket
		12)Create elsatic block storage
		13)Delete elsatic block storage
		14)Attach elsatic block storage
		15)Configure yum""")
		pyttsx3.speak("You are requested to enter the ip of the instance in which you want to run the command")	
		ip=input("Enter the ip:\t")
		print()
		print("\n\n \"option 1 configure the name node\"")
		pyttsx3.speak("Speak request in the same way as it's displayed on screen and speak when you see say your choice")
		r=sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source,duration=7)	
			print("\n\nsay your choise")
			audio=r.listen(source)
			print("\n we got it....\n")
		pyttsx3.speak("please wait for a while we are processing your request")
		p=r.recognize_google(audio)
		print(p)
		if((('namenode' in p) or ('name node' in p)) and ('configure' in p)):
			pyttsx3.speak("Enter the port number")
			p=input("port:\t")
			os.system("ssh root@{} ansible-playbook /var/www/cgi-bin/hadoop_namenode.yml".format(ip))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Ha doop name node is configured")
			pyttsx3.speak("noe you just need to format hadoop Ha doop name node and start the service ")
			
		elif ((('datanode' in p) or ('data node' in p)) and ('configure' in p)):
			pyttsx3.speak("Enter the ip address of name node")
			nip=input("Name node ip:\t")
			pyttsx3.speak("Enter the port number")
			p=input("port:\t")
			os.system("ssh root@{} ansible-playbook /var/www/cgi-bin/hadoop_datanode.yml".format(ip))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Ha doop data node is configured")
			pyttsx3.speak("nw you just need to start Ha doop data node service ")
		elif(('launch' in p) and ('docker' in p) and ('container' in p)):
			os.system("ssh root@{} systemctl start docker\t".format(ip))
			pyttsx3.speak("Docker service started")
			pyttsx3.speak("Which operating system you want to launch")
			ost=input("OS:\t")
			pyttsx3.speak("Do you have docker image of operating system you selected in your instance")
			qq=input("(y/n):\t")
			if qq == 'n':
				os.system("ssh root@{} docker pull {}".format(ip,ost))
			os.system("ssh -t root@{} docker run -i -t {}".format(ip,ost))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your docker container has been launched")
		elif(('remove' in p) and ('docker' in p) and ('container' in p)):
			os.system("ssh root@{} docker ps -a".format(ip))
			pyttsx3.speak("give the name of the name or id of container which you would like to delete from above displayed list")
			cid=input("Container id or name:\t")
			os.system("ssh root@{} docker container rm -f {}".format(ip,cid))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your docker container has been removed")
		elif(('remove' in p) and ('docker' in p) and ('image' in p)):
			os.system("ssh root@{} docker images".format(ip))
			pyttsx3.speak("give the name of the image which you would like to delete from above displayed list")
			iid=input("Image name\t")
			os.system("ssh root@{} docker rmi -f {}".format(ip,iid))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your docker image has been removed")
		elif(('create' in p) and ('logical' in p) and ('volume' in p)):
			pyttsx3.speak("Enter name of hard disk")
			hd=input("Hard disk name:\t")
			os.system("ssh root@{} pvcreate {}".format(ip,hd))
			pyttsx3.speak("Enter name of logical volume")
			n=input("Logical volume name:\t")
			pyttsx3.speak("Enter name of volume group")
			vg=input("Volume group name:\t")
			os.system("ssh root@{} vgcreate {} {} ".format(ip,vg,hd))
			pyttsx3.speak("Enter the size of logical volume you would like to create")
			s=input("Size(ex: 1G,1M):\t")
			os.system("ssh root@{} lvcreate --size {} --name {} {}".format(ip,s,n,vg) )
			os.system("ssh root@{} mkfs.ext4 /dev/{}/{}".format(ip,vg,n))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your Logical volume has been created")
		elif(('display' in p) and ('logical' in p) and ('volume' in p)):
			pyttsx3.speak("Enter name of volume group")
			vg=input("Volume group name:\t")
			pyttsx3.speak("Enter name of logical volume")
			lv=input("Logical volume name:\t")	
			os.system("ssh root@{} lvdisplay /dev/{}/{}".format(ip,vg,lv))
			pyttsx3.speak("hears the information about logical volume!!!!")
		elif(('extend' in p) and ('logical' in p) and ('volume' in p)):
			pyttsx3.speak("Enter the size by which you would like to extend")
			s=input("Size (ex: 1G,1M)\t")
			pyttsx3.speak("Enter name of logical volume")
			lv=input("Logical volume name\t")
			pyttsx3.speak("Enter name of volume group")
			vg=input("Volume group name\t")
			os.system("ssh root@{} lvextend --size +{} /dev/{}/{}".format(ip,s,vg,lv))
			os.system("ssh root@{} resize2fs /dev/{}/{}".format(ip,vg,lv))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your Logical volume has been extended")		
		elif(('launch' in p) and ('Amazon cloud' in p) and ('instance' in p)):
			pyttsx3.speak("Enter the number of aws instance you want to launch")
			c=input("number:\t")
			os.system(" aws ec2 run-instances --image-id ami-0e306788ff2473ccb   --key-name keyhadoop --instance-type t2.micro --count {}  --subnet-id subnet-4e757c26".format(c))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your aws instance has been launched")
		elif(('delete' in p) and ('Amazon cloud' in p) and ('instance' in p)):
			pyttsx3.speak("Enter the instance id which you want ot terminate")
			i=input("Instance id: \t")
			os.system(" aws ec2  terminate-instances --instance-ids {}".format(i))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your aws instance has been removed")
		elif(('create' in p) and ('S3' in p) and ('bucket' in p)):
			pyttsx3.speak("Enter the unique name for you aws s3 bucket")
			nn=input("Name:\t")
			os.system( "aws s3 mb s3://{} --region ap-south-1".format(nn))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your aws S3 bucket has been launched")
		elif(('create' in p) and ('elastic' in p) and ('storage' in p)):
			pyttsx3.speak("Enter the size of EBS volume which you want to create")
			s=input("Size:\t")
			os.system(" aws ec2 create-volume --availability-zone ap-south-1a   --size {}".format(s))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your elsatic block storage has been launched")
		elif(('delete' in p) and ('elastic' in p) and ('storage' in p)):
			pyttsx3.speak("Enter the volume id which you want to delete")
			vi=input("Volume id\t")
			os.system(" aws ec2 delete-volume --volume-id {}".format(vi))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your elsatic block storage has been removed")				
		elif(('attach' in p) and ('elastic' in p) and ('storage' in p)):
			pyttsx3.speak("Enter the aws instance id to which you want ot attach volume")
			ii=input("Instance id:\t")
			pyttsx3.speak("Enter the volume id which you wnat to attach")
			vi=input("Volume id:\t")
			os.system(" aws ec2 attach-volume --instance-id {}  --volume-id {} --device /dev/sdc".format(ii,vi))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("Your elsatic block storage has been attached")
		elif((('yum' in p) or ('Yum' in p)) and ('configure' in p)):
			os.system("ssh root@{} ansible-playbook /var/www/cgi-bin/yum_config.yml".format(ip))
			pyttsx3.speak("SUCCESS!!!!!!")
			pyttsx3.speak("we have configured yum in your instance")
			pyttsx3.speak("now your instance is ready to install softwares")
			
		else: 
			continue
