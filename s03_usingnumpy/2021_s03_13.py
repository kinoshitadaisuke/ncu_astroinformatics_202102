#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:05 (CST) daisuke>
#

# importing numpy module
import numpy

# creating a matrix A
A = numpy.array ( [ [1, 2], [3, 4] ] )
# creating a matrix B
B = numpy.array ( [ [4, 2], [1, 3] ] )

# printing matrix A and B
print ("matrix A:")
print (A)
print ("matrix B:")
print (B)

# this is probably not what you expect...
C = A * B
print ("matrix C:")
print ("C = A * B")
print (C)

# matrix product
D = A @ B
print ("matrix D:")
print ("D = A @ B")
print (D)

# different way to get matrix product
E = A.dot (B)
print ("matrix E:")
print ("E = A.dot (B)")
print (E)

# one more way to get matrix product
F = numpy.matmul (A, B)
print ("matrix F:")
print ("F = numpy.matmul (A, B)")
print (F)
