#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:43 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_data = 'cobe.data'

# figure file
file_fig = '2021_s08_13.pdf'

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
ax.errorbar (data_freq_kayser, data_intensity, yerr=data_uncertainty, \
             fmt='ro', markersize=5, ecolor='black', capsize=3, \
             label='CMB measured by COBE/FIRAS')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
