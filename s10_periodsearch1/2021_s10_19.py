#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:44 (CST) daisuke>
#

# importing argparse module
import argparse

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing numpy module
import numpy

# command-line argument analysis
parser = argparse.ArgumentParser (description='Phase Dispersion Minimization')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.pdf", \
                     help='output figure file name')
parser.add_argument ('-a', type=float, default=0.0, \
                     help='minimum value of x to be plotted')
parser.add_argument ('-b', type=float, default=100.0, \
                     help='maximum value of x to be plotted')
args = parser.parse_args()

# input file name
file_data = args.i

# output file name
file_fig = args.o

# range of x on the plot
x_min = args.a
x_max = args.b

# empty numpy arrays for storing data
data_per = numpy.array ([])
data_var = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (per_day_str, per_hr_str, per_min_str, var_str) = line.split ()
        # conversion from string into float
        per_hr = float (per_hr_str)
        var = float (var_str)
        # appending the data at the end of numpy arrays
        data_per = numpy.append (data_per, per_hr)
        data_var = numpy.append (data_var, var)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Frequency [cycle/day]'
label_y = 'Variance'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# range
ax.set_xlim (x_min, x_max)

# plotting data
ax.plot (24.0 / data_per, data_var, 'b-', label='result of PDM analysis')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
