###################################################################################################
#
# Search any file type by serpapi
# Author: Rocco <Sheliak> Sicilia
# Usage: $ SearchFile.py {_SITE_} {_FILETYPE_} {_KEYW_}
#
###################################################################################################

import sys
import config as cfg
from serpapi import GoogleSearch
import json

if sys.argv[1]:
    site = sys.argv[1]
else:
    sys.exit()

if sys.argv[2]:
    filetype = sys.argv[2]
else:
    sys.exit()

if len(sys.argv) == 4:
    keyw = sys.argv[3]
else:
    keyw = ''

params = {
  "q": keyw + ' site:' + site + ' filetype:' + filetype,
  "num": 500,
  "api_key": cfg.google["token"]
}

search = GoogleSearch(params)
results = search.get_dict()

with open('rawdata.json', 'w') as outfile:
    json.dump(results, outfile)