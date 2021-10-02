#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:22 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array "a"
a = numpy.linspace (-3, 3, 7)
print ("a =", a)

# calculating 10**a
b = 10**a
print ("b = 10**a =", b)

# calculating log10(b)
c = numpy.log10 (b)
print ("c = log10(b) =", c)

# making a Numpy array "d"
d = numpy.linspace (1, 5, 9)
print ("d =", d)

# calculating exp(d)
e = numpy.exp (d)
print ("e = exp(d) =", e)

# calculating log(e)
f = numpy.log (e)
print ("f = log(e) =", f)

# calculating sqrt(f)
g = numpy.sqrt (f)
print ("g = sqrt(f) =", g)

