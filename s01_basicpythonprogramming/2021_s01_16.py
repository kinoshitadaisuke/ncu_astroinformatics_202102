#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:01 (CST) daisuke>
#

# file name
filename = 'site.data'

# opening file in read mode
fh = open (filename, 'r')

# reading file line-by-line
for line in fh:
    # skip the line if the line starts with '#'
    if (line[0] == '#'):
        continue
    # split the line into fields
    (site, longitude, latitude, altitude, timezone) = line.split ()
    # print information
    print ("%-8s  %4d m above sea level" % (site, float (altitude)) )

# closing file
fh.close ()
