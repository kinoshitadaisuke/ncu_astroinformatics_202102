#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:47:12 (CST) daisuke>
#

# importing sqlite3 module
import sqlite3

# importing argparse module
import argparse

# database file
file_database = 'elements.db'

# connecting to the database
conn = sqlite3.connect (file_database)
c = conn.cursor ()

# SQL query
command = 'select AtomicNumber,Element,Symbol,AtomicMass,' \
    + 'NumberofProtons,NumberofNeutrons,NumberofElectrons,' \
    + 'Phase,Radioactive,Type,Density,MeltingPoint,BoilingPoint,Year ' \
    + 'from elements where (Phase like \"liq\") order by AtomicNumber;'
c.execute (command)

# fetching results of query
results = c.fetchall ()

# printing results of query
for result in results:
    print ("Element: %s (%s, Atomic Number = %d, Atomic Mass = %f)" \
           % (result[1], result[2], result[0], result[3]) )
    print ("  Protons = %3d, Neutrons = %3d, Electrons = %3d" \
           % (result[4], result[5], result[6]) )
    print ("  Phase = %-12s, Radioactive = %-3s, Type = %-24s" \
           % (result[7], result[8], result[9]) )
    print ("  Melting Point = %7.2f K, Boiling Point = %7.2f K" \
           % (result[11], result[12]) )
    print ("  Density = %g g/cc, Discovery Year = %4d" \
           % (result[10], result[13]) )
