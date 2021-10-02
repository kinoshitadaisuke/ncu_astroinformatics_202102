#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:11 (CST) daisuke>
#

# importing numpy array
import numpy

# catalogue file name
file_catalogue = 'bsc5.data'

# dictionary for storing data
stars = {}

# opening catalogue file
fh = open (file_catalogue, 'r')

# reading catalogue line-by-line
for line in fh:
    # Harvard Revised Number of star
    HR = line[0:4].strip ()
    # name
    name = line[4:14].strip ()
    # Vmag
    mag_V = line[102:107].strip ()
    # B-V colour
    colour_BV = line[109:114].strip ()
    # dynamical parallax flag
    dynamical_parallax = line[160].strip ()
    # spectral type
    sptype = line[127:147].strip ()
    # parallax
    parallax = line[161:166].strip ()

    # skip, if any of mag_V, colour_BV, parallax is missing
    if ( (mag_V == '') or (colour_BV == '') or (parallax == '') ):
        continue
    # skip, if parallax is negative
    if (parallax[0] == '-'):
        continue
    # skip, if parallax is dynamical parallax
    if (dynamical_parallax == 'D'):
        continue
    # reformat parallax
    if (parallax[:2] == '+.'):
        parallax = '+0.' + parallax[2:]

    # conversion from string to float
    mag_V     = float (mag_V)
    colour_BV = float (colour_BV)
    parallax  = float (parallax)

    # skip, if parallax is zero
    if (parallax < 10**-4):
        continue
    
    # distance in parsec
    dist_pc = 1.0 / parallax

    # absolute magnitude
    absmag_V = mag_V - 5.0 * numpy.log10 (dist_pc) + 5.0

    # constructing the dictionary
    stars[HR] = {}
    stars[HR]["mag_V"]     = mag_V
    stars[HR]["colour_BV"] = colour_BV
    stars[HR]["parallax"]  = parallax
    stars[HR]["dist_pc"]   = dist_pc
    stars[HR]["absmag_V"]  = absmag_V
    stars[HR]["sptype"]    = sptype
    stars[HR]["name"]      = name
    
# closing catalogue file
fh.close ()

# printing header
print ("# Vmag, (B-V), parallax, distance, absmag_V, sptype, HR, name")

# printing information of 1st mag stars
for key, value in sorted (stars.items (), key=lambda x: x[1]['mag_V']):
    if (stars[key]['mag_V'] >= 1.5):
        break
    print ("%+6.3f,%+6.3f,%+6.3f,%8.3f,%+6.3f,%20s,%4s,%s" \
           % (stars[key]['mag_V'], stars[key]['colour_BV'], \
              stars[key]['parallax'], stars[key]['dist_pc'], \
              stars[key]['absmag_V'], stars[key]['sptype'], \
              key, stars[key]['name']) )
