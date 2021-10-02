#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:29 (CST) daisuke>
#

# importing numpy module
import numpy

# a sample dataset
data = numpy.array ([1.2, 3.4, 5.6, 7.8, 9.0, 12.3, 45.6])
print ("data =", data)

# manually calculating the sum
sum0 = 0.0
for datum in data:
    sum0 += datum
print ("sum0 =", sum0)

# using function "sum"
sum1 = numpy.sum (data)
print ("sum1 =", sum1)

# a different way to calculate the sum using "sum" method
sum2 = data.sum ()
print ("sum2 =", sum2)
