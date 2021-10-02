#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:38 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_data = 'hd61005.data'

# figure file
file_fig = '2021_s08_11.pdf'

# numpy arrays for storing data
wl   = numpy.array ([])
flux = numpy.array ([])
err  = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading data file
    for line in fh:
        # if line starts with '#', the skip
        if (line[0] == '#'):
            continue
        # splitting the line
        data     = line.split ()
        wl_str   = data[0]
        flux_str = data[1]
        err_str  = data[2]
        # wavelength
        wl   = numpy.append (wl, float (wl_str))
        # flux
        flux = numpy.append (flux, float (flux_str))
        # error
        err  = numpy.append (err, float (err_str))

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Wavelength [micron]'
label_y = 'Flux [Jy]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')

# plotting data
ax.errorbar (wl, flux, yerr=err, fmt='ro', \
             markersize=5, ecolor='black', capsize=3, label='HD61005')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
