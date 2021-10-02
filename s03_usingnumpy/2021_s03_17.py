#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:43:20 (CST) daisuke>
#

# importing numpy module
import numpy

# angles in deg
angle_deg = numpy.linspace (0.0, 360.0, 13)

# angles in rad
angle_rad = numpy.radians (angle_deg)

# sin (angle_rad)
data_sin = numpy.sin (angle_rad)

# cos (angle_rad)
data_cos = numpy.cos (angle_rad)

# printing header
print ("%3s  %8s  %8s  %8s" % ("deg", "rad", "sin", "cos") )

# printing data
for i in range ( len (angle_deg) ):
    print ("%3d  %8.5f  %8.5f  %8.5f" \
           % (angle_deg[i], angle_rad[i], data_sin[i], data_cos[i]) )
