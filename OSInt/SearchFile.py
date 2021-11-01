###################################################################################################
#
# Search any file type by serpapi
# Author: Rocco <Sheliak> Sicilia
# Usage: $ SearchFile.py {_SITE_} {_FILETYPE_} {_KEYW_}
#
###################################################################################################

from serpapi import GoogleSearch
import config as cfg
import sys


if sys.argv[1]:
    site = sys.argv[1]
else:
    sys.exit()

if sys.argv[2]:
    filetype = sys.argv[2]
else:
    sys.exit()

if sys.argv[3]:
    keyw = sys.argv[3]
else:
    keyw = ''

params = {
  "q": keyw + ' site:"' + site + '" filetype:"' + filetype +'"',
  "google_domain": "google.com",
  "api_key": cfg.google["token"]
}

search = GoogleSearch(params)
results = search.get_dict()

print(results)