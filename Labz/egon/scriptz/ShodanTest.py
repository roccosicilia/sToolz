###################################################################################################
#
# Get data from Shodan.io - test script for TwitchTV
# Author: Rocco <Sheliak> Sicilia
# Usage: $ 
#
###################################################################################################

import sys
import json
import requests
import time
import config as cfg

# vars
shodan_auth = cfg.shodan["auth"]
host = sys.argv[1]

report = requests.get("https://api.shodan.io/shodan/host/{}?key={}".format(host, shodan_auth))
# print(report.text)
report_json = json.loads(report.text)
# print(report_json['tags'])

data = report_json['data']

for i in data:
    try:
        # print("Host: {} \t CPE: {}".format(i["ip"], i["cpe"]))
        print("Vulns list for CPE {}".format(i["cpe"]))
        try:
            vulns = i["vulns"]
            for vuln in vulns:
                detailts = vulns[vuln]
                print("{} \tcvss: {} \tVerified: {}".format(vuln, detailts["cvss"], detailts["verified"]))
        except:
            print("No vulns found")
    except:
        print("CPE not available")
