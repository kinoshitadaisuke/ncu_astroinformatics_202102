#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:47:52 (CST) daisuke>
#

# importing astropy module
import astropy.units
import astropy.time
import astropy.coordinates

# importing astroplan module
import astroplan

# units
unit_m = astropy.units.m

# location of observing site
ncu_lon  = "+121d11m12s"
ncu_lat  = "+24d58m12s"
ncu_elev = 151.6 * unit_m

# printing location
print ("Location:")
print ("  longitude =", ncu_lon)
print ("  latitude  =", ncu_lat)
print ("  elevation =", ncu_elev)

# location object
location = astropy.coordinates.EarthLocation.from_geodetic \
    (ncu_lon, ncu_lat, ncu_elev)

# observer object
ncu = astroplan.Observer (location=location, name="NCU Main Campus", \
                          timezone="Asia/Taipei")

# time
list_time_str = [
    "2020-04-19T09:00:00",
    "2020-04-19T10:00:00",
    "2020-04-19T11:00:00",
    "2020-04-19T12:00:00",
    "2020-04-19T13:00:00",
    "2020-04-19T14:00:00",
    "2020-04-19T15:00:00",
    "2020-04-19T16:00:00",
    "2020-04-19T17:00:00",
    "2020-04-19T18:00:00",
    "2020-04-19T19:00:00",
    "2020-04-19T20:00:00",
    "2020-04-19T21:00:00",
    "2020-04-19T22:00:00",
    "2020-04-19T23:00:00",
    "2020-04-20T00:00:00",
    ]

# time object
list_time = astropy.time.Time (list_time_str, scale='utc')

# is night?
result_is_night = ncu.is_night (list_time)

# printing results
print ("Is night?")
for i in range ( len (result_is_night) ):
    print ("  %s ==> %s" % (list_time[i], result_is_night[i]) )
