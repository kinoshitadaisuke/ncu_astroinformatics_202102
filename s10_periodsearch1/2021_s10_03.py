#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:00 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing numpy module
import numpy

# data file name
file_data = '2021_s10_01.data'

# output file name
file_fig = '2021_s10_03.pdf'

# assumed period (day)
p_assumed = 1.0 / 24

# empty numpy arrays for storing data
data_mjd   = numpy.array ([])
data_phase = numpy.array ([])
data_mag   = numpy.array ([])

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
        (datetime, mjd_str, mag_str) = line.split ()
        # conversion from string into float
        mjd   = float (mjd_str)
        mag   = float (mag_str)
        phase = mjd / p_assumed - int (mjd / p_assumed)
        # appending the data at the end of numpy arrays
        data_mjd   = numpy.append (data_mjd, mjd)
        data_phase = numpy.append (data_phase, phase)
        data_mag   = numpy.append (data_mag, mag)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Phase'
label_y = 'Apparent Magnitude [mag]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# range
ax.set_ylim (16.5, 15.5)

# plotting data
ax.plot (data_phase, data_mag, 'bo', label='synthetic time-series data')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
