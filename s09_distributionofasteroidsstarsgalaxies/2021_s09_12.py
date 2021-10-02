#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:50:32 (CST) daisuke>
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
u_deg = astropy.units.deg

# files
file_eph = 'asteroids_20210503.data'
file_pdf = 'all_sky_asteroids_20210503_2.pdf'
file_png = 'all_sky_asteroids_20210503_2.png'

# lists for storing data
list_ra_rad  = []
list_dec_rad = []

# opening file
fh = open (file_eph, 'r')

# reading file
for line in fh:
    # splitting line and extracting data
    (ra_rad_str, dec_rad_str, date_str, number_str) = line.split ()
    # conversion from string to float
    ra_rad  = float (ra_rad_str)
    dec_rad = float (dec_rad_str)
    # appending data to lists
    list_ra_rad.append (ra_rad)
    list_dec_rad.append (dec_rad)

# closing file
fh.close ()

# making numpy arrays
data_ra_rad = numpy.array (list_ra_rad)
list_ra_rad.clear ()
data_dec_rad = numpy.array (list_dec_rad)
list_dec_rad.clear ()

# Ecliptic
ecliptic_l  = numpy.linspace (0.0, 359.99999, 100)
ecliptic_b  = numpy.zeros (100)
ecliptic = astropy.coordinates.SkyCoord (ecliptic_l, ecliptic_b, \
                                         frame='geocentricmeanecliptic', \
                                         unit=u_deg)
ecliptic_ra   = ecliptic.transform_to ('icrs').ra.radian
ecliptic_dec  = ecliptic.transform_to ('icrs').dec.radian

# wrapping RA
for i in range ( len (data_ra_rad) ):
    if (data_ra_rad[i] > numpy.pi):
        data_ra_rad[i] -= 2.0 * numpy.pi
for i in range ( len (ecliptic_ra) ):
    if (ecliptic_ra[i] > numpy.pi):
        ecliptic_ra[i] -= 2.0 * numpy.pi

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111, projection="mollweide")

# axes
ax.grid ()

# plotting data
title_str = "Asteroids on %s (equatorial)" % (date_str)
ax.set_title (title_str, loc='right')
dist = ax.hexbin (data_ra_rad, data_dec_rad, gridsize=90, \
                  cmap=matplotlib.cm.plasma)
fig.colorbar (dist, ax=ax, spacing='uniform', extend='both')
ax.plot (ecliptic_ra, ecliptic_dec, marker='o', color='yellow', \
         markersize=0.1, linestyle=None)

# saving file
fig.savefig (file_pdf, bbox_inches="tight")
fig.savefig (file_png, bbox_inches="tight", dpi=600)
