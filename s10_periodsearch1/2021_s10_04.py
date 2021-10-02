#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:03 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing numpy module
import numpy

# data file name
file_data = '2021_s10_01.data'

# output file name
file_fig = '2021_s10_04.pdf'

# assumed period (day)
p_assumed_hr = numpy.array ([ 1.0, 1.5, 2.0, 2.5, 3.0, 3.5 ])
p_assumed_day = p_assumed_hr / 24.0

# empty numpy arrays for storing data
data_mjd   = numpy.array ([])
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
        mjd = float (mjd_str)
        mag = float (mag_str)
        # appending the data at the end of numpy arrays
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making multiple plots
for i in range (len (p_assumed_hr)):
    # making a subplot
    subplot = 320 + int (i) + 1
    ax = fig.add_subplot (subplot)

    # calculation of phase
    p_assumed = p_assumed_day[i]
    data_phase = numpy.array ([])
    for mjd in data_mjd:
        phase = mjd / p_assumed - int (mjd / p_assumed)
        data_phase = numpy.append (data_phase, phase)
    
    # labels
    label_x = 'Phase'
    label_y = 'Magnitude [mag]'
    if ( (i > 3) ):
        ax.set_xlabel (label_x)
    if (i % 2 == 0):
        ax.set_ylabel (label_y)

    # range
    ax.set_xlim (0.0, 1.0)
    ax.set_ylim (16.5, 15.0)

    # plotting data
    figlabel = "assumed period %3.1f hr" % p_assumed_hr[i]
    ax.plot (data_phase, data_mag, 'b.', label=figlabel)
    ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
