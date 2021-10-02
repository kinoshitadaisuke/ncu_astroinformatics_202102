#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:40 (CST) daisuke>
#

# importing astropy module
import astropy
import astropy.coordinates
import astropy.units
import astropy.utils

# units
u_deg  = astropy.units.deg
u_hour = astropy.units.hour
u_m    = astropy.units.m

# setting for coordinate conversion from/to horizontal system
astropy.utils.iers.conf.auto_download = True

# obtaining coordinate of Betelgeuse
obj = 'Acrux'
coord = astropy.coordinates.SkyCoord.from_name (obj, parse=True)

# printing coordinate of Betelgeuse
print ("Coordinate of %s:" % obj)
print ("  equatorial (in decimal deg):", coord.to_string ('decimal'))
print ("  equatorial (in hmsdms):", coord.to_string ('hmsdms'))

# coordinate conversion into Galactic coordinate
coord_galactic = coord.transform_to ('galactic')

# printing result of coordinate conversion
print ("  galactic (in decimal deg):", coord_galactic.to_string ('decimal'))

# coordinate conversion into horizontal coordinate
lulin_lon = '+120:52:25'
lulin_lat = '+23:28:07'
lulin_altitude = 2862.0 * u_m
site_lon = astropy.coordinates.Angle (lulin_lon, unit=u_deg)
site_lat = astropy.coordinates.Angle (lulin_lat, unit=u_deg)
site_altitude = lulin_altitude
location_site \
    = astropy.coordinates.EarthLocation (lat=site_lat, lon=site_lon, \
                                         height=site_altitude)

# time
obs_datetime = '2021-03-09 01:00:00'
utc_offset = 8 * u_hour
time = astropy.time.Time (obs_datetime) - utc_offset
coord_altaz = coord.transform_to \
    (astropy.coordinates.AltAz (obstime=time, location=location_site))

# printing result of coordinate conversion
print ("  altaz (in decimal deg):", coord_altaz.to_string ('decimal'))
