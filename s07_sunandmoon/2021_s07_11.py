#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:19 (CST) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units
import astropy.coordinates

# units
unit_m = astropy.units.m

# Lulin observatory
lulin_lon = "+120d52m25s"
lulin_lat = "+23d28m07s"
lulin_elev = 2862 * unit_m

# location object
location = astropy.coordinates.EarthLocation.from_geodetic \
    (lulin_lon, lulin_lat, lulin_elev)

# date/time
time_str = "2021-04-19T12:00:00"
time     = astropy.time.Time (time_str)

# printing location and date/time
print ("Location:")
print ("  lon  = \"%s\"" % lulin_lon)
print ("  lat  = \"%s\"" % lulin_lat)
print ("  elev = %s" % lulin_elev)
print ("Date/Time:")
print ("  date/time = \"%s\"" % time)

# using DE430
astropy.coordinates.solar_system_ephemeris.set ('de430')

# position of the Moon
moon = astropy.coordinates.get_body ('moon', time, location)
(moon_ra, moon_dec) = moon.to_string ('hmsdms').split ()

# printing position of the Moon
print ("Moon:")
print ("  RA:  %s" % moon_ra)
print ("  Dec: %s" % moon_dec)
