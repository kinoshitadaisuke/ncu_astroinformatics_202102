#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:52:43 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# command-line argument analysis
parser = argparse.ArgumentParser (description='plotting time-series data')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.eps", \
                     help='output figure file name')
args = parser.parse_args ()

# data file name
file_data = args.i

# output file name
file_fig = args.o

# coefficients
a = 30.994049
b = 3436918.663151

# empty numpy arrays for storing data
data_mjd  = numpy.array ([])
data_flux = numpy.array ([])
data_err  = numpy.array ([])

# opening file for reading
with open (file_data, 'r') as fh_read:
    # opening file for writing
    with open (file_fig, 'w') as fh_write:
        # reading file line-by-line
        for line in fh_read:
            # skipping line if the line starts with '#'
            if (line[0] == '#'):
                continue
            # removing line feed at the end of line
            line = line.strip ()
            # splitting data
            (datetime_str, mjd_str, flux_str, err_str) = line.split ()
            # check data
            if (flux_str == 'nan'):
                continue
            # conversion from string into float
            mjd  = float (mjd_str)
            flux = float (flux_str) / (-a * mjd + b)
            err  = float (err_str) / float (flux_str)
            # writing data
            record = "%s %.10f %.10f %.10f\n" % (datetime_str, mjd, flux, err)
            fh_write.write (record)
