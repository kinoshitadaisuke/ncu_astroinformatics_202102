#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:47 (CST) daisuke>
#

# importing matplotlib module
import argparse
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
parser.add_argument ('-p', type=float, default=1.0, \
                     help='period in hr')
args = parser.parse_args()


# data file name
file_data = args.i

# output file name
file_fig = args.o

# assumed period (day)
p_assumed = args.p / 24.0

# empty numpy arrays for storing data
data_jd      = numpy.array ([])
data_mag_app = numpy.array ([])
data_mag_abs = numpy.array ([])
data_phase   = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # skipping line if the line does not start with digits
        if not (line[0].isdigit):
            continue
        # skipping line if it is empty
        if (line.strip () == ''):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (frame_id_str, month_str, day_str, jd_str, mag_app_str, mag_abs_str) \
            = line.split ()
        # conversion from string into float
        frame_id = float (frame_id_str)
        day = float (day_str)
        jd_str = jd_str.replace (',', '')
        jd = float (jd_str)
        mag_app = float (mag_app_str)
        mag_abs = float (mag_abs_str)

        # appending the data at the end of numpy arrays
        data_jd      = numpy.append (data_jd, jd)
        data_mag_app = numpy.append (data_mag_app, mag_app)
        data_mag_abs = numpy.append (data_mag_abs, mag_abs)

        phase = (jd - data_jd[0]) / p_assumed
        phase -= int (phase)
        data_phase   = numpy.append (data_phase, phase)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Phase'
label_y = 'Absolute Magnitude [mag]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting data
ax.invert_yaxis ()
ax.plot (data_phase, data_mag_abs, 'ro', label='folded lightcurve')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
