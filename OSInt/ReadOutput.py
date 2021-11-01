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

    print("####################")
    print(results["search_metadata"])

    print("####################")
    print(results["search_parameters"])

    print("####################")
    print(results["search_information"])

    print("####################")
    print(results["organic_results"])

    print("####################")
    print(results["pagination"])

    print("####################")
    print(results["serpapi_pagination"])
    