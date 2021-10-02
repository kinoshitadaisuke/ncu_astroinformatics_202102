#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:16 (CST) daisuke>
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
    "2021-01-15T00:00:00",
    "2021-02-15T00:00:00",
    "2021-03-15T00:00:00",
    "2021-04-15T00:00:00",
    "2021-05-15T00:00:00",
    "2021-06-15T00:00:00",
    "2021-07-15T00:00:00",
    "2021-08-15T00:00:00",
    "2021-09-15T00:00:00",
    "2021-10-15T00:00:00",
    "2021-11-15T00:00:00",
    "2021-12-15T00:00:00",
    ]
time = astropy.time.Time (list_time)

# Royal Observatory Greenwich in UK
greenwich_lon = "+00d00m02s"
greenwich_lat = "+51d28m37s"
greenwich_elev = 47 * unit_m

# location object
location = astropy.coordinates.EarthLocation.from_geodetic \
    (greenwich_lon, greenwich_lat, greenwich_elev)

# observer object
greenwich = astroplan.Observer (location=location, name="Greenwich", \
                                timezone="Europe/London")

# end of twilight
twilight_astronomical_end = greenwich.twilight_evening_astronomical \
    (time, which="nearest")

# start of twilight
twilight_astronomical_start = greenwich.twilight_morning_astronomical \
    (time, which="nearest")

# time between end of evening twilight and start of morning twilight
obs_time = twilight_astronomical_start.mjd - twilight_astronomical_end.mjd

# printing results
for i in range ( len (obs_time) ):
    date = time[i].ymdhms
    print ("length of observable time on %04d-%02d-%02d = %4.1f hours" \
           % (date['year'], date['month'], date['day'], obs_time[i] * 24) )
