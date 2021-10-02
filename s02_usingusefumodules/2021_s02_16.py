#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:33 (CST) daisuke>
#

# importing Matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
# importing numpy module
import numpy

# output file name
file_output = '2021_s02_16.pdf'

# constants for straight line
# a * x + b
a = 3.0
b = 5.0

# constants for random number generation
mean = 0.0
stddev = 1.0

# number of data to be generated
n = 16

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'X [arbitrary unit]'
label_y = 'Y [arbitrary unit]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# generating data
line_x = numpy.linspace (0.0, 15.0, 1001)
line_y = a * line_x + b

error_y = numpy.random.normal (mean, stddev, n)
data_x = numpy.linspace (0.0, 15.0, n)
data_y = a * data_x + b + error_y

yerr = [ stddev * 2 ] * n

# plotting a figure
ax.plot (line_x, line_y, 'r--', label='theoretical prediction')
ax.errorbar (data_x, data_y, yerr=yerr, fmt='bo', ecolor='black', \
             capsize=5, label='data')
ax.legend ()

# saving the figure to a file
fig.savefig (file_output)
