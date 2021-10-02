#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:13 (CST) daisuke>
#

# importing modules
import numpy
import scipy.optimize
import matplotlib.figure
import matplotlib.backends.backend_agg

# input data file
file_data = '2021_s10_05.data'

# output figure file
file_fig = '2021_s10_08.pdf'

# range of data for fitting
x_min_fit = 1.9
x_max_fit = 2.1

# range of data for plotting
x_min_plot = 1.7
x_max_plot = 2.3

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
        if ( (per_hr >= x_min_fit) and (per_hr <= x_max_fit) ):
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
fitted_x = numpy.linspace (x_min_plot, x_max_plot, 10**3)
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
ax.set_xlim (x_min_plot, x_max_plot)
ax.set_ylim (0.0, 0.5)

# plotting a figure
ax.plot (fitted_x, fitted_y, 'r--', label='fitted curve by curve_fit', \
         linewidth=5)
ax.plot (data_all_per, data_all_var, 'b-', label='result of PDM analysis')
ax.legend ()

# saving the figure to a file
fig.savefig (file_fig)
