#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:25 (CST) daisuke>
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

# moonrise
moonrise = lulin.moon_rise_time (time, which="nearest")

# moonset
moonset = lulin.moon_set_time (time, which="nearest")

# printing results
print ("moonrise time nearest to %s" % time)
print ("  JD = %s" % moonrise)
print ("     = %s" % moonrise.isot)
print ("moonset time nearest to %s" % time)
print ("  JD = %s" % moonset)
print ("     = %s" % moonset.isot)
