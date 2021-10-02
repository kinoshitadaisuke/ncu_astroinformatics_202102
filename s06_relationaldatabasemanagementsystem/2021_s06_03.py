#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:47:04 (CST) daisuke>
#

# importing sqlite3 module
import sqlite3

# importing math module
import math

# database file
file_database = 'bsc.db'

# connecting to the database
conn = sqlite3.connect(file_database)
c = conn.cursor ()

# SQL query
command = 'select hr,name,RA_str,DEC_str,Glon,Glat,Vmag,BV,SpType,' \
    + 'parallax,pmRA,pmDEC,pm_total,radvel,rotvel from bsc ' \
    + 'where name like \"%Alp%Ori%\";'
c.execute (command)

# fetching results of query
result = c.fetchone ()

# calculations
parallax = result[9]
if (parallax < 0.0):
    distance = 0.0
    absmag = -999.99
else:
    distance = 1.0 / parallax
    absmag = result[6] - 5.0 * math.log10 (distance) + 5.0

# printing result of query
print ("Star: HR %d" % result[0])
print ("  Name: %s" % result[1])
print ("  RA and DEC: %s, %s" % (result[2], result[3]) )
print ("  Glon and Glat: %f, %f" % (result[4], result[5]) )
print ("  Vmag: %f mag" % result[6])
print ("  B-V: %f" % result[7])
print ("  Spectral Type: %s" % result[8])
print ("  parallax: %f arcsec" % result[9])
print ("  distance: %f parsec" % distance)
print ("  absolute magnitude: %f mag" % absmag)
print ("  proper motion in RA: %f arcsec/yr" % result[10])
print ("  proper motion in DEC: %f arcsec/yr" % result[11])
print ("  total proper motion: %f arcsec/yr" % result[12])
print ("  radial velocity: %f km/s" % result[13])
print ("  rotational velocity: %f km/s" % result[14])
