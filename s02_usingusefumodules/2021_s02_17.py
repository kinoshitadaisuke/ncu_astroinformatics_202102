#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:36 (CST) daisuke>
#

# importing astropy module
import astropy
import astropy.time

# J2000
j2000 = '2000-01-01T12:00:00.000'
time_j2000 = astropy.time.Time (j2000, scale='utc')
print ("calendar date (UT) =", time_j2000)
print ("  JD  = %16.8f" % time_j2000.jd)
print ("  MJD = %16.8f" % time_j2000.mjd)

# getting the current time
time_now = astropy.time.Time.now ()
print ("calendar date (UT) =", time_now)
print ("  JD  = %16.8f" % time_now.jd)
print ("  MJD = %16.8f" % time_now.mjd)
