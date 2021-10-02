#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:47 (CST) daisuke>
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
file_data = 'cobe.data'

# figure file
file_fig = '2021_s08_14.pdf'

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
data_freq_kayser  = numpy.array ([])
data_intensity   = numpy.array ([])
data_residual    = numpy.array ([])
data_uncertainty = numpy.array ([])
data_galspec     = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading data file
    for line in fh:
        # skip if the line starts with '#'.
        if (line[0] == '#'):
            continue
        # splitting the data
        (freq_kayser_str, intensity_str, residual_str, uncertainty_str,
         galspec_str) = line.split ()
        # conversion from string into float
        freq_kayser = float (freq_kayser_str)
        intensity   = float (intensity_str)
        residual    = float (residual_str)
        uncertainty = float (uncertainty_str)
        galspec     = float (galspec_str)
        # appending data to numpy arrays
        data_freq_kayser = numpy.append (data_freq_kayser, freq_kayser)
        data_intensity   = numpy.append (data_intensity, intensity)
        data_residual    = numpy.append (data_residual, residual)
        data_uncertainty = numpy.append (data_uncertainty, uncertainty)
        data_galspec     = numpy.append (data_galspec, galspec)

# conversion from wavenumber into wavelength
data_wavelength_mm = 10.0 / data_freq_kayser
data_wavelength_m  = data_wavelength_mm / 10**3

# initial values of coefficients of fitted function
T = 10.0
a = 10**10
init = [T, a]

# function
def func (x, T, a):
    x_mm = 10.0 / x
    x_m = x_mm * 10**-3
    f = c / x_m
    y = a * 2.0 * h * f**3 / c**2 / (numpy.exp (h * f / (k * T) ) - 1.0 )
    return (y)

# least-squares method
popt, pcov = scipy.optimize.curve_fit (func, data_freq_kayser, \
                                       data_intensity, \
                                       p0=init, sigma=data_uncertainty)

print ("popt:")
print (popt)

print ("pcov:")
print (pcov)

# dof
dof = len (data_freq_kayser) - len (init)
print ("dof =", dof)

# residual
residual = data_intensity - func (data_freq_kayser, popt[0], popt[1])
reduced_chi2 = (residual**2).sum () / dof
print ("reduced chi^2 =", reduced_chi2)

# errors of T and a
T_err = numpy.sqrt (pcov[0][0])
a_err = numpy.sqrt (pcov[1][1])
print ("T = %f +/- %f (%f %%)" % (popt[0], T_err, T_err / popt[0] * 100.0) )
print ("a = %f +/- %f (%f %%)" % (popt[1], a_err, a_err / popt[1] * 100.0) )

# fitted curve
fitted_x = numpy.linspace (0.1, 23.0, 10000)
fitted_y = func (fitted_x, popt[0], popt[1])

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Wavenumber [cm^-1]'
label_y = 'Intensity [MJy sr^-1]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# axes
ax.set_xlim (0.0, 23.0)
ax.set_ylim (0.0, 500.0)

# plotting data
ax.plot (fitted_x, fitted_y, 'b-', linewidth=3, label='Blackbody')
ax.errorbar (data_freq_kayser, data_intensity, yerr=data_uncertainty, \
             fmt='ro', markersize=5, ecolor='black', capsize=3, \
             label='CMB measured by COBE/FIRAS')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
