###################################################################################################
#
# Test get info from Breach Directory by RapidApi.com
# Author: Rocco <Sheliak> Sicilia
# Usage: $ python3 GetBreachDirectory.py {target_email} {api_key}
#
###################################################################################################

import requests
import sys

target = sys.argv[1]
apikey = sys.argv[2]
url = "https://breachdirectory.p.rapidapi.com/"

querystring = {"func":"auto","term":target}

headers = {
	"X-RapidAPI-Host": "breachdirectory.p.rapidapi.com",
	"X-RapidAPI-Key": apikey
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)