#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:44:43 (CST) daisuke>
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
desc = 'a Python script to make a simple plot using Matplotlib'
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
b      = 5.0
c      = 3.0

# data
noise  = numpy.random.normal (mean, stddev, n)
data_x = numpy.linspace (x_min, x_max, n)
data_y = a * ( data_x - b )**2 + c + noise

# plotting a figure
ax.set_xlim (-1.0, 11.0)
ax.set_ylim (-1.0, +65)
ax.plot (data_x, data_y, 'cs', label='sample data', markersize=10)
ax.legend (loc='upper right')

# saving the figure to a file
fig.savefig (file_output)
