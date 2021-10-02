#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:50:21 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.units
import astropy.coordinates

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg
u_rad = astropy.units.rad

# files
file_cat = 'catalogue/hipparcos/hip2.dat'
file_pdf = 'all_sky_hip_equ_den.pdf'
file_png = 'all_sky_hip_equ_den.png'

# list to store data
list_ra_rad = []
list_dec_rad = []

# counting number of data
n = 0

# opening file
fh = open (file_cat, 'r')

# reading data
for line in fh:
    n += 1

# closing file
fh.close ()

# opening file
fh = open (file_cat, 'r')

# reading data
i = 0
for line in fh:
    # extracting data
    ra_str  = line[15:28].strip ()
    dec_str = line[29:42].strip ()
    mag_str = line[129:136].strip ()
    BV_str  = line[152:158].strip ()

    # skipping, if any of data is missing.
    if ( (ra_str == '') or (dec_str == '') or (mag_str == '') \
         or (BV_str == '') ):
        continue
    # conversion from string to float
    ra_rad  = float (ra_str)
    dec_rad = float (dec_str)
    mag     = float (mag_str)
    BV      = float (BV_str)
    
    # coordinate
    coord = astropy.coordinates.SkyCoord (ra_rad, dec_rad, \
                                          frame=astropy.coordinates.ICRS, \
                                          unit=u_rad)

    # appending data to lists
    ra_rad_wrap = coord.ra.wrap_at (180 * u_deg).radian
    list_ra_rad.append (ra_rad_wrap)
    list_dec_rad.append (coord.dec.radian)

    # progress
    i += 1
    if (i % 5000 == 0):
        print ("progress: %6d / %6d" % (i, n) )

# closing file
fh.close ()

# making numpy arrays
data_ra_rad = numpy.array (list_ra_rad)
list_ra_rad.clear ()
data_dec_rad = numpy.array (list_dec_rad)
list_dec_rad.clear ()

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111, projection="aitoff")

# axes
ax.grid ()

# plotting data
ax.set_title ('Hipparcos Catalogue (equatorial)', loc='right')
dist = ax.hexbin (data_ra_rad, data_dec_rad, gridsize=120, \
                  cmap=matplotlib.cm.inferno)
fig.colorbar (dist, ax=ax, spacing='uniform', extend='max')

# saving file
fig.savefig (file_pdf, bbox_inches="tight")
fig.savefig (file_png, bbox_inches="tight", dpi=600)
