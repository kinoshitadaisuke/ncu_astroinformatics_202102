#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:41 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_data = 'hd61005.data'

# figure file
file_fig = '2021_s08_12.pdf'

#
# constants
#

# speed of light
c = scipy.constants.c
# Planck constant
h = scipy.constants.h
# Boltzmann constant
k = scipy.constants.k

# numpy arrays for storing data
wl    = numpy.array ([])
flux  = numpy.array ([])
err   = numpy.array ([])
wl1   = numpy.array ([])
flux1 = numpy.array ([])
err1  = numpy.array ([])
wl2   = numpy.array ([])
flux2 = numpy.array ([])
err2  = numpy.array ([])

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
        # conversion from string into float
        wl_float   = float (wl_str)
        flux_float = float (flux_str)
        err_float  = float (err_str)
        # wavelength
        wl   = numpy.append (wl, wl_float)
        # flux
        flux = numpy.append (flux, flux_float)
        # error
        err  = numpy.append (err, err_float)
        if (wl_float < 20.0):
            wl1   = numpy.append (wl1, wl_float)
            flux1 = numpy.append (flux1, flux_float)
            err1  = numpy.append (err1, err_float)
        if (wl_float > 30.0):
            wl2   = numpy.append (wl2, wl_float)
            flux2 = numpy.append (flux2, flux_float)
            err2  = numpy.append (err2, err_float)

# initial values of coefficients of fitted function
T1 = 5000.0
T2 = 100.0
a1 = 10**6
a2 = 10**6
init1 = [T1, a1]
init2 = [T2, a2]

# function
def func (x, T, a):
    x_m = x * 10**-6
    f = c / x_m
    y = a * 2.0 * h * f**3 / c**2 / (numpy.exp (h * f / (k * T) ) - 1.0 )
    return (y)

# least-squares method
popt1, pcov1 = scipy.optimize.curve_fit (func, wl1, flux1, \
                                         p0=init1, sigma=err1)
popt2, pcov2 = scipy.optimize.curve_fit (func, wl2, flux2, \
                                         p0=init2, sigma=err2)

print ("T1 = %f K" % (popt1[0]) )
print ("T2 = %f K" % (popt2[0]) )

# fitted curve
wl_min = -0.4
wl_max = 2.7
n      = 10**4
fitted_x = numpy.logspace (wl_min, wl_max, n)
fitted_y = func (fitted_x, popt1[0], popt1[1]) \
    + func (fitted_x, popt2[0], popt2[1])

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
ax.plot (fitted_x, fitted_y, 'b-', linewidth=3, label='Blackbody fitting')
ax.errorbar (wl, flux, yerr=err, fmt='ro', \
             markersize=5, ecolor='black', capsize=3, label='HD61005')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
