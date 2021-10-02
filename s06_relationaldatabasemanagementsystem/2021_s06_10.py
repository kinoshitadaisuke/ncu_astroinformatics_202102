#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:47:23 (CST) daisuke>
#

# importing modules
import sqlite3

# database file
file_db = 'mpcorb.db'

# connection to the database
conn = sqlite3.connect (file_db)
c = conn.cursor ()

# SQL query
c.execute ("select name,a,e,i,absmag from mpcorb where (name like '%wingip%')")

# printing results
print ("%-28s %11s %9s %9s %6s" % ('Name', 'a [au]', 'e', 'i [deg]', 'absmag'))
print ("-------------------------------------------------------------------")
for obj in c.fetchall ():
    print ("%-28s %11.7f %9.7f %9.5f %6.1f" \
           % (obj[0], obj[1], obj[2], obj[3], obj[4]) )

# closing connection
conn.commit ()
conn.close ()
