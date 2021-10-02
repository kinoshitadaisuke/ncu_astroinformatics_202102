#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:42:44 (CST) daisuke>
#

# importing numpy module
import numpy

# making a numpy array
array_c = numpy.array ([ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0] ])

# accessing elements using indexing and slicing
print ("array_c:")
print (array_c)
print ("array_c[1,2] =", array_c[1,2])
print ("array_c[2,0] =", array_c[2,0])
print ("array_c[1,:] =", array_c[1,:])
print ("array_c[:,2] =", array_c[:,2])
print ("array_c[0:2,1:]:")
print (array_c[0:2,1:])
