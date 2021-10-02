#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:33 (CST) daisuke>
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
time_str = "2021-04-19T16:00:00"
time     = astropy.time.Time (time_str)
date     = time.ymdhms

# printing location and date/time
print ("Location:")
print ("  lon  = \"%s\"" % lulin_lon)
print ("  lat  = \"%s\"" % lulin_lat)
print ("  elev = %s" % lulin_elev)
print ("Date/Time:")
print ("  date/time = \"%s\"" % time)

# target
object_name = 'Arcturus'
obj = astroplan.FixedTarget.from_name (object_name)

# rise time
time_rise = lulin.target_rise_time (time, obj, which="nearest")

# set time
time_set = lulin.target_set_time (time, obj, which="nearest")

# printing results
print ("rise and set of %s on %04d-%02d-%02d:" \
       % (object_name, date['year'], date['month'], date['day']) )
print ("  rise time: %s" % time_rise.isot)
print ("  set time:  %s" % time_set.isot)
