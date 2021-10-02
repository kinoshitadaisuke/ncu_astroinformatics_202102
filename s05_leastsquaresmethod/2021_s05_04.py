#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:50 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.linalg

# matrix
A = numpy.array ( [ [4.0, 7.0], [3.0, 5.0] ] )

# printing matrix A
print ("matrix A:")
print (A)

# determinant of matrix A
A_det = scipy.linalg.det (A)

# printing the determinant of matrix A
print ("determinant of matrix A =", A_det)

# inverse of matrix A
A_inv = scipy.linalg.inv (A)

# printing inverse of matrix A
print ("A^{-1}:")
print (A_inv)

# eigenvalues of matrix A
eigenvalues = scipy.linalg.eigvals (A)

# printing eigenvalues of matrix A
print ("eigenvalues of matrix A =", eigenvalues)

# eigenvalues and eigenvectors of matrix A
eigenvalvec = scipy.linalg.eig (A)
print ("eigenvalues of matrix A:")
print (eigenvalvec[0])
print ("eigenvectors of matrix A:")
print (eigenvalvec[1])
