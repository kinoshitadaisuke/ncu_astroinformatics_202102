#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:59 (CST) daisuke>
#

# importing numpy module
import numpy

# parameters
n = 10**6
data_min =   0.0
data_max = 100.0

# initialisation of random number generator
numpy.random.seed ()

# generation of a set of random numbers
a = numpy.random.uniform (data_min, data_max, n)
print ("a =", a)

# sorting
# .sort () method sorts an array in-place.
a.sort ()
print ("a =", a)
