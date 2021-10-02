#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 13:52:12 (CST) daisuke>
#

# importing your own module
import ncu_astro

# semimajor axis of Saturn in au
a_saturn_au = 9.54

# conversion from au to metre
a_saturn_m = ncu_astro.au2m (a_saturn_au)

# printing result
print ("a of Saturn = %5.2f au" % a_saturn_au)
print ("             = %g m" % a_saturn_m)

# distance to Canopus in parsec
dist_canopus_pc = 95

# conversion from parsec to metre
dist_canopus_m = ncu_astro.pc2m (dist_canopus_pc)

# printing result
print ("distance to Canopus = %d pc" % dist_canopus_pc)
print ("                    = %g m" % dist_canopus_m)

# parsec and light-year
dist_1pc = ncu_astro.pc2m (1.0)
dist_1ly = ncu_astro.ly2m (1.0)
print ("1 pc = %5.3f ly" % (dist_1pc / dist_1ly) )

# annual parallax of Sirius in mas
p_sirius_mas = 379.21
p_sirius_arcsec = p_sirius_mas / 1000.0
dist_sirius_pc = ncu_astro.par2dist (p_sirius_arcsec)
dist_sirius_m = ncu_astro.pc2m (dist_sirius_pc)
print ("annual parallax of Sirius = %f mas" % p_sirius_mas)
print ("distance to Sirius = %f pc" % dist_sirius_pc)
print ("                   = %g m" % dist_sirius_m)
