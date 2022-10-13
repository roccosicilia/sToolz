###################################################################################################
#
# Get data link from a website
# Author: Rocco <Sheliak> Sicilia
# Usage: $ 
#
###################################################################################################

import sys
import json
import requests
import readline

# vars
target = sys.argv[1]

content = requests.get(target)
content_html = content.text
#print(content_html)

lines = readline(content_html)
for line in lines:
    if 'href' in line:
        print(line)
