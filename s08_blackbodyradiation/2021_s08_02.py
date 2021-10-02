#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:15 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = '2021_s08_02.pdf'

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

# range of wavelength (from 10**-8 m to 10**-4 m)
wl_exponent_min = -8.0
wl_exponent_max = -4.0

# wavelength in metre
wl_exponent = numpy.linspace (wl_exponent_min, wl_exponent_max, 400001)
wl = 10**wl_exponent

# blackbody spectrum
bb = 2.0 * h * c**2 / wl**5 / (numpy.exp (h * c / (wl * k * T) ) - 1.0 )

# finding a peak
bb_max = 0.0
wl_max = 0.0
for i in range ( len (wl) ):
    if (bb[i] > bb_max):
        wl_max = wl[i]
        bb_max = bb[i]

# printing the result
print ("Peak of the spectrum at lambda = %g nm" % (wl_max * 10**9) )
        
# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Wavelength [nm]'
label_y = 'Specific Intensity [W sr^-1 m^-3]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# axes
ax.set_xlim (10, 3000)
ax.set_ylim (0.0, 3.0 * 10**13)

# plotting data
ax.plot (wl * 10**9, bb, 'r-', linewidth=3, label='Blackbody of T = 5800 K')
ax.axvline (wl_max * 10**9, linewidth=3, color='g', label='Peak of spectrum')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
