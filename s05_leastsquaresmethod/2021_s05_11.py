#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:46:10 (CST) daisuke>
#

# importing modules
import argparse
import sys
import numpy
import scipy.optimize
import matplotlib.figure
import matplotlib.backends.backend_agg

# argument analysis
desc = 'least-squares fitting using "leastsq" of SciPy'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', default='', help='input file name')
parser.add_argument ('-o', default='', help='output file name')
args = parser.parse_args ()

# data file name
file_input  = args.i

# output file name
file_output = args.o

# if no file name is specified for input file, then we stop the program.
if (file_input == ''):
    print ("The input file name has to be specified.")
    sys.exit (1)
# if no file name is specified for output file, then we stop the program.
if (file_output == ''):
    print ("The output file name has to be specified.")
    sys.exit (1)
# if output file name is not PDF, PNG, PS, or EPS, then we top the program.
if not ( (file_output[-4:] == '.pdf') or (file_output[-4:] == '.png') \
         or (file_output[-3:] == '.ps') or (file_output[-4:] == '.eps') ):
    print ("The output file has to be PDF or PNG, PS, or EPS.")
    sys.exit (1)

# making empty numpy arrays for data
data_x = numpy.array ([])
data_y = numpy.array ([])

# opening file for reading
with open (file_input, 'r') as fh_read:
    # reading data line-by-line
    for line in fh_read:
        # splitting the line into x and y
        (x_str, y_str) = line.split ()
        # converting string into float
        x_float = float (x_str)
        y_float = float (y_str)
        # appending data to numpy arrays
        data_x = numpy.append (data_x, x_float)
        data_y = numpy.append (data_y, y_float)

# printing x and y values
print (data_x)
print (data_y)

# initial values of coefficients of fitted function
param = [1.0, 1.0]

# function for least-squares fitting
def func (x, param):
    y = param[0] * x + param[1]
    return y

# calculation of residual
def residue (param, x, y):
    residual = y - func (x, param)
    return residual

# least-squares fitting using scipy.optimize.leastsq
fit = scipy.optimize.leastsq (residue, param, args=(data_x, data_y), \
                              full_output=True)

# fitted coefficients
a_fitted = fit[0][0]
b_fitted = fit[0][1]
print ("fitted coefficients:")
print ("  a = %f" % a_fitted)
print ("  b = %f" % b_fitted)

# degree of freedom
dof = len (data_x) - len (param)
print ("dof = %d" % dof)

# calculation of reduced chi-square
residual = residue (fit[0], data_x, data_y)
reduced_chi_square = (residual**2).sum () / dof
print ("reduced chi-square = %f" % reduced_chi_square)

# calculation of covariance matrix
covar = fit[1] * reduced_chi_square
print ('covariance matrix:')
print (covar)

# errors of fitted coefficients
fit_err         = [0.0] * len (fit[0])
fit_err_percent = [0.0] * len (fit[0])
fit_err[0] = numpy.sqrt (covar[0][0])
fit_err[1] = numpy.sqrt (covar[1][1])
fit_err_percent[0] = fit_err[0] / fit[0][0] * 100.0
fit_err_percent[1] = fit_err[1] / fit[0][1] * 100.0
print ("errors of fitted coefficients:")
print ("  ", fit_err)
print ("errors of fitted coefficients [%]:")
print ("  ", fit_err_percent)

# printing results
print ("results of fitting:")
print ("  a = %f +/- %f (%f %%)" \
       % (a_fitted, fit_err[0], fit_err_percent[0]) )
print ("  b = %f +/- %f (%f %%)" \
       % (b_fitted, fit_err[1], fit_err_percent[1]) )

# fitted line
fitted_x = numpy.linspace (-1.0, 11.0, 10**6)
fitted_y = a_fitted * fitted_x + b_fitted

# making fig and ax
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'X [arbitrary unit]'
label_y = 'Y [arbitrary unit]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting a figure
ax.plot (fitted_x, fitted_y, 'r--', label='fitted line by least-squares method')
ax.plot (data_x, data_y, 'bo', label='synthetic data for least-squares method')
ax.legend ()

# saving the figure to a file
fig.savefig (file_output)
