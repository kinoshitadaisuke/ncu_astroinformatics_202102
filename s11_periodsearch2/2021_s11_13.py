#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:52:38 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser (description='plotting time-series data')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.eps", \
                     help='output figure file name')
args = parser.parse_args ()

# data file name
file_data = args.i

# output file name
file_fig = args.o

# empty numpy arrays for storing data
data_mjd  = numpy.array ([])
data_flux = numpy.array ([])
data_err  = numpy.array ([])

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
        (datetime_str, mjd_str, flux_str, err_str) = line.split ()
        # conversion from string into float
        mjd  = float (mjd_str)
        flux = float (flux_str) / 10**6
        err  = float (err_str) / 10**6
        # appending the data at the end of numpy arrays
        data_mjd  = numpy.append (data_mjd, mjd)
        data_flux = numpy.append (data_flux, flux)
        data_err  = numpy.append (data_err, err)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'MJD [day]'
label_y = 'Flux [10^6 e-/sec]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting data
ax.errorbar (data_mjd, data_flux, yerr=data_err, fmt='b.', \
             markersize=1, ecolor='black', capsize=1, \
             label='photometry of Kepler-13')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
