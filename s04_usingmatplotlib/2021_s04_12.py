#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:44:55 (CST) daisuke>
#

# importing sys module
import sys

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# argument analysis
desc = 'a Python script to make a log plot using Matplotlib'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-o', default='', help='output file name')
args = parser.parse_args()

# output file name
file_output = args.o

if (file_output == ''):
    print ("You have to specify the name of output file using -o option.")
    sys.exit ()

# semimajor axis and orbital period of planets
# make a dictionary to store the data
planets = {
    'Mercury': { 'a':  0.3871, 'P':    88.0, 'marker': 'bs'},
    'Venus':   { 'a':  0.7233, 'P':   224.7, 'marker': 'y^'}, 
    'Earth':   { 'a':  1.0000, 'P':   365.2, 'marker': 'go'},
    'Mars':    { 'a':  1.5237, 'P':   687.0, 'marker': 'rv'},
    'Jupiter': { 'a':  5.2034, 'P':  4331.0, 'marker': 'ms'},
    'Saturn':  { 'a':  9.5371, 'P': 10747.0, 'marker': 'g^'},
    'Uranus':  { 'a': 19.1913, 'P': 30589.0, 'marker': 'co'},
    'Neptune': { 'a': 30.0690, 'P': 59800.0, 'marker': 'bv'},
}

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Semimajor Axis [au]'
label_y = 'Orbital Period [day]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# range of x and y axes
x_min = 0.1
x_max = 100.0
y_min = 10.0
y_max = 100000.0
    
# axis settings
ax.set_xlim (x_min, x_max)
ax.set_ylim (y_min, y_max)
ax.set_xscale ('log')
ax.set_yscale ('log')

# plotting data
C = 365.256363004
data_x = numpy.linspace (0.1, 100.0, 10**3)
data_y = data_x**1.5 * C
ax.plot (data_x, data_y, color='coral', linewidth=3, linestyle='--')
for planet in planets.keys ():
    ax.plot (planets[planet]['a'], planets[planet]['P'], \
             planets[planet]['marker'], label=planet, markersize=10)
ax.grid ()
ax.legend ()

# saving the figure to a file
fig.savefig (file_output)
