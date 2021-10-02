#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:05 (CST) daisuke>
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
list_time = [
    "2021-01-15T16:00:00",
    "2021-02-15T16:00:00",
    "2021-03-15T16:00:00",
    "2021-04-15T16:00:00",
    "2021-05-15T16:00:00",
    "2021-06-15T16:00:00",
    "2021-07-15T16:00:00",
    "2021-08-15T16:00:00",
    "2021-09-15T16:00:00",
    "2021-10-15T16:00:00",
    "2021-11-15T16:00:00",
    "2021-12-15T16:00:00",
    ]
time = astropy.time.Time (list_time)

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

# sunset
sunset = lulin.sun_set_time (time, which="nearest")

# sunrise
sunrise = lulin.sun_rise_time (time, which="nearest")

# length of night
length_night = sunrise.mjd - sunset.mjd

# printing results
for i in range ( len (length_night) ):
    date = time[i].ymdhms
    print ("length of nighttime on %04d-%02d-%02d = %4.1f hours" \
           % (date['year'], date['month'], date['day'], length_night[i] * 24) )
