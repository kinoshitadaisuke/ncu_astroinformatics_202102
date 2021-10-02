#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:33 (CST) daisuke>
#

# importing modules
import argparse
import numpy
import scipy.optimize
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser (description='Phase Dispersion Minimization')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.pdf", \
                     help='output figure file name')
parser.add_argument ('-a', type=float, default=0.0, \
                     help='minimum period to be used for fitting')
parser.add_argument ('-b', type=float, default=100.0, \
                     help='maximum period to be used for fitting')
args = parser.parse_args()

# input data file
file_data = args.i

# output figure file
file_fig = args.o

# range of data for fitting
x_min = args.a
x_max = args.b

# empty numpy array for storing data
data_all_per = numpy.array ([])
data_all_var = numpy.array ([])
data_fit_per = numpy.array ([])
data_fit_var = numpy.array ([])

# opening file for reading
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (per_day_str, per_hr_str, per_min_str, var_str) = line.split ()
        # conversion from string into float
        per_hr = float (per_hr_str)
        var = float (var_str)
        # appending the data at the end of numpy arrays
        data_all_per = numpy.append (data_all_per, per_hr)
        data_all_var = numpy.append (data_all_var, var)
        if ( (per_hr >= x_min) and (per_hr <= x_max) ):
            data_fit_per = numpy.append (data_fit_per, per_hr)
            data_fit_var = numpy.append (data_fit_var, var)

# initial values of coefficients of fitted function
a = 1.0
b = 1.0
c = 1.0

# function to be used for least-squares fitting
def func (x, a, b, c):
    y = a * (x - b)**2 + c
    return y

# least-squares fitting using scipy.optimize.curve_fit
popt, pcov = scipy.optimize.curve_fit (func, data_fit_per, data_fit_var)

# fitted coefficients
print ("popt:")
print (popt)

# covariance matrix
print ("pcov:")
print (pcov)

# fitted a and b
a_fitted = popt[0]
b_fitted = popt[1]
c_fitted = popt[2]

# degree of freedom
dof = len (data_fit_per) - 3
print ("dof =", dof)

# residual
residual = data_fit_var - func (data_fit_per, a_fitted, b_fitted, c_fitted)
reduced_chi2 = (residual**2).sum () / dof
print ("reduced chi^2 =", reduced_chi2)

# errors of a and b
a_err = numpy.sqrt (pcov[0][0])
b_err = numpy.sqrt (pcov[1][1])
c_err = numpy.sqrt (pcov[2][2])
print ("a = %f +/- %f (%f %%)" % (a_fitted, a_err, a_err / a_fitted * 100.0) )
print ("b = %f +/- %f (%f %%)" % (b_fitted, b_err, b_err / b_fitted * 100.0) )
print ("c = %f +/- %f (%f %%)" % (c_fitted, c_err, c_err / c_fitted * 100.0) )

# fitted line
fitted_x = numpy.linspace (x_min, x_max, 10**3)
fitted_y = func (fitted_x, a_fitted, b_fitted, c_fitted)

# making fig and ax
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Period [hr]'
label_y = 'Variance'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# range of plot
ax.set_xlim (x_min, x_max)
ax.set_ylim (0, func (x_max, a_fitted, b_fitted, c_fitted) * 1.2 )

# plotting a figure
ax.plot (fitted_x, fitted_y, 'r--', label='fitted curve by curve_fit', \
         linewidth=5)
ax.plot (data_all_per, data_all_var, 'b-', label='result of PDM analysis')
ax.legend ()

# saving the figure to a file
fig.savefig (file_fig)
