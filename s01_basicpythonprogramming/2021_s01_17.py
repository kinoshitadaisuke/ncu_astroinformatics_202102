#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:13 (CST) daisuke>
#

# importing pathlib
import pathlib

# file name
filename = 'site.data'

# constructing a path object
path_sitedata = pathlib.Path (filename)

# reading file
with path_sitedata.open () as fh:
    lines = fh.readlines ()

# printing data
for line in lines:
    # skip the line if the line starts with '#'
    if (line[0] == '#'):
        continue
    # split the line into fields
    (site, longitude, latitude, altitude, timezone) = line.split ()
    # print information
    print ("%-8s  %4d m above sea level" % (site, float (altitude)) )
