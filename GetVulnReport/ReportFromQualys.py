###################################################################################################
#
# Get XML report from QUALYS
# Author: Rocco <Sheliak> Sicilia
# Usage: $ ReportFromQualys.py {_DATE_}
#
###################################################################################################

import sys
import requests
import time
import xml.etree.ElementTree as ET
import config as cfg


# vars
now = int(time.time())

qualys_baseurl =    cfg.qualys["baseurl"]
qualys_api =        cfg.qualys["api"]
qualys_auth =       cfg.qualys["auth"]

if len(sys.argv) == 2:
    # get reports list
    date = sys.argv[1]
    print("Report list for date {0}:".format(date))
    report = requests.get(qualys_baseurl + qualys_api + 'action=list', headers={'Authorization': qualys_auth, 'X-Requested-With': 'TestAPI'})
    tree_report = ET.ElementTree(ET.fromstring(report.text))
    root_report = tree_report.getroot()
 
    # print(root_report[0][1][0][0].tag)
    # print("Reports number: {}".format(len(root_report[0][1])))

    for report in root_report[0][1]:
        if(report[5].text == 'XML'):
            print("##################################################")
            print("Report ID: {}".format(report[0].text))
            print("Report type: {}".format(report[2].text))
            print("Report user: {}".format(report[3].text))
            print("Report date: {}".format(report[4].text))
            print("Report format: {}".format(report[5].text))

            # get report data
            data = requests.get(qualys_baseurl + qualys_api + 'action=fetch&id=' + report[0].text, headers={'Authorization': qualys_auth, 'X-Requested-With': 'TestAPI'})
            tree_data = ET.ElementTree(ET.fromstring(data.text))
            root_data = tree_data.getroot()

            # print(root_data[0][5].tag)
            # print(root_data[0][5][0].tag, root_data[0][5][0].text)
            # print(root_data[0][5][1].tag, root_data[0][5][1].text)
            # print(root_data[0][5][2].tag, root_data[0][5][2].text)

            # def asset group
            print("Asset group list: ")
            for target in root_data[0][4][0]:
                asset_group_list = target.text.splitlines()
                for asset in asset_group_list:
                    print("\t {}".format(asset))

            print("Total Vulns: {}".format(root_data[0][5][0].text))
            print("Avarage Security Risk: {}".format(root_data[0][5][1].text))
            print("Business Risk: {}".format(root_data[0][5][2].text))

            # check for high CVSS
            # print(root_data[2].tag)
            # print(root_data[2][0][0].tag) ## IP

            print("--------------------")
            print("- Hosts data       -")
            print("--------------------")
            for host in root_data[2]:
                print("Scan info for host {} ({})".format(host[0].text, host[3].text))

                print("--")
                print("\t-- High score vulns")

                for vuln in host[5]:
                    ## search QID
                    qids = vuln.findall("QID")
                    for qid in qids:
                        id = qid.text
                    ## search last_found
                    last_founds = vuln.findall("LAST_FOUND")
                    for last_found in last_founds:
                        last_found_date = last_found.text
                    ## search CVSS3
                    scores = vuln.findall("CVSS3_FINAL")
                    for score in scores:
                        cvss3 = score.text

                    print("\t-- Vuln ID {} \tlast found {} \tCVSS3 {}".format(id, last_found_date, cvss3))

            print("--------------------")
else:
    print("Usage: python ./ReportFromQualys.py YYYY/MM/DD ")

