#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:00 (CST) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units
import astropy.coordinates

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

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
time_str = "2021-04-19T04:00:00"
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

# position of the Sun
sun = astropy.coordinates.get_body ('sun', time, location)
(sun_ra, sun_dec) = sun.to_string ('hmsdms').split ()

# conversion from equatorial into ecliptic
sun_ecliptic = sun.transform_to \
    (astropy.coordinates.GeocentricMeanEcliptic (obstime=time) )
sun_lambda = sun_ecliptic.lon
sun_beta   = sun_ecliptic.lat

# conversion from equatorial into horizontal
sun_altaz = sun.transform_to \
    (astropy.coordinates.AltAz (obstime=time, location=location) )
sun_alt = sun_altaz.alt
sun_az  = sun_altaz.az

# printing position of the Sun
print ("Sun:")
print ("  Equatorial: RA=%s, Dec=%s" % (sun_ra, sun_dec) )
print ("  Ecliptic:   lambda=%s, beta=%s" % (sun_lambda, sun_beta) )
print ("  AltAz:      az=%s, alt=%s" % (sun_az, sun_alt) )
