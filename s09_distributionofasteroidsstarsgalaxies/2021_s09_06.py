#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:50:16 (CST) daisuke>
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

# data file
file_data = 'bsc2.data'

# output files
file_pdf = 'all_sky_bsc_equ_col.pdf'
file_png = 'all_sky_bsc_equ_col.png'

# numpy arrays to storing data
data_hr   = numpy.array ([])
data_ra   = numpy.array ([])
data_dec  = numpy.array ([])
data_l    = numpy.array ([])
data_b    = numpy.array ([])
data_Vmag = numpy.array ([])
data_BV   = numpy.array ([])

# opening file
fh = open (file_data, 'r')

# counting number of objects
n = 0
for line in fh:
    n += 1

# closing file
fh.close ()

# opening file
fh = open (file_data, 'r')

i = 0
# reading file
for line in fh:
    # skipping line, if the line starts with '#'
    if (line[0] == '#'):
        continue
    # counting and showing progress
    i += 1
    if (i % 500 == 0):
        print ("progress: %4d / %4d" % (i, n) )
    # splitting line
    (hr_str, ra_str, dec_str, glon_str, glat_str, Vmag_str, BV_str) \
        = line.split ()
    # conversion from string to int or float
    hr = int (hr_str)
    glon_deg = float (glon_str)
    glat_deg = float (glat_str)
    Vmag = float (Vmag_str)
    BV = float (BV_str)

    # coordinate
    coord = astropy.coordinates.SkyCoord (ra_str, dec_str, \
                                          frame=astropy.coordinates.FK5, \
                                          equinox="J2000", unit=(u_ha, u_deg) )

    # RA in hour, Dec in deg
    ra_hr = coord.ra.deg / 15.0
    dec_deg = coord.dec.deg
    # conversion from (RA, Dec) to (l, b) using astropy
    l_rad = coord.galactic.l.radian
    b_rad = coord.galactic.b.radian

    # appending data to numpy arrays
    data_hr   = numpy.append (data_hr, hr)
    data_ra   = numpy.append (data_ra, ra_hr)
    data_dec  = numpy.append (data_dec, dec_deg)
    data_l    = numpy.append (data_l, l_rad)
    data_b    = numpy.append (data_b, b_rad)
    data_Vmag = numpy.append (data_Vmag, Vmag)
    data_BV   = numpy.append (data_BV, BV)

# closing file
fh.close ()

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# axes
ax.grid ()
ax.set_xlim (24.0, 0.0)
ax.set_ylim (-90.0, +90.0)
ax.set_xticks (numpy.linspace (0, 24, 9))
ax.set_yticks (numpy.linspace (-90, 90, 7))
ax.set_xlabel ('Right Ascension [hr]')
ax.set_ylabel ('Declination [deg]')

# plotting data
ax.set_title ('Bright Star Catalogue (equatorial)')
size = (8.0 - data_Vmag) * 5.0
colour = 2.0 - data_BV
for j in range ( len (colour) ):
    if (colour[j] < 0.0):
        colour[j] = 0.0
ax.scatter (data_ra, data_dec, s=size, c=colour, cmap=matplotlib.cm.Spectral, \
            marker='o', alpha=0.3)
galplane_l = numpy.linspace (0, 359.99999, 100)
galplane_b = numpy.zeros (100)
galplane = astropy.coordinates.SkyCoord (l=galplane_l, b=galplane_b, \
                                         frame='galactic', unit=u_deg)
galplane_ra_hr = numpy.array ([])
galplane_dec_deg = numpy.array ([])
for k in range ( len (galplane) ):
    ra_hr  = galplane[k].transform_to ('icrs').ra.deg / 15.0
    dec_deg = galplane[k].transform_to ('icrs').dec.deg
    galplane_ra_hr  = numpy.append (galplane_ra_hr, ra_hr)
    galplane_dec_deg = numpy.append (galplane_dec_deg, dec_deg)
ax.plot (galplane_ra_hr, galplane_dec_deg, 'ko', markersize=3)

# saving figure to files
fig.savefig (file_pdf, bbox_inches="tight")
fig.savefig (file_png, dpi=225, bbox_inches="tight")
