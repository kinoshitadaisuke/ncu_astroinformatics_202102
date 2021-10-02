#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:54 (CST) daisuke>
#

# importing numpy module
import numpy

# parameters
# number of random numbers to be generated
n = 10**7
# mean
mean = 50.0
# standard deviation
stddev = 10.0

# initialisation of random number generator
numpy.random.seed ()

# generation of a set of random numbers
data = numpy.random.normal (mean, stddev, n)
print ("number of data = %g" % len (data))
print ("data =", data)

# maximum value
data_max = data.min ()
print ("maximum value =", data_max)

# minimum value
data_min = data.max ()
print ("minimum value =", data_min)
