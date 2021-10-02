#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:13 (CST) daisuke>
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

# end of twilight
twilight_astronomical_end = lulin.twilight_evening_astronomical \
    (time, which="nearest")

# start of twilight
twilight_astronomical_start = lulin.twilight_morning_astronomical \
    (time, which="nearest")

# time between end of evening twilight and start of morning twilight
obs_time = twilight_astronomical_start.mjd - twilight_astronomical_end.mjd

# printing results
for i in range ( len (obs_time) ):
    date = time[i].ymdhms
    print ("length of observable time on %04d-%02d-%02d = %4.1f hours" \
           % (date['year'], date['month'], date['day'], obs_time[i] * 24) )
