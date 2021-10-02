#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:01 (CST) daisuke>
#

# importing numpy module
import numpy

# making numpy arrays
a = numpy.array ([1.0, 3.0])
b = numpy.array ([4.0, 2.0])

# printing vectors "a" and "b"
print ("a =", a)
print ("b =", b)

# dot product of vectors
c = numpy.dot (a, b)
print ("dot product of vectors:")
print ("  c = numpy.dot (a, b) =", c)

# inner product of vectors
d = numpy.inner (a, b)
print ("inner product of vectors:")
print ("  d = numpy.inner (a, b) =", d)

# cross product of vectors
e = numpy.array ([1.0, 0.0, 0.0])
f = numpy.array ([0.0, 1.0, 0.0])
g = numpy.cross (e, f)
print ("cross product of vectors:")
print ("  e =", e)
print ("  f =", f)
print ("  g = numpy.cross (e, f) =", g)
