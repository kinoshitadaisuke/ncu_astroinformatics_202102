#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:45 (CST) daisuke>
#

# importing numpy module
import numpy

# parameters
# number of random numbers to be generated
n = 10**6
# mean
mean = 50.0
# standard deviation
stddev = 10.0

# initialisation of random number generator
numpy.random.seed ()

# generation of a set of random numbers
data = numpy.random.normal (mean, stddev, n)
print ("number of data = %g" % len (data))
print ("data =", data)

# maximum value
data_max = numpy.amax (data)
print ("maximum value =", data_max)

# minimum value
data_min = numpy.amin (data)
print ("minimum value =", data_min)

# percentile
p00135 = numpy.percentile (data,  0.135)
p02275 = numpy.percentile (data,  2.275)
p15865 = numpy.percentile (data, 15.865)
p50000 = numpy.percentile (data, 50.000)
p84135 = numpy.percentile (data, 84.135)
p97725 = numpy.percentile (data, 97.725)
p99865 = numpy.percentile (data, 99.865)
print ("p00135 =", p00135)
print ("p02275 =", p02275)
print ("p15865 =", p15865)
print ("p50000 =", p50000)
print ("p84135 =", p84135)
print ("p97725 =", p97725)
print ("p99865 =", p99865)

# the other way to calculate mean, variance, and standard deviation
data_mean   = data.mean ()
data_median = numpy.median (data)
data_var    = data.var ()
data_std    = data.std ()
print ("mean     =", data_mean)
print ("median   =", data_median)
print ("variance =", data_var)
print ("stddev   =", data_std)
