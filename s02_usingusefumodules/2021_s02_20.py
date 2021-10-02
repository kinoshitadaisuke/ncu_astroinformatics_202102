#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:48 (CST) daisuke>
#

# importing urllib module
import urllib.request

# URL
url = 'http://newton.ex.ac.uk/research/qsystems/collabs/pi/pi3.txt'

# output file name
file_output = 'pi_1000.txt'

# opening WWW connection
fh_in = urllib.request.urlopen (url)

# opening file for writing
fh_out = open (file_output, 'w')

# reading file line by line
for line in fh_in:
    # writing the line into the file
    fh_out.write (line.decode ('utf-8'))

# closing file
fh_out.close ()
