#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:32 (CST) daisuke>
#

# importing numpy module
import numpy

#
# Numpy 1.17 has a new random number generator.
# If you are using Numpy 1.17 or newer, read the official document
# for the usage of new generator.
#
# https://docs.scipy.org/doc/numpy-1.17.0/reference/random/index.html
#
# Following code is based on the legacy generator.
#

# initialisation of random number generator
numpy.random.seed ()

# generation of a random number
r1 = numpy.random.random ()
print (r1)
r2 = numpy.random.random ()
print (r2)
r3 = numpy.random.random ()
print (r3)

# generation of a set of random numbers between 0 and 1
r4 = numpy.random.random (10)
print ("Random number generation using numpy.random.random:")
print (r4)

# generation of a set of random numbers of uniform distribution
# between n_min and n_max
n_min = 10
n_max = 20
r5 = numpy.random.uniform (n_min, n_max, 10)
print ("Random number generation using numpy.random.uniform:")
print (r5)

# generation of a set of random numbers of Gaussian distribution
mean   = 50.0
stddev = 10.0
r6 = numpy.random.normal (mean, stddev, 10)
print ("Random number generation using numpy.random.normal:")
print (r6)
