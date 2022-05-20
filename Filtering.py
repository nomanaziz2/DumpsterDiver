#!/usr/bin/python

import json
import sys
import re

# Opening JSON file
f = open(sys.argv[1])

# File for Filtering
filteredFiles = set()

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    filteredFiles.add(i['File'])

# Closing file
f.close()

# Printing Lines with Quotes
for file in filteredFiles:
    with open(file, 'r') as f:
        lines = f.readlines()

        found = False

        for line in lines:

            # For matching quotes
            regex = re.compile(
                r"(:|=)( *)(?P<quote>['\"])(?P<string>.*?)(?<!\\)(?P=quote)")

            match = regex.search(line)

            if match:

                # For not including imports in dart language
                regex2 = re.compile(r"import '.+'")

                match2 = regex2.search(line)

                if not match2:

                    if not found:
                        found = True
                        print("File : ", file)

                    print("\t", line)
