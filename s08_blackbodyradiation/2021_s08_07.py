#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:29 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.units
import astropy.modeling.models

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = '2021_s08_07.pdf'

# units
unit_micron = astropy.units.micron
unit_K = astropy.units.K

# wavelength
wl_min = -7.0
wl_max = -4.0
n = 10**4
wl = numpy.logspace (wl_min, wl_max, num=n) * 10**6 * unit_micron

# temperature
T = 3000.0 * unit_K

# blackbody radiation
bb = astropy.modeling.models.BlackBody (temperature=T)
bb_data = bb (wl)
    
# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Wavelength [micron]'
label_y = 'Spectral Radiance [erg sec^-1 cm^-2 sr^-1 Hz^-1]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# axes
ax.set_xscale ('log')
ax.set_xlim (0.1, 100)
ax.set_ylim (0.0, 6*10**-6)
ax.grid ()
ax.ticklabel_format (axis="y", style="sci", scilimits=(0,0))

# plotting data
ax.plot (wl, bb_data, 'r-', linewidth=3, label="T=3000K blackbody")
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
