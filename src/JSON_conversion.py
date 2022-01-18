# CONVERTING TXT FILE INTO JSON
import re
import json
import pandas as pd

# the file to be converted to
# json format
filename = '2021-12-27_2201 RE BL HLCL Sh#66100459 Doc#HLCUBSC2112BIPH0/message.txt'  #Path of the file
# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
with open(filename) as fh:
    for line in fh:

        if re.search('^([^,]+):', line):
            c = [line.split(":")]
            nam = c[0]

            dict1[nam[0]] = nam[1]
            # Printing the dictionary
            # print(dict1)

# creating json file
# the JSON file is named as test1
out_file = open("mssgtxt_output_1.json", "w")
json.dump(dict1, out_file, indent=4, sort_keys=False)
out_file.close()