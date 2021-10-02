#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:46:01 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# parameters
n = 10**7

# data for integration
data_x1 = numpy.linspace (0.0, 1.0, n)
data_y1 = numpy.sqrt (1.0 - data_x1**2)

# integration using Simpson's rule
I1 = scipy.integrate.simps (data_y1, x=data_x1)

# printing result
print ("I1   =", I1)
print ("pi/4 =", numpy.pi / 4.0)

# data for integration
mean    = 50.0
sigma   = 10.0
x_max   = mean + 3.0 * sigma
x_min   = mean - 3.0 * sigma
data_x2 = numpy.linspace (x_min, x_max, n)
data_y2 = numpy.exp (-1.0 * (data_x2 - mean)**2 / (2.0 * sigma**2)) \
    / numpy.sqrt (2.0 * numpy.pi * sigma**2)

# integration using Simpson's rule
I2 = scipy.integrate.simps (data_y2, x=data_x2)

# printing result
print ("I2   =", I2)
print ("I2 should be 0.9973.")
