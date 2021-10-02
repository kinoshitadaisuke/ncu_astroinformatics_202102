#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:19 (CST) daisuke>
#

# importing math module
import math

# importing numpy
import numpy

# importing astropy module
import astropy.time
import astropy.units

# parameters

# amplitude (mag)
A = 0.25

# period (day)
P = 7.5 / 24

# phase
delta = 2.0 * math.pi * 0.30

# average magnitude
c = 19.0

# observable time
start_night = (20 - 8) / 24.0 # 12:00 UT
end_night   = (28 - 8) / 24.0 # 20:00 UT

# time for calibration data
start_calib = (24 - 8) / 24.0 # 16:00 UT
end_calib   = (25 - 8) / 24.0 # 17:00 UT

# start of observation
start_date = '2021-05-10T12:00:00'
start_t = astropy.time.Time (start_date, scale='utc')
start_mjd = start_t.mjd

# end of observation
end_date = '2021-05-13T20:00:00'
end_t = astropy.time.Time (end_date, scale='utc')
end_mjd = end_t.mjd

# exposure time (sec)
exptime = 180.0

# overhead time (sec)
overhead = 30.0

# interval between exposures (sec)
interval = exptime + overhead

# error
mean  = 0.0
sigma = 0.03

print ("# start of obs. =", start_date, "= MJD", start_mjd)
print ("# end of obs.   =", end_date, "= MJD", end_mjd)
print ("# amplitude =", A, "mag")
print ("# period =", P, "day")
print ("# delta =", delta)
print ("# average mag =", c, "mag")
print ("# exposure time =", exptime, "sec")
print ("# overhead =", overhead, "sec")

# sine curve
def func (x, A, P, delta, c):
    y = A * math.sin (2.0 * math.pi * x / P + delta) + c
    return (y)

# printing header
print ("#")
print ("# date/time, MJD, mag")
print ("#")

# generation of a synthetic time-series data
t = start_t
while (t < end_t):
    # MJD
    mjd = t.mjd
    fractional_day = mjd - int (mjd)
    # apparent magnitude
    mag = func (mjd, A, P, delta, c) + numpy.random.normal (mean, sigma)
    # error
    err = numpy.random.normal (mean, sigma)
    # printing data
    if ( ( (fractional_day >= start_night) \
           and (fractional_day <= end_night) ) \
         and ( (fractional_day < start_calib) \
               or (fractional_day > end_calib) ) ):
        print ("%s %f %f %f" % (t, mjd, mag, abs (err) ) )
    # calculation of time of next exposure
    t += (interval + numpy.random.uniform (0.0, 60.0) ) * astropy.units.second
