#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:44:31 (CST) daisuke>
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
desc = 'a Python script to make a line plot using Matplotlib'
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
x_max  = 3.0
n      = 101
mean   = 0.0
stddev = 0.1

# data
noise1  = numpy.random.normal (mean, stddev, n)
data_x1 = numpy.linspace (x_min, x_max, n)
data_y1 = numpy.sin (2.0 * numpy.pi * data_x1) + noise1

noise2  = numpy.random.normal (mean, stddev, n)
data_x2 = numpy.linspace (x_min, x_max, n)
data_y2 = 2.0 * numpy.sin (3.0 * numpy.pi * data_x2) + noise2

noise3  = numpy.random.normal (mean, stddev, n)
data_x3 = numpy.linspace (x_min, x_max, n)
data_y3 = 0.5 * numpy.sin (1.0 * numpy.pi * data_x3) + noise3

# plotting a figure
ax.set_xlim (-0.2, 3.2)
ax.set_ylim (-3.7, +3.7)
ax.plot (data_x1, data_y1, 'r-', label='sine curve 1')
ax.plot (data_x2, data_y2, 'g-', label='sine curve 2')
ax.plot (data_x3, data_y3, 'b-', label='sine curve 3')
ax.legend (loc='upper right')

# saving the figure to a file
fig.savefig (file_output)
