#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:44:26 (CST) daisuke>
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
desc = 'a Python script to make a cosine curve plot using Matplotlib'
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

# data
data_x = numpy.linspace (0.0, 3.0, 3001)
data_y = numpy.cos (2.0 * numpy.pi * data_x)

# plotting a figure
ax.set_xlim (-0.2, 3.2)
ax.set_ylim (-1.3, +1.3)
ax.plot (data_x, data_y, '-', label='cosine curve')
ax.legend (loc='upper right')

# saving the figure to a file
fig.savefig (file_output)
