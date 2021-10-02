#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:11 (CST) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units
import astropy.coordinates

# importing astroplan module
import astroplan

# units
unit_m = astropy.units.m

# time
time_str = "2021-04-19T16:00:00"
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

# end of twilight
twilight_civil_end        = lulin.twilight_evening_civil \
    (time, which="nearest")
twilight_nautical_end     = lulin.twilight_evening_nautical \
    (time, which="nearest")
twilight_astronomical_end = lulin.twilight_evening_astronomical \
    (time, which="nearest")

# start of twilight
twilight_civil_start        = lulin.twilight_morning_civil \
    (time, which="nearest")
twilight_nautical_start     = lulin.twilight_morning_nautical \
    (time, which="nearest")
twilight_astronomical_start = lulin.twilight_morning_astronomical \
    (time, which="nearest")

# printing results
print ("end of evening twilight nearest to %s" % time)
print ("  civil twilight:        %s" % twilight_civil_end.isot)
print ("  nautical twilight:     %s" % twilight_nautical_end.isot)
print ("  astronomical twilight: %s" % twilight_astronomical_end.isot)
print ("start of morning twilight nearest to %s" % time)
print ("  civil twilight:        %s" % twilight_civil_start.isot)
print ("  nautical twilight:     %s" % twilight_nautical_start.isot)
print ("  astronomical twilight: %s" % twilight_astronomical_start.isot)
