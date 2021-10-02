#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:50:54 (CST) daisuke>
#

# importing math module
import math

# importing astropy module
import astropy.time
import astropy.units

# parameters

# amplitude (mag)
A = 0.3

# period (day)
P = 2.0 / 24

# phase
delta = 2.0 * math.pi * 0.20

# average magnitude
c = 16.0

# start of observation
start_date = '2021-05-10T12:00:00'
start_t    = astropy.time.Time (start_date, scale='utc')
start_mjd  = start_t.mjd

# end of observation
end_date = '2021-05-10T20:00:00'
end_t    = astropy.time.Time (end_date, scale='utc')
end_mjd  = end_t.mjd

# exposure time (sec)
exptime = 180.0

# overhead time (sec)
overhead = 30.0

# interval between exposures (sec)
interval = exptime + overhead

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
    # apparent magnitude
    mag = func (mjd, A, P, delta, c)
    # printing data
    print ("%s %f %f" % (t, mjd, mag) )
    # calculation of time of next exposure
    t += interval * astropy.units.second
