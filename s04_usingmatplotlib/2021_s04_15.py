#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:05 (CST) daisuke>
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

# importing numpy module
import numpy

# argument analysis
desc = 'a Python script to make a histogram using Matplotlib'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-o', default='', help='output file name')
args = parser.parse_args()

# output file name
file_output = args.o

if (file_output == ''):
    print ("You have to specify the name of output file using -o option.")
    sys.exit ()

# parameters
data_N    = 10**6
mean      = 100.0
stddev    =  10.0
data_min  =  65.0
data_max  = 135.0
bin_width =   0.5
bin_n     = int ( (data_max - data_min) / bin_width ) + 1

# initialisation of Numpy arrays for histogram
histogram_x = numpy.linspace (data_min, data_max, bin_n)
histogram_y = numpy.zeros (bin_n, dtype='int64')
    
# initialisation of random number generator
numpy.random.seed ()

# generating random numbers
data = numpy.random.normal (mean, stddev, data_N)

# processing all the data one-by-one
for i in range ( len (data) ):
    # skipping data if it is outside of the range
    if ( (data[i] > data_max) or (data[i] < data_min) ):
        continue
    # counting
    histogram_y[int ( (data[i] - data_min ) / bin_width )] += 1
    
# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'X [arbitrary unit]'
label_y = 'Number of random numbers'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting histogram
ax.bar (histogram_x, histogram_y, bin_width, edgecolor='black', \
        linewidth=0.3, align='edge', label='Gaussian distribution')
ax.legend ()

# saving the figure to a file
fig.savefig (file_output)
