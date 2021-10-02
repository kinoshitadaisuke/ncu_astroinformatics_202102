#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:19 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.optimize

#
# constants
#

# speed of light
c = scipy.constants.c
# Planck constant
h = scipy.constants.h
# Boltzmann constant
k = scipy.constants.k

#
# parameters
#

# temperature in K
T = 5800.0

# function to minimize
def func (x):
    y = ( (x-5.0) * numpy.exp (x) + 5.0 )**2
    return (y)

# initial value of x
x0 = 5.0

# value of x
result = scipy.optimize.minimize (func, x0)
x = result['x'][0]
print ("x =", x)

# peak wavelength
wl_peak = h * c / (x * k * T)

# printing result
print ("peak of T = %f K blackbody: lambda_peak = %f nm" \
       % (T, wl_peak * 10**9) )
