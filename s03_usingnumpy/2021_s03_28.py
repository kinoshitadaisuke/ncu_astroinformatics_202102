#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:44:02 (CST) daisuke>
#

# importing numpy module
import numpy

# parameters
n = 10**7
a = 2.0
b1 = 2.0
b2 = 5.0

# initialising random number generator
numpy.random.seed ()

# generating a set of random numbers of beta distribution
data1 = numpy.random.beta (a, b1, n)
data2 = numpy.random.beta (a, b2, n)

# sorting
data1_sorted = numpy.sort (data1)
data2_sorted = numpy.sort (data2)

# median
if (n % 2 == 0):
    median1 = (data1_sorted[int(n/2)] + data1_sorted[int(n/2)-1]) / 2.0
    median2 = (data2_sorted[int(n/2)] + data2_sorted[int(n/2)-1]) / 2.0
else:
    median1 = data1_sorted[int(n/2)]
    median2 = data2_sorted[int(n/2)]

# printing results
print ("beta distribution (a=%f, b=%f):" % (a, b1) )
print ("  ", data1)
print ("  ", data1_sorted)
print ("  median =", median1)
print ("beta distribution (a=%f, b=%f):" % (a, b2) )
print ("  ", data2)
print ("  ", data2_sorted)
print ("  median =", median2)
