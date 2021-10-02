#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:42:41 (CST) daisuke>
#

# importing numpy module
import numpy

# making a numpy array
array_c = numpy.array ([ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0] ])

# printing numpy array information
print ("array_c:")
print (array_c)
print ("ndim     =", array_c.ndim)
print ("shape    =", array_c.shape)
print ("size     =", array_c.size)
print ("dtype    =", array_c.dtype)
print ("itemsize =", array_c.itemsize)
print ("data     =", array_c.data)
