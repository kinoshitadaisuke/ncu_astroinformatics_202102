#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:46 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.stats

# parameters
n      = 10**6
mean   = 50.0
stddev = 10.0
limits = (35.0, 65.0)

# generation of a set of random numbers
data = numpy.random.normal (mean, stddev, n)

# printing generated random numbers
print ("data:")
print (data)

# calculating the standard deviation using numpy
stddev_numpy = numpy.std (data)

# printing the standard deviation calculated by numpy
print ("stddev  =", stddev_numpy, "(calculated by numpy)")

# calculating the mean using scipy
stddev_scipy = scipy.stats.tstd (data)

# printing the mean calculated by scipy
print ("stddev  =", stddev_scipy, "(calculated by scipy)")

# calculating the trimmed standard deviation using scipy
tstddev = scipy.stats.tstd (data, limits)

# printing the trimmed standard deviation calculated by scipy
print ("tstddev = %f (%f <= x <= %f)" % (tstddev, limits[0], limits[1]) )
