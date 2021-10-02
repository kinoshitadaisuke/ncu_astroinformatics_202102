#
# Time-stamp: <2021/10/02 12:40:32 (CST) daisuke>
#

# conversion from au to metre
def au2m (distance_au):
    au = 1.495978707 * 10**11
    distance_m = distance_au * au
    return (distance_m)

# conversion from parsec to metre
def pc2m (distance_pc):
    pc = 3.085677581 * 10**16
    distance_m = distance_pc * pc
    return (distance_m)

# conversion from light-year to metre
def ly2m (distance_ly):
    ly = 9.4607304725808 * 10**15
    distance_m = distance_ly * ly
    return (distance_m)

# conversion from annual parallax to distance in pc
def par2dist (parallax_arcsec):
    distance_pc = 1.0 / parallax_arcsec
    return (distance_pc)
