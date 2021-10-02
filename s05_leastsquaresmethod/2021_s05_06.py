#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:55 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# function
f1 = lambda x: numpy.cos (x)

# lower limit and upper limit of integration
a1 = 0.0
b1 = numpy.pi * 0.5

# integration
result1 = scipy.integrate.quad (f1, a1, b1)

# printing result
print ("result 1: ", result1[0], "+/-", result1[1])

# function
f2 = lambda x: numpy.exp (-1.0 * x**2)

# lower limit and upper limit of integration
a2 = numpy.NINF
b2 = numpy.inf

# integration
result2 = scipy.integrate.quad (f2, a2, b2)

# printing result
print ("result 2: ", result2[0], "+/-", result2[1])
print ("sqrt(pi) =", numpy.sqrt (numpy.pi))
