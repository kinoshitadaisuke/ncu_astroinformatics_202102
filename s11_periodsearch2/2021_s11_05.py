#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:52:18 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser (description='plotting power spectrum')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.pdf", \
                     help='output figure file name')
args = parser.parse_args ()

# data file name
file_data = args.i

# output file name
file_fig = args.o

# empty numpy arrays for storing data
data_freq    = numpy.array ([])
data_per_day = numpy.array ([])
data_per_hr  = numpy.array ([])
data_per_min = numpy.array ([])
data_power   = numpy.array ([])

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
        (freq_str, per_day_str, per_hr_str, per_min_str, power_str) \
            = line.split ()
        # conversion from string into float
        freq    = float (freq_str)
        per_day = float (per_day_str)
        per_hr  = float (per_hr_str)
        per_min = float (per_min_str)
        power   = float (power_str)
        # appending the data at the end of numpy arrays
        data_freq    = numpy.append (data_freq, freq)
        data_per_day = numpy.append (data_per_day, per_day)
        data_per_hr  = numpy.append (data_per_hr, per_hr)
        data_per_min = numpy.append (data_per_min, per_min)
        data_power   = numpy.append (data_power, power)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Period [hr]'
label_y = 'Power'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting data
ax.plot (data_per_hr, data_power, 'b-', \
         label='result of Lomb-Scargle periodogram')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
