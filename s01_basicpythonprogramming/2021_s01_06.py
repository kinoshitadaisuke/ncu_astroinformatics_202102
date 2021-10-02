#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:39:11 (CST) daisuke>
#

# definition of a function
def au2m (distance_au):
    au = 1.495978707 * 10**11
    distance_m = distance_au * au
    return (distance_m)

# semimajor axis of Neptune in au
a_neptune_au = 30.0699

# conversion from au to metre
a_neptune_m = au2m (a_neptune_au)

# printing result
print ("semimajor axis of Neptune:")
print ("  a = %f au" % a_neptune_au)
print ("    = %g m" % a_neptune_m)
