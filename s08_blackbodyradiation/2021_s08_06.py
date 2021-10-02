#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:26 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = '2021_s08_06.pdf'

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

# range of frequency (from 10**3 Hz to 10**20 Hz)
f_exponent_min = 3.0
f_exponent_max = 20.0

# frequency
f_exponent = numpy.linspace (f_exponent_min, f_exponent_max, 170001)
f = 10**f_exponent

bb = numpy.array ([])

# blackbody spectrum
for i in range (9):
    T = 10**(float (i))
    bb_T = 2.0 * h * f**3 / c**2 / (numpy.exp (h * f / (k * T) ) - 1.0 )
    bb = numpy.append (bb, bb_T)

# reshape the numpy array
bb = bb.reshape (9, 170001)
    
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
ax.set_xlim (10**3.0, 10**20.0)
ax.set_ylim (10**-30.0, 10**7.0)
ax.grid ()

# plotting data
for i in range (9):
    label = "T = 10^%d K" % (i)
    ax.plot (f, bb[i], '-', linewidth=3, label=label)
ax.legend ()

# secondary x-axis
ax2 = ax.twiny ()
label_x2 = 'Wavelength [m]'
ax2.set_xlabel (label_x2)
ax2.set_xscale ('log')
ax2.set_xlim (c/10**3.0, c/10**20.0)

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
