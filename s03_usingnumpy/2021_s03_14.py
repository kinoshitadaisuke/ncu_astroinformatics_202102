#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:08 (CST) daisuke>
#

# importing numpy module
import numpy

# making a unit matrix
E2 = numpy.identity (2)
print ("E2:")
print (E2)

# making 3x3 unit matrix
E3 = numpy.identity (3)
print ("E3:")
print (E3)

# matrix A
A = numpy.array ( [ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0] ] )

# printing matrix A
print ("A:")
print (A)

# B = A * E3
B = A @ E3

# printing matrix A
print ("B = A @ E3:")
print (B)
