#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:50 (CST) daisuke>
#

# importing numpy module
import numpy

# data
data = numpy.array ([10.0, 9.9, 10.1, 9.8, 10.2, 9.7, 10.3, 12.0, 13.0])

# errors
err = numpy.array ([0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 3.0, 3.0])

# printing data and errors
print ("data =", data)
print ("err  =", err)

# calculation of simple average
average_simple = numpy.mean (data)

# calculation of weighted average
average_weighted = numpy.average (data, weights=1.0/err)

# printing results
print ("simple average: %f" % average_simple)
print ("weighted average: %f" % average_weighted)
