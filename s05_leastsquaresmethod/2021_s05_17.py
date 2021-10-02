#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:46:30 (CST) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing numpy module
import numpy

# argument analysis
desc = 'generating synthetic data for least-squares method'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-o', default='', help='output file name')
args = parser.parse_args ()

# output file name
file_output = args.o

# if no name is given for output file, we stop the program.
if (file_output == ''):
    print ("Name of output file has to be specified!")
    sys.exit (1)

#
# parameters
#
a           = 3.0
b           = 5.0
data_min    = 0.0
data_max    = 15.0
data_n      = int (data_max - data_min) + 1
noise_mean  = 0.0
noise_sigma = 0.5

# x
data_x = numpy.linspace (data_min, data_max, data_n)
# y_err
data_yerr = numpy.random.normal (noise_mean, noise_sigma, data_n)
# y
data_y = a * data_x + b + data_yerr

# printing x and y
print ("x:", data_x)
print ("y:", data_y)

# opening file for writing
with open (file_output, 'w') as fh:
    # writing data to file
    for i in range ( len (data_x) ):
        # noise
        noise = numpy.random.normal (noise_mean, noise_sigma)
        # formatting data
        if (i > 10):
            line = "%.3f\t%.3f\t%.3f\n" \
                % (data_x[i], data_y[i] + 9.0, noise + 13.0)
        else:
            line = "%.3f\t%.3f\t%.3f\n" \
                % (data_x[i], data_y[i], noise + 2.0)
        # writing data
        fh.write (line)
