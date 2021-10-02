#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:22 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing numpy module
import numpy

# data file name
file_data = '2021_s10_10.data'

# output file name
file_fig = '2021_s10_11.pdf'

# empty numpy arrays for storing data
data_mjd = numpy.array ([])
data_mag = numpy.array ([])
data_err = numpy.array ([])

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
        (datetime, mjd_str, mag_str, err_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        err = float (err_str)
        # appending the data at the end of numpy arrays
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)
        data_err = numpy.append (data_err, err)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'MJD - 59000 [day]'
label_y = 'Apparent Magnitude [mag]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# range
ax.set_ylim (19.5, 18.5)

# plotting data
ax.errorbar (data_mjd - 59000, data_mag, yerr=data_err, fmt='bo', \
             markersize=5, ecolor='black', capsize=5, \
             label='synthetic time-series data')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
