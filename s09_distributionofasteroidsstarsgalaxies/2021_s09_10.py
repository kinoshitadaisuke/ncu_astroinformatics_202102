#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:50:26 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astroquery module
import astroquery.mpc

# date
date_start = '2021-05-03'

# number of asteroids
n = 1000

# asteroid ephemerides
for i in range (1, n + 1, 1):
    # ephemeris from MPC
    eph = astroquery.mpc.MPC.get_ephemeris (i, start=date_start, \
                                            step='1d', number=1)

    # RA and Dec in radian
    ra_rad  = eph['RA'] / 180.0 * numpy.pi
    dec_rad = eph['Dec'] / 180.0 * numpy.pi

    # printing result
    print ("%8.6f %+9.6f %s %d" % (ra_rad, dec_rad, date_start, i) )
