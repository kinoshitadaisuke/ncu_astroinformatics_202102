#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:24 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = '2021_s08_05.pdf'

#
# constants
#

# speed of light
c = scipy.constants.c
# Planck constant
h = scipy.constants.h
# Boltzmann constant
k = scipy.constants.k

#
# parameters
#

# temperature
T = 5800.0

# range of frequency (from 10**0 Hz to 10**16 Hz)
f_exponent_min = 0.0
f_exponent_max = 16.0

# frequency
f_exponent = numpy.linspace (f_exponent_min, f_exponent_max, 160001)
f = 10**f_exponent

# blackbody spectrum
bb_p  = 2.0 * h * f**3 / c**2 / (numpy.exp (h * f / (k * T) ) - 1.0 )
bb_rj = 2.0 * f**2 * k * T / c**2
bb_w  = 2.0 * h * f**3 / c**2 * numpy.exp (-h * f / (k * T) )

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Frequency [Hz]'
label_y = 'Specific Intensity [W sr^-1 m^-2 Hz^-1]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (10**2, 10**18)
ax.set_ylim (10**-30, 10**-5)

# plotting data
ax.plot (f, bb_p, 'r-', linewidth=5, label="Planck's law")
ax.plot (f, bb_rj, 'g-', linewidth=2, label="Rayleigh-Jeans law")
ax.plot (f, bb_w, 'b-', linewidth=2, label="Wien's law")
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
