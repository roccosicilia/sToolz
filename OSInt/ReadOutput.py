###################################################################################################
#
# Read json output
# Author: Rocco <Sheliak> Sicilia
# Usage: $ ReadOutput.py {_OPERATION_}
#          ---> "-p"    print file list
#
###################################################################################################

import sys
import json

if len(sys.argv) == 1:

    with open('rawdata.json') as json_file:
        results = json.load(json_file)

        ## view all information
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

        sys.exit()

else:

    with open('rawdata.json') as json_file:
        results = json.load(json_file)

    ### print file list
    if sys.argv[1] == '-p':
        for result in results["organic_results"]:
            print(result['title'])
