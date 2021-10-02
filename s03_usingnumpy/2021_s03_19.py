#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:25 (CST) daisuke>
#

# importing numpy module
import numpy

# a sample dataset
a = numpy.array ([0.123, -4.567, 8.901, -23.456, 78.901])
print ("a =", a)

# round
b = numpy.round (a)
print ("b =", b)

c = numpy.round (a, decimals=1)
print ("c =", c)

d = numpy.round (a, decimals=2)
print ("d =", d)

# floor
e = numpy.floor (a)
print ("e =", e)
