#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/06/06 19:58:54 (CST) daisuke>
#

# importing json module
import json

# file name
file_json = 'data/osn/sne-2005-2009/2MASSJ02051081-0447150.json'

# opening file
fh = open (file_json, 'r')

# reading JSON data from file
data = json.load (fh)

# closing file
fh.close ()

# printing data
for obj in data:
    print ("obj =", obj)
    for key in data[obj]:
        print ("  %-12s ==> %s" % (key, data[obj][key]) )
