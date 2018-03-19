#This is a simple website blocker written in Python which blocks websites for a specific time(From 8 am to 4 pm in this script) by editing the hosts file.
#This is only meant for windows users

import time
from datetime import datetime as dt

hosts_path="/etc/hosts"														#Change the path of the hosts file according to your host file location
redirect="127.0.0.1"														#This is the local ip address of the user which is used for re-routing the user through this so that nothing will open
website_list=["www.facebook.com","facebook.com","gmail.com","www.gmail.com"]#Enter names of the websites needed to be blocked in the same format as in this list

while True:																				#Change the values of 8 and 16 accordingly as 8 is the starting time and 16 is the ending time
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):	
        print("Blocker Active")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
     else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
