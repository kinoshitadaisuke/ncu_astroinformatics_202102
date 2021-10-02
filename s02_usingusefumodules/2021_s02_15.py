#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:29 (CST) daisuke>
#

# importing numpy module
import numpy

# array A
A = numpy.array ( [ [1, 3], [2, 4] ] )

# array B
B = numpy.array ( [ [7, 8], [5, 6] ] )

# calculation of matrix product
C = A @ B

print ("Matrix A:")
print (A)
print ("Matrix B:")
print (B)
print ("Matrix C:")
print (C)
