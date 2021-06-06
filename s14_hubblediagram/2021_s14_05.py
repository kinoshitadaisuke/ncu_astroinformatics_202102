#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/06/06 16:53:43 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize
import scipy.constants

# importing astropy module
import astropy.io.ascii
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
desc = 'estimating Hubble constant using least-squares method'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', '--input', help='input data file name')
parser.add_argument ('-o', '--output', help='output figure file name')
args = parser.parse_args ()

# file names
file_data = args.input
file_fig  = args.output

# constants
c = scipy.constants.c

# reading CSV data
rawdata = astropy.io.ascii.read (file_data, format='csv')

# dictionary to store data
data = {}

# examining the data
for i in range ( len (rawdata) ):
    # extracting data
    # name of galaxy
    name = rawdata[i]['NAME']
    # distance modulus
    distmod = rawdata[i]['m-M']
    # error of distance modulus
    distmod_err = rawdata[i]['err']
    # distance in Mpc
    dist_Mpc = rawdata[i]['D [Mpc]']
    # redshift
    z = rawdata[i]['col10']
    # velocity in m/s
    v = ( (z + 1.0)**2 - 1.0 ) / ( (z + 1.0)**2 + 1.0 ) * c
    # appending data to the dictionary
    # skip if redshift is missing.
    # skip if error of distance modulus is large.
    # skip if distance is larger than 500 Mpc
    if ( (z > 0.0) and (distmod_err < 0.05) and (dist_Mpc < 300.0) \
         and (v < 5.0 * 10**7) ):
        # if the data is not in the dictionary, add data
        if not name in data:
            data[name] = {}
            data[name]['distmod'] = distmod
            data[name]['distmod_err'] = distmod_err
            data[name]['dist_Mpc'] = dist_Mpc
            data[name]['z'] = z
            data[name]['v'] = v

# making numpy arrays for plotting data
data_d = numpy.array ([])
data_v = numpy.array ([])
for name in sorted (data, key=lambda x: data[x]['dist_Mpc']):
    data_d = numpy.append (data_d, data[name]['dist_Mpc'])
    data_v = numpy.append (data_v, data[name]['v'] * 10**-3)

# initial values of coefficient
H0 = 100.0
init = [H0]

# function
def func (x, H0):
    y = H0 * x
    return (y)

# least-squares method
popt, pcov = scipy.optimize.curve_fit (func, data_d, data_v, p0=init)

# result of fitting
H0_bestfit = popt[0]
print ("popt:")
print (popt)
print ("pcov:")
print (pcov)

# degree of freedom
dof = len (data_d) - len (init)
print ("dof =", dof)

# residual
residual = data_v - func (data_d, popt[0])
reduced_chi2 = (residual**2).sum () / dof
print ("reduced chi^2 =", reduced_chi2)

# error of H0
H0_err = numpy.sqrt (pcov[0][0])
print ("H0 = %f +/- %f (%f %%)" \
       % (H0_bestfit, H0_err, H0_err / H0_bestfit * 100.0) )

# fitted curve
fitted_x = numpy.linspace (0.0, 300.0, 1000)
fitted_y = func (fitted_x, H0_bestfit)
    
# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# axes
ax.set_xlabel ('Distance [Mpc]')
ax.set_ylabel ('Velocity [km/s]')
ax.grid ()

# making a Hubble diagram
label_fitting = "best-fit line (H0=%4.1f)" % (H0_bestfit)
ax.plot (fitted_x, fitted_y, linestyle='--', color='red', \
         label=label_fitting)
ax.plot (data_d, data_v, \
         marker='o', color='blue', markersize=2, linestyle='none', \
         label='galaxies in NED-1D')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=450)
