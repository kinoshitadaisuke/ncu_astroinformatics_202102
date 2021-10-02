#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:39 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing numpy module
import numpy

# input file
file_data = 'varuna.data'

# output file
file_fig = '2021_s10_17.pdf'

data_jd      = numpy.array ([])
data_mag_app = numpy.array ([])
data_mag_abs = numpy.array ([])

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

        # only the data taken on 17 Feb are used for plotting
        if not ( (month_str == 'Feb') and (day_str[0:2] == '17') ):
            continue
        
        # appending the data at the end of numpy arrays
        data_jd      = numpy.append (data_jd, jd)
        data_mag_app = numpy.append (data_mag_app, mag_app)
        data_mag_abs = numpy.append (data_mag_abs, mag_abs)
        
# making fig and ax
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'JD - 2451950'
label_y = 'R-band Absolute Magnitude [mag]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting a figure
ax.invert_yaxis ()
ax.plot (data_jd - 1950.0, data_mag_app, 'ro', label='(20000) Varuna')
ax.legend ()

# saving the figure to a file
fig.savefig (file_fig)
