#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:48:35 (CST) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units
import astropy.coordinates

# importing astroplan module
import astroplan
import astroplan.plots

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# figure file for saving
file_fig = '2021_s07_17.pdf'

# units
unit_m = astropy.units.m

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
time_str = "2020-04-19T16:00:00"
time     = astropy.time.Time (time_str)

# target
regulus  = astroplan.FixedTarget.from_name ('Regulus')
spica    = astroplan.FixedTarget.from_name ('Spica')
arcturus = astroplan.FixedTarget.from_name ('Arcturus')
antares  = astroplan.FixedTarget.from_name ('Antares')
vega     = astroplan.FixedTarget.from_name ('Vega')
altair   = astroplan.FixedTarget.from_name ('Altair')

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# plotting
box = ax.get_position ()
ax.set_position ([box.x0, box.y0, box.width * 0.83, box.height])
astroplan.plots.plot_airmass (regulus,  lulin, time, ax=ax)
astroplan.plots.plot_airmass (spica,    lulin, time, ax=ax)
astroplan.plots.plot_airmass (arcturus, lulin, time, ax=ax)
astroplan.plots.plot_airmass (antares,  lulin, time, ax=ax)
astroplan.plots.plot_airmass (vega,     lulin, time, ax=ax)
astroplan.plots.plot_airmass (altair,   lulin, time, ax=ax, \
                              brightness_shading=True, max_airmass=2.5)
ax.legend (bbox_to_anchor=(1.05, 1.00), loc='upper left', shadow=True)

# saving the plot into a file
fig.savefig (file_fig, bbox_inches="tight")
