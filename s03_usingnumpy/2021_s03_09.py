#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:42:52 (CST) daisuke>
#

# importing numpy module
import numpy

# creating floating point arrays using linspace function

# making a numpy array of [0.0, 0.1, 0.2, ..., 5.0]
array_k = numpy.linspace (0, 5, 51)
print ("array_k:")
print (array_k)

# making a numpy array of [0.00, 0.025, 0.05, ..., 1.00]
array_l = numpy.linspace (0, 1, 41)
print ("array_l:")
print (array_l)

# making a numpy array of [0.000, 0.333, ..., 5.000]
array_m = numpy.linspace (0, 10, 31)
print ("array_m:")
print (array_m)
