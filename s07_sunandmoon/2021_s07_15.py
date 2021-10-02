#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:30 (CST) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units
import astropy.coordinates

# importing astroplan module
import astroplan

# units
unit_m = astropy.units.m

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

# date/time
time_str = "2021-04-19T14:30:00"
time     = astropy.time.Time (time_str)

# printing location and date/time
print ("Location:")
print ("  lon  = \"%s\"" % lulin_lon)
print ("  lat  = \"%s\"" % lulin_lat)
print ("  elev = %s" % lulin_elev)
print ("Date/Time:")
print ("  date/time = \"%s\"" % time)

# target
object_name = 'Acrux'
obj = astroplan.FixedTarget.from_name (object_name)

# alt and az of target
obj_altaz = lulin.altaz (time, obj)

# printing results
print ("Object = %s" % object_name)
print ("  Az:  %s" % obj_altaz.az)
print ("  Alt: %s" % obj_altaz.alt)
print ("  airmass: %s" % obj_altaz.secz)
