#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:45 (CST) daisuke>
#

# importing math module
import math

# log (10)
a = math.log (10)
print ("log (10) =", a)

# exp (10)
b = math.exp (10)
print ("exp (10) =", b)
c = math.log (b)
print ("log (", b, ") =", c)

# log10 (1000)
d = math.log10 (1000)
print ("log10 (1000) =", d)

# pow (3, 4)
e = math.pow (3, 4)
print ("pow (3, 4)   =", e)

# sqrt (3)
f = math.sqrt (3)
print ("sqrt (3)     =", f)

# sin (45 deg)
g_deg = 45.0
g_rad = g_deg / 180.0 * math.pi
sin_g = math.sin (g_rad)
print ("sin (45 deg) =", sin_g)
print ("sqrt(2)/2    =", math.sqrt(2) / 2.0)

# cos (30 deg)
h_deg = 30.0
h_rad = h_deg / 180.0 * math.pi
cos_h = math.cos (h_rad)
print ("cos (30 deg) =", cos_h)
print ("sqrt(3)/2    =", math.sqrt(3) / 2.0)
