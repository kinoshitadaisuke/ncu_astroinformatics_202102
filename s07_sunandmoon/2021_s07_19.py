#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:42 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units
import astropy.coordinates

# importing astroplan module
import astroplan
import astroplan.plots

# importing matplotlib module
import matplotlib.pyplot

# figure file for saving
file_fig = '2021_s07_19.pdf'

# units
unit_m = astropy.units.m
unit_hour = astropy.units.hour

# Lulin observatory
lulin_lon = "+120d52m25s"
lulin_lat = "+23d28m07s"
lulin_elev = 2862 * unit_m

# location object
location = astropy.coordinates.EarthLocation.from_geodetic \
    (lulin_lon, lulin_lat, lulin_elev)

# observer object
lulin = astroplan.Observer (location=location, name="Lulin", \
                            timezone="Asia/Taipei")

# date/time
time_str = "2021-04-19T16:00:00"
time     = astropy.time.Time (time_str)
time     = time + numpy.linspace (-5, +5, 11) * unit_hour

# target
regulus  = astroplan.FixedTarget.from_name ('Regulus')
arcturus = astroplan.FixedTarget.from_name ('Arcturus')
antares  = astroplan.FixedTarget.from_name ('Antares')
vega     = astroplan.FixedTarget.from_name ('Vega')

# plotting
astroplan.plots.plot_sky (regulus,  lulin, time)
astroplan.plots.plot_sky (arcturus, lulin, time)
astroplan.plots.plot_sky (antares,  lulin, time)
astroplan.plots.plot_sky (vega,     lulin, time)
matplotlib.pyplot.legend (loc='upper left', bbox_to_anchor=(1.05, 1.0) )
matplotlib.pyplot.title ("sky chart on 19/Apr/2021")

# saving the plot into a file
matplotlib.pyplot.savefig (file_fig, bbox_inches="tight")
