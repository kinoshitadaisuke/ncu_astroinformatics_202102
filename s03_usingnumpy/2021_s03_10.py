#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:42:55 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array using linspace
a = numpy.linspace (10.0, 100.0, 10)

# printing Numpy array a
print ("a =", a)

# scalar b
b = 5.0

# c = a - b
c = a - b

# printing Numpy array c
print ("b =", b)
print ("c = a - b =", c)

# scalar d
d = 5.0

# e = c / d
e = c / d

# printing Numpy array e
print ("d =", d)
print ("e = c / d =", e)
