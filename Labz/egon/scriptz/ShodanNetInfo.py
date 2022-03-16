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
domain = sys.argv[1]

# head
print("#"*75 + "\n# vRecon for {}".format(str(domain)))

# get host/ip from A, MX, TXT record
def GetDnsInfo(domain, type):
    # get data from google DNS
    print("# Get DNS info...")
    request = requests.get("https://dns.google/resolve?name={}&type={}".format(domain, type))
    request_json = json.loads(request.text)
    answers = request_json["Answer"]
    # read data and define MX and SPF lists
    data = []
    for answer in answers:
        if type == 'MX':
            mxdata = answer["data"].split()
            res = mxdata[1]
            data.append(res[:-1])
            print("# MX record found: {}".format(res[:-1]))
        elif type == 'TXT':
            txtdata = answer["data"].split(', ')
            for txtrecord in txtdata:
                if 'spf' in txtrecord:
                    spfelements = txtrecord.split()
                    for spfelement in spfelements:
                        if 'ip4' in spfelement or 'include' in spfelement:
                            spf = spfelement.split(':')
                            data.append(spf[1])
                            print("# SPF host found: {}".format(spf[1]))
        else:
            print("Error: Domain or Type is invalid.")
    return data 

# get data from Shodan
for host in GetDnsInfo(domain, 'MX'):
    report = requests.get("https://api.shodan.io/shodan/host/{}?key={}".format(host, shodan_auth))
    report_json = json.loads(report.text)
    try:
        report_data = report_json['data']

        for i in report_data:
            try:
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
    except:
        print("Shodan data not available")