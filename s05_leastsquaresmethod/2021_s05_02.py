#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:44 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.stats

# parameters
n        = 10**6
data_min =   0.0
data_max = 100.0

# generation of a set of random numbers
data = numpy.random.uniform (data_min, data_max, n)

# printing generated random numbers
print ("data:")
print (data)

# calculating the mean manually
mean_manual = numpy.sum (data) / len (data)

# printing the mean calculated manually
print ("mean  =", mean_manual, "(calculated manually)")

# calculating the mean using numpy
mean_numpy = numpy.mean (data)

# printing the mean calculated by numpy
print ("mean  =", mean_numpy, "(calculated by numpy)")

# calculating the mean using scipy
mean_scipy = scipy.stats.tmean (data)

# printing the mean calculated by scipy
print ("mean  =", mean_scipy, "(calculated by scipy)")

# calculating the trimmed mean using scipy
tmean1 = scipy.stats.tmean (data, (20.0, 30.0))

# printing the trimmed mean calculated by scipy
print ("tmean =", tmean1, "(20.0 <= x <= 30.0)")

# calculating the trimmed mean using scipy
tmean2 = scipy.stats.tmean (data, (60.0, 70.0))

# printing the trimmed mean calculated by scipy
print ("tmean =", tmean2, "(60.0 <= x <= 70.0)")
