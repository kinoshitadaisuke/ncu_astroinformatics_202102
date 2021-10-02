#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:48 (CST) daisuke>
#

# importing math module
import math

# pi
pi = math.pi
print ("pi   =", pi)

# e
e = math.e
print ("e    =", e)

# 2 pi
tau = math.tau
print ("tau  =", tau)
print ("2*pi =", 2.0 * pi)

# conversion from deg to rad
a_deg = 90.0
a_rad = math.radians (a_deg)
print ("a    =", a_deg, "deg")
print ("     =", a_rad, "rad")

# conversion from rad to deg
b_rad = pi
b_deg = math.degrees (b_rad)
print ("b    =", b_rad, "rad")
print ("     =", b_deg, "deg")
