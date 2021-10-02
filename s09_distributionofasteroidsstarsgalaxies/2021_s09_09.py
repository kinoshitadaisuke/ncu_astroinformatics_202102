#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:50:24 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# files
list_file_cat = ['catalogue/2mass/xsc_aaa', 'catalogue/2mass/xsc_baa']
file_pdf  = 'all_sky_2mass_den.pdf'
file_png  = 'all_sky_2mass_den.png'

# lists for storing data
list_glon_rad = []
list_glat_rad = []

# reading catalogue files
for file_cat in list_file_cat:
    print ("reading the file \"%s\"..." % (file_cat) )

    # opening file
    fh = open (file_cat, 'r')

    # reading lines
    for line in fh:
        # splitting line
        records = line.split ('|')
        # extracting data
        glon_str = records[6].strip ()
        glat_str = records[7].strip ()
        # skip, if any of data is missing.
        if ( (glon_str == '') or (glat_str == '') ):
            continue
        # conversion from string to float
        glon_deg = float (glon_str)
        glat_deg = float (glat_str)
        # deg --> radian
        glon_rad = glon_deg / 180.0 * numpy.pi
        if (glon_rad > numpy.pi):
            glon_rad -= 2.0 * numpy.pi
        glat_rad = glat_deg / 180.0 * numpy.pi
        # appending data to lists
        list_glon_rad.append (glon_rad)
        list_glat_rad.append (glat_rad)

    # closing file
    fh.close ()

    print ("done!")

print ("constructing numpy arrays...")

# making numpy arrays
data_glon_rad = numpy.array (list_glon_rad)
list_glon_rad.clear ()
data_glat_rad = numpy.array (list_glat_rad)
list_glat_rad.clear ()

print ("done!")

print ("generating a plot...")

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111, projection="aitoff")

# axes
ax.grid ()

# plotting data
ax.set_title ('2MASS XSC (galactic)', loc='right')
dist = ax.hexbin (data_glon_rad, data_glat_rad, gridsize=180, \
                  cmap=matplotlib.cm.plasma)
fig.colorbar (dist, ax=ax, spacing='uniform', extend='max')

# saving file
fig.savefig (file_pdf, bbox_inches="tight")
fig.savefig (file_png, bbox_inches="tight", dpi=600)

print ("done!")
