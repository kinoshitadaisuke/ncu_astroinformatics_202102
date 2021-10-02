#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:48 (CST) daisuke>
#

# importing astropy module
import astropy.units

# importing astroplan module
import astroplan
import astroplan.plots

# importing matplotlib module
import matplotlib.pyplot

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# file
file_fig = '2021_s07_20.pdf'

# units
unit_arcmin = astropy.units.arcmin

# field-of-view
fov = 15.0 * unit_arcmin

# target
m13 = astroplan.FixedTarget.from_name ('M13')

# image
ax, hdu = astroplan.plots.plot_finder_image (m13, fov_radius=fov)

# saving the image to file
matplotlib.pyplot.savefig (file_fig)
