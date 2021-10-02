#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:57 (CST) daisuke>
#

# importing numpy module
import numpy

# parameters
n = 10**6
data_min =   0.0
data_max = 100.0

# initialisation of random number generator
numpy.random.seed ()

# generation of a set of random numbers
a = numpy.random.uniform (data_min, data_max, n)
print ("a =", a)

# sorting
b = numpy.sort (a)
print ("b =", b)

for i in range (10):
    j = int (n / 10 * i)
    print ("a[%06d] = %8.5f,   b[%06d] = %8.5f" % (j, a[j], j, b[j]) )
