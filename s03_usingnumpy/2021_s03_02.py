#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:42:33 (CST) daisuke>
#

# importing numpy module
import numpy

# making a numpy array
array_a = numpy.array ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# accessing to an element using an index
print ("array_a[5] =", array_a[5])

# one more example
print ("array_a[8] - array_a[2] =", array_a[8] - array_a[2])

# accessing to a part of the array using a slice
print ("array_a[2:7] =", array_a[2:7])
print ("array_a[:8]  =", array_a[:8])
print ("array_a[4:]  =", array_a[4:])
