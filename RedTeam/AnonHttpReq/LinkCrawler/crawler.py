###################################################################################################
#
# Get link from a website
# Author: Rocco <Sheliak> Sicilia
# Usage: $ python ./crawler.py {target} {filename}
#
###################################################################################################

import sys
import requests

# vars
target = sys.argv[1]
filename = sys.argv[2]

content = requests.get(target)
content_html = content.text
#print(content_html)

lines = content_html.splitlines()
for line in lines:
    if 'href=' in line:
        # print(line.strip())
        string = line.split(' ')
        for element in string:
            # print(element)
            if 'href=' in element:
                # print(element)
                link = element.split('>')
                link = link[0].replace('href=', '')
                link = link.replace("'", '')
                link = link.replace('"', '')
                if len(link) > 3 and target in link:
                    print(link)
                    with open("{}".format(filename), "a") as output:
                        output.write(link + "\r\n")
