###################################################################################################
#
# AnonHttpReq.py
# Author: Rocco <Sheliak> Sicilia
# Usage: $ 
#
###################################################################################################

from itertools import count
from random import random, randrange
import sys
import requests

# var
target = sys.argv[1]
urlfile = sys.argv[2]
counter = int(sys.argv[3])
session = requests.session()
useragent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

urls = open(urlfile).readlines()
urls = ' '.join(urls).split()
urls_num = len(urls)

i = 0
while (i <= counter):
    pos = randrange(0, urls_num)
    socksp = randrange(1, 4)
    print("Select URL in pos {}, proxy {}: \t{}".format(pos, socksp, urls[pos]))
    # session.get(urls[pos]).text
    session.proxies = { 'http':  'socks5://192.168.1.6:906{}'.format(socksp), 'https': 'socks5://192.168.1.6:906{}'.format(socksp) }
    session.get(urls[pos], headers = useragent)
    i = i+1
