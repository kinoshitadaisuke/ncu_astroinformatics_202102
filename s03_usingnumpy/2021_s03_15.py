#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:11 (CST) daisuke>
#

# importing numpy module
import numpy

# creating a matrix A
A = numpy.array ( [ [5.0, 3.0], [6.0, 4.0] ] )

# printing matrix A
print ("matrix A:")
print (A)

# calculating inverse matrix of A
A_inv = numpy.linalg.inv (A)

# printing inverse matrix of A
print ("inverse matrix of A:")
print ("matrix A^-1:")
print (A_inv)

# calculation of A * A^-1
print ("matrix B:")
print ("B = A @ A^-1")
B = numpy.matmul (A, A_inv)
print (B)
