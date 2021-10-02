#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:39:57 (CST) daisuke>
#

# initialisation of a multi-dimensional dictionary
asteroid = {
    'Ceres': {
        'a': 2.769,
        'e': 0.076,
        'i': 10.594,
        'H': 3.4,
        'diameter': 939.4,
        'rotation period': 9.07,
    },
    'Pallas': {
        'a': 2.774,
        'e': 0.230,
        'i': 34.833,
        'H': 4.2,
        'diameter': 545,
        'rotation period': 7.81,
    },
    'Juno': {
        'a': 2.668,
        'e': 0.257,
        'i': 12.991,
        'H': 5.33,
        'diameter': 246.596,
        'rotation period': 7.21,
    },
    'Vesta': {
        'a': 2.361,
        'e': 0.089,
        'i': 7.142,
        'H': 3.0,
        'diameter': 525.4,
        'rotation period': 5.34,
    },
}

# printing dictionary information
print ("Ceres =", asteroid['Ceres'])
print ("Vesta =", asteroid['Vesta'])
print ("a of Pallas =", asteroid['Pallas']['a'], "au")
print ("e of Juno =", asteroid['Juno']['e'])
print ("i of Vesta =", asteroid['Vesta']['i'], "deg")
print ("H of Ceres =", asteroid['Ceres']['H'], "mag")

# printing rotation period of 4 asteroids
for key in (asteroid.keys ()):
    print ("rotation period of %-6s : %4.1f hour" \
           % (key, asteroid[key]['rotation period']) )
