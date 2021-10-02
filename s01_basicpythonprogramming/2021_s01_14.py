#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:39:53 (CST) daisuke>
#

# initialisation of a dictionary
mag = {
    "Sirius": -1.46,
    "Canopus": -0.74,
    "Rigil Kentaurus": -0.27,
    "Arcturus": -0.05,
    "Vega": 0.03,
    "Capella": 0.08,
    "Rigel": 0.13,
    "Procyon": 0.34,
    "Achernar": 0.46,
    "Betelgeuse": 0.50,
}

# printing the dictionary "mag"
print (mag)

# accessing to an element
print ("magnitude of Vega =", mag['Vega'])

# printing all the data
for star in sorted (mag.keys ()):
    print ("%-16s : %+5.2f mag" % (star, mag[star]) )
