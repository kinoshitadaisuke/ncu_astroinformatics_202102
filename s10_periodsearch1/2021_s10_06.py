#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:08 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing numpy module
import numpy

# data file name
file_data = '2021_s10_05.data'

# output file name
file_fig = '2021_s10_06.pdf'

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
label_x = 'Period [hr]'
label_y = 'Variance'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting data
ax.set_ylim (0.0, 0.5)
ax.plot (data_per, data_var, 'b-', label='result of PDM analysis')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
