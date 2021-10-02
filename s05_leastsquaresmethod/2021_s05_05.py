#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:53 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.interpolate

# data
data_x = numpy.linspace (0.0, 10.0, 11)
data_y = 3.0 * data_x + 2.0

# printing data
print ("data_x =", data_x)
print ("data_y =", data_y)

# making interpolation function
i_func = scipy.interpolate.interp1d (data_x, data_y)

# interpolation
x1 = 2.5
y1 = i_func (x1)

# printing result
print ("using interpolation: x1 =", x1, "==>", "y1 =", y1)
print ("y1 should be y1 = 3.0 * %3.1f + 2.0 = %4.1f" % (x1, 3.0 * x1 + 2.0) )

# one more
x2 = 3.75
y2 = i_func (x2)

# printing result
print ("using interpolation: x2 =", x2, "==>", "y2 =", y2)
print ("y2 should be y1 = 3.0 * %4.2f + 2.0 = %5.2f" % (x2, 3.0 * x2 + 2.0) )
