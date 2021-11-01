###################################################################################################
#
# Read json output
# Author: Rocco <Sheliak> Sicilia
# Usage: $ ReadOutput.py {_FILENAME_}
#
###################################################################################################

import sys
import json

with open('data.json') as json_file:
    results = json.load(json_file)

    for data in results:
        print(data)

