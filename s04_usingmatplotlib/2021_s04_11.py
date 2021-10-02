#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:44:51 (CST) daisuke>
#

# importing sys module
import sys

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# argument analysis
desc = 'a Python script to make a log plot using Matplotlib'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-o', default='', help='output file name')
args = parser.parse_args()

# output file name
file_output = args.o

if (file_output == ''):
    print ("You have to specify the name of output file using -o option.")
    sys.exit ()

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'X [arbitrary unit]'
label_y = 'Y [arbitrary unit]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# parameters
x_min  = 0.0
x_max  = 10.0
n      = 11
mean   = 0.0
stddev = 0.3
a      = 2.0
b      = 0.5
c      = 10.0

# data
noise   = numpy.random.normal (mean, stddev, n)
data_x  = numpy.linspace (x_min, x_max, n)
data_y  = a * numpy.exp (b * data_x) + c + noise
error_y = numpy.random.normal (mean, stddev, n) + 10.0

# plotting a figure
ax.set_xlim (-1.0, 11.0)
ax.set_ylim (1, 10**3)
ax.set_yscale ('log')
ax.errorbar (data_x, data_y, yerr=error_y, \
             label='sample data for log plot', \
             fmt='bp', markersize=8, ecolor='black', capsize=5)
ax.legend (loc='upper left')

# saving the figure to a file
fig.savefig (file_output)
