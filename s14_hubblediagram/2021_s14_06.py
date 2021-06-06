#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/06/06 19:23:46 (CST) daisuke>
#

# importing pathlib module
import pathlib

# list of data files
files = pathlib.Path ('.').glob ('data/osn/*/*.json')

# printing file names
for file in sorted (files):
    print (file)
