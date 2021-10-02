#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:47:09 (CST) daisuke>
#

# importing sqlite3 module
import sqlite3

# CSV file
file_csv = 'elements.csv'

# database file
file_db = 'elements.db'

# SQL command to make a table
sql_maketable = "create table elements "
sql_maketable += "(AtomicNumber integer primary key, Element text, "
sql_maketable += "Symbol text, AtomicMass real, NumberofNeutrons integer, "
sql_maketable += "NumberofProtons integer, NumberofElectrons integer, "
sql_maketable += "ElementPeriod integer, ElementGroup integer, "
sql_maketable += "Phase text, Radioactive text, "
sql_maketable += "Natural text, Metal text, Nonmetal text, Metalloid text, "
sql_maketable += "Type text, AtomicRadius real, Electronegativity real, "
sql_maketable += "FirstIonization real, Density real, "
sql_maketable += "MeltingPoint real, BoilingPoint real, "
sql_maketable += "NumberOfIsotopes integer, Discoverer text, Year integer, "
sql_maketable += "SpecificHeat real, NumberofShells integer, "
sql_maketable += "NumberofValence integer);"

# connection to database
conn = sqlite3.connect (file_db)
c = conn.cursor ()

# making a table
c.execute (sql_maketable)

# opening file
fh = open (file_csv, 'r')

# processing CSV file line-by-line
for line in fh:
    # if the line does not start with number, then we skip it.
    if not (line[0].isdecimal ()):
        continue

    # removing white space at the end of the line
    line = line.rstrip ()

    # reformatting the data
    if (line.find (',"') >= 0):
        line = line.replace (',"', ',')
        line = line.replace (', ', ' and ')
        line = line.replace ('",', ',')

    # reading data
    (AtomicNumber, Element, Symbol, AtomicMass, \
     NumberofNeutrons, NumberofProtons, NumberofElectrons, \
     Period, Group, Phase, Radioactive, Natural, \
     Metal, Nonmetal, Metalloid, Type, AtomicRadius, \
     Electronegativity, FirstIonization, Density, \
     MeltingPoint, BoilingPoint, NumberOfIsotopes, \
     Discoverer, Year, SpecificHeat, NumberofShells, NumberofValence) \
     = line.split (',')

    AtomicNumber = int (AtomicNumber)
    AtomicMass = float (AtomicMass)
    NumberofNeutrons = int (NumberofNeutrons)
    NumberofProtons = int (NumberofProtons)
    NumberofElectrons = int (NumberofElectrons)
    Period = int (Period)
    if (Group == ''):
        Group = -1
    else:
        Group = int (Group)
    if (Radioactive == ''):
        Radioactive = 'no'
    if (Natural == ''):
        Natural = 'no'
    if (Metal == ''):
        Metal = 'no'
    if (Nonmetal == ''):
        Nonmetal = 'no'
    if (Metalloid == ''):
        Metalloid = 'no'
    if (Type == ''):
        Type = 'unknown'
    if (AtomicRadius == ''):
        AtomicRadius = -1.0
    else:
        AtomicRadius = float (AtomicRadius)
    if (Electronegativity == ''):
        Electronegativity = -1.0
    else:
        Electronegativity = float (Electronegativity)
    if (FirstIonization == ''):
        FirstIonization = -1.0
    else:
        FirstIonization = float (FirstIonization)
    if (Density == ''):
        Density = -1.0
    else:
        Density = float (Density)
    if (MeltingPoint == ''):
        MeltingPoint = -1.0
    else:
        MeltingPoint = float (MeltingPoint)
    if (BoilingPoint == ''):
        BoilingPoint = -1.0
    else:
        BoilingPoint = float (BoilingPoint)
    if (NumberOfIsotopes == ''):
        NumberOfIsotopes = -1
    else:
        NumberOfIsotopes = int (NumberOfIsotopes)
    if (Discoverer == ''):
        Discoverer = 'UNDEF'
    if (Year == ''):
        Year = -9999
    else:
        Year = int (Year)
    if (SpecificHeat == ''):
        SpecificHeat = -1.0
    else:
        SpecificHeat = float (SpecificHeat)
    NumberofShells = int (NumberofShells)
    if (NumberofValence == ''):
        NumberofValence = 0
    else:
        NumberofValence = int (NumberofValence)

    # making SQL command to add data
    sql_adddata = "insert into elements values (%d, \"%s\", \"%s\", " \
        % (AtomicNumber, Element, Symbol)
    sql_adddata += "%f, %d, %d, %d, " \
        % (AtomicMass, NumberofNeutrons, NumberofProtons, NumberofElectrons)
    sql_adddata += "%d, %d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", " \
        % (Period, Group, Phase, Radioactive, Natural, \
           Metal, Nonmetal, Metalloid)
    sql_adddata += "\"%s\", %f, %f, %f, %f, %f, %f, " \
        % (Type, AtomicRadius, Electronegativity, FirstIonization, \
           Density, MeltingPoint, BoilingPoint)
    sql_adddata += "%d, \"%s\", %d, %f, %d, %d);" \
        % (NumberOfIsotopes, Discoverer, Year, SpecificHeat, \
           NumberofShells, NumberofValence)

    # executing a SQL command to add data into table
    c.execute (sql_adddata)
    
# closing file
fh.close ()

# closing the connection to database
conn.commit ()
conn.close()
