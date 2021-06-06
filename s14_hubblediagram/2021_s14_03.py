#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/06/06 16:26:40 (CST) daisuke>
#

# importing astropy module
import astropy.io.ascii

# file
file_data = 'ned1d_with_header.csv'

# reading CSV data
rawdata = astropy.io.ascii.read (file_data, format='csv')

# printing astropy table information
print (rawdata.info ())

# printing data
print (rawdata)
