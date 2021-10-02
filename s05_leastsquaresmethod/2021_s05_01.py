#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:40 (CST) daisuke>
#

# importing scipy module
import scipy
import scipy.constants

# important constants
pi    = scipy.constants.pi
c     = scipy.constants.c
h     = scipy.constants.h
G     = scipy.constants.G
k     = scipy.constants.k
sigma = scipy.constants.sigma

# printing some mathematical and physical constants

# pi
print ("# pi")
print ("pi = %16.14f" % pi)

# c
print ("# speed of light")
print ("c = %G" % c)

# h
print ("# Planck constant")
print ("h = %G" % h)

# G
print ("# gravitational constant")
print ("G = %G" % G)

# k
print ("# Boltzmann constant")
print ("k = %G" % k)

# Stefan-Boltzmann constant
print ("# Stefan-Boltzmann constant")
print ("sigma = %G" % sigma)
