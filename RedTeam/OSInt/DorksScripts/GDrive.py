###################################################################################################
#
# Search for GDrive content
# Author: Rocco <Sheliak> Sicilia
# Usage: $ GDrive.py {_keyword_} {_num_}
# Usage sample: $ GDrive.py foo 5
#
###################################################################################################

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

keyword = sys.argv[1]
num = sys.argv[2]

url = "https://www.google.com/search?q=site%3Adrive.google.com+inurl%3Afile+{0}&num={1}".format(keyword, num)

headers = CaseInsensitiveDict()
headers["Connection"] = "keep-alive"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
headers["Upgrade-Insecure-Requests"] = "1"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Language"] = "en-US,en;q=0.5"
headers["Accept-Encoding"] = "gzip, deflate"

resp = requests.get(url, headers=headers)
raw_output = resp.text
raw_output = raw_output.split('<div class="tF2Cxc"><div class="yuRUbf">')

i = 1
while i < int(num):
    result = raw_output[i].split(' ')
    link = str(result[1]).replace('href="', '').replace('"', '')
    print(link)
    i = i+1
