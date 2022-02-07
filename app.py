# https://youtu.be/EsO2H0S3uFk

import shutil
import time
import datetime


def time_in_range(start, end, current):
    return start <= current <= end


# Free time = 17:00H - 7:00H
start = datetime.time(17, 0, 0)
end = datetime.time(7, 0, 0)
current = datetime.datetime.now().time()
# BE CAREFUL! BACK UP YOUR HOSTS FILE FIRST.
hosts = "/etc/hosts"
# Pi-hole redirect
redirect = "127.0.0.1"
# Subdomain is required, else the website will not be blocked should the user perform a GET to that destination.
websites = ['www.facebook.com', 'facebook.com']

# Here we modify the hosts file which precedes a DNS lookup, so that blocked websites will be written within the correct window of time.
while True:
    if end < current:
        print("Get to work!")
        with open(hosts, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website+"\n")
    else:
        with open('/etc/hosts') as old_hosts, open('/home/hosts', 'w') as new_hosts:
            for line in old_hosts:
                if not any(website in line for website in websites):
                    new_hosts.write(line)
        shutil.move('/home/hosts', '/etc/hosts')
        print("Free time.")
        time.sleep(120)
