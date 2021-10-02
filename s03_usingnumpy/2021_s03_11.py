#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:42:58 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using linspace
a = numpy.linspace (10.0, 55.0, 10)
b = numpy.linspace (15.0, 10.5, 10)

# printing Numpy arrays a and b
print ("a =", a)
print ("b =", b)

# calculation
c = a * b

# printing Numpy array c
print ("c = a * b =", c)

# making Numpy array using linspace
d = numpy.linspace (1.1, 2.0, 10)
print ("d =", d)

# calculation
e = c / d

# printing Numpy array e
print ("e = c / d =", e)
