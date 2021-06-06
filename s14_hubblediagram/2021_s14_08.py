#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/06/06 20:01:22 (CST) daisuke>
#

# importing pathlib module
import pathlib

# importing json module
import json

# list of data files
files = pathlib.Path ('.').glob ('data/osn/*/*.json')

# key names
key_type = 'claimedtype'

# processing each file
for file in sorted (files):
    # opening file
    with open (file, 'r') as fh:
        # reading JSON data from file
        data = json.load (fh)

    # checking all the objects in JSON file
    for obj in data:
        # skip if type is not known
        if not (key_type in data[obj]):
            continue
        # skip if supernova is not type-Ia
        if not (data[obj][key_type][0]['value'] == 'Ia'):
            continue
        # printing data
        print ("%s ==> %s" % (obj, data[obj][key_type][0]['value']) )
