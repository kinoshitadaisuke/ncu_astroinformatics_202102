#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:47:55 (CST) daisuke>
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

# target
list_target = [
    "Canopus",
    "Betelgeuse",
    "Sirius",
    "Spica",
    "Vega",
    "Antares",
    "Fomalhaut",
    "Polaris",
    ]

# time
list_time = [
    "2021-01-01T12:00:00",
    "2021-04-01T12:00:00",
    "2021-07-01T12:00:00",
    "2021-11-01T12:00:00",
    ]

# checking visibility of targets
for time_str in list_time:
    # time object
    time = astropy.time.Time (time_str)
    print ("Visibility of targets at Lulin on %s:" % time)
    for target in list_target:
        # getting object from name
        obj = astroplan.FixedTarget.from_name (target)
        # checking visibility of the object
        visibility = lulin.target_is_up (time, obj)
        # printing result
        print ("  %10s ==> %s" % (target, visibility) )
