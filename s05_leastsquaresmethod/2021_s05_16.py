#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:46:27 (CST) daisuke>
#

# importing modules
import argparse
import sys
import numpy
import scipy.optimize
import matplotlib.figure
import matplotlib.backends.backend_agg

# argument analysis
desc = 'least-squares method using "curve_fit" of SciPy'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', default='', help='input file name')
parser.add_argument ('-o', default='', help='output file name')
parser.add_argument ('-a', type=float, default=1.0, help='initial value of a')
parser.add_argument ('-b', type=float, default=1.0, help='initial value of b')
parser.add_argument ('-c', type=float, default=1.0, help='initial value of c')
args = parser.parse_args ()

# data file name
file_input  = args.i

# output file name
file_output = args.o

# initial values of fitting coefficients
a = args.a
b = args.b
c = args.c

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

# function for least-squares fitting
def func (x, a, b, c):
    y = a * (x - b)**2 + c
    return y

# least-squares fitting using scipy.optimize.curve_fit
popt, pcov = scipy.optimize.curve_fit (func, data_x, data_y, p0=(a, b, c))

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
dof = len (data_x) - 3
print ("dof =", dof)

# residual
residual = data_y - func (data_x, a_fitted, b_fitted, c_fitted)
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
fitted_x = numpy.linspace (2965.0, 3025.0, 10**6)
fitted_y = a_fitted * (fitted_x - b_fitted)**2 + c_fitted

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
ax.plot (fitted_x, fitted_y, 'm:', label='fitted line by curve_fit')
ax.plot (data_x, data_y, 'gs', label='synthetic data for least-squares method')
ax.legend ()

# saving the figure to a file
fig.savefig (file_output)
