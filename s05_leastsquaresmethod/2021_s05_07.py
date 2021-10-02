#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:58 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# parameters
n = 10**7

# data for integration
# y = -3 * (x - 1)**2 + 3 = -3 * x**2 + 6 * x
data_x1 = numpy.linspace (0.0, 2.0, n)
data_y1 = -3.0 * data_x1**2 + 6.0 * data_x1

# integration using trapezoidal rule
I1 = scipy.integrate.trapz (data_y1, x=data_x1)

# printing result
print ("I1 =", I1)

# data for integration
# y = sin (x)
data_x2 = numpy.linspace (0.0, numpy.pi, n)
data_y2 = numpy.sin (data_x2)

# integration using trapezoidal rule
I2 = scipy.integrate.trapz (data_y2, x=data_x2)

# printing result
print ("I2 =", I2)
