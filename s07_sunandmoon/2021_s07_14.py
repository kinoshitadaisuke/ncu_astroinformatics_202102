#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:27 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units
import astropy.coordinates

# importing astroplan module
import astroplan

# units
unit_m   = astropy.units.m
unit_rad = astropy.units.rad
unit_deg = astropy.units.deg

# time
time_str = [
    "2021-04-12T12:00:00",
    "2021-04-19T12:00:00",
    "2021-04-26T12:00:00",
    "2021-05-03T12:00:00",
    ]
time = astropy.time.Time (time_str)

# Lulin observatory
lulin_lon = "+120d52m25s"
lulin_lat = "+23d28m07s"
lulin_elev = 2862 * unit_m

# location object
location = astropy.coordinates.EarthLocation.from_geodetic \
    (lulin_lon, lulin_lat, lulin_elev)

# observer object
lulin = astroplan.Observer (location=location, name="Lulin", \
                            timezone="Asia/Taipei")

# illumination
illumination = lulin.moon_illumination (time)

# moon phase
phase = lulin.moon_phase (time)

# printing results
for i in range ( len (phase) ):
    print ("Moon on %s" % time[i])
    print ("  illumination = %f" % illumination[i])
    print ("  moon phase = %s = %s" % (phase[i], \
           phase[i] / numpy.pi * 180 / unit_rad * unit_deg) )
