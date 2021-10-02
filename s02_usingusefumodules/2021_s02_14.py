#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:26 (CST) daisuke>
#

# importing numpy module
import numpy

# initializing numpy array a
a = numpy.array ([1.2, 3.4, 5.6, 7.8, 9.0, 12.3])
print ("a =", a)

# initializing numpy array b
b = numpy.zeros (6)
for i in (range (6)):
    b[i] = i + 1
print ("b =", b)

# calculation of c = a * b
c = a * b

# printing result
print ("c = a * b =", c)
