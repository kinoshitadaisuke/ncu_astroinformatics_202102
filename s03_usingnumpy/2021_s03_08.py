#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:42:49 (CST) daisuke>
#

# importing numpy module
import numpy

# creating integer arrays using arange function

# making a numpy array of [0, 1, 2, 3, 4]
array_g = numpy.arange (5)
print ("array_g:")
print (array_g)

# making a numpy array of [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
array_h = numpy.arange (5, 15)
print ("array_h:")
print (array_h)

# making a numpy array of [0, 2, 4, 6, 8, 10, 12, 14]
array_i = numpy.arange (0, 15, 2)
print ("array_i:")
print (array_i)

# making a numpy array of [1, 4, 7, 10, 13, 16, 19]
array_j = numpy.arange (1, 20, 3)
print ("array_j:")
print (array_j)
