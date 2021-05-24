#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/23 17:14:56 (CST) daisuke>
#

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = '2021_s12_05.pdf'

# target list
# Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, and Pluto
dic_target = {
    '10':  'Sun',
    '199': 'Mercury',
    '299': 'Venus',
    '399': 'Earth',
    '499': 'Mars',
    '599': 'Jupiter',
    '699': 'Saturn',
    '799': 'Uranus',
    '899': 'Neptune',
    '999': 'Pluto'
}

# marker size and colour
sizes   = [10, 2, 5, 5, 4, 8, 8, 6, 6, 2]
colours = ['yellow', 'blue', 'gold', 'green', 'red', \
           'orange', 'brown', 'lime', 'indigo', 'slategrey']

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'X [au]'
label_y = 'Y [au]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# axes
ax.set_xlim (-35, 35)
ax.set_ylim (-35, 35)
ax.set_aspect('equal')
ax.grid ()

# getting positions of the Sun and planets
for i, n in enumerate (dic_target):
    # querying JPL Horizons
    obj = astroquery.jplhorizons.Horizons (id=n, id_type='majorbody', \
                                           location='@ssb', \
                                           epochs={'start': '2021-05-24', \
                                                   'stop': '2021-05-25', \
                                                   'step': '1y'})
    # state vector of the target object
    vec = obj.vectors ()

    # plotting data
    ax.plot (vec['x'], vec['y'], marker='o', markersize=sizes[i], \
             color=colours[i], label=dic_target[n])

# title of plot
ax.set_title ("Positions of the Sun and planets on 24/May/2021")
# showing legend
ax.legend (bbox_to_anchor=(1.01, 1.00), loc='upper left', shadow=True)

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
