#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:33 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.units
import astropy.modeling.models

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_data = 'sun.data'

# figure file name
file_fig = '2021_s08_09.pdf'

# units
unit_W  = astropy.units.W
unit_m  = astropy.units.m
unit_nm = astropy.units.nm
unit_sr = astropy.units.sr
unit_K  = astropy.units.K

# initialisation of numpy arrays for storing data
wl = numpy.array ([])
irradiance = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # initialisation of the parameter "i" for counting lines
    i = 0
    # reading data line-by-line
    for line in fh:
        # incrementing line number
        i += 1
        # skipping first 9 lines
        if (i < 10):
            continue
        # splitting data into wavelength and irradiance
        line = line.strip ()
        (wl_str, irradiance_str) = line.split ()
        # converting string into float
        wl_float = float (wl_str)
        irradiance_float = float (irradiance_str)
        # appending data to numpy arrays
        wl = numpy.append (wl, wl_float)
        irradiance = numpy.append (irradiance, irradiance_float)

# wavelength
wl2_min = -7.0
wl2_max = -5.0
n = 10**4
wl2 = numpy.logspace (wl2_min, wl2_max, num=n) * 10**9 * unit_nm

# temperature
T = 5780.0 * unit_K

# blackbody radiation
bb = astropy.modeling.models.BlackBody \
    (temperature=T, \
     scale=7.0 * 10**-5 * unit_W / (unit_m**2 * unit_nm * unit_sr) )
bb_data = bb (wl2)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Wavelength [nm]'
label_y = 'Irradiance [W m^-2 nm^-1]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# axes
ax.set_xlim (100, 10000)
ax.set_ylim (0.0, 2.5)
ax.set_xscale ('log')

# plotting data
ax.plot (wl, irradiance, 'r-', label='Sun')
ax.plot (wl2, bb_data, 'b-', label='T=5780K Blackbody')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
