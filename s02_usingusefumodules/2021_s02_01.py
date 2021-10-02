#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:42 (CST) daisuke>
#

# importing math module
import math

# pi
pi = math.pi
print ("pi     = %f" % pi)

#
# a_deg = 60.0 deg
#
a_deg = 60.0
print ("a      = %f deg" % a_deg)
#
# a_rad = 60.0 / 180.0 * pi rad
#
a_rad = a_deg / 180.0 * pi
print ("a      = %f rad" % a_rad)

# sin(a)
sin_a = math.sin (a_rad)
print ("sin(a) = %f" % sin_a)
# cos(a)
cos_a = math.cos (a_rad)
print ("cos(a) = %f" % cos_a)
# tan(a)
tan_a = math.tan (a_rad)
print ("tan(a) = %f" % tan_a)
