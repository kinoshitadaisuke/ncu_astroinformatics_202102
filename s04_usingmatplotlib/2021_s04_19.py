#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:45:17 (CST) daisuke>
#

# importing sys module
import sys

# importing argparse module
import argparse

# importing numpy array
import numpy

# importing matplotlib module
import matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# argument analysis
desc = 'a Python script to make a HR-diagram using Matplotlib'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', default='', help='input file name')
parser.add_argument ('-o', default='', help='output file name')
args = parser.parse_args()

# catalogue file name
file_input  = args.i
file_output = args.o

if (file_input == ''):
    print ("You have to specify the name of input file using -i option.")
    sys.exit ()

if (file_output == ''):
    print ("You have to specify the name of output file using -o option.")
    sys.exit ()

# dictionary for storing data
stars = {}

# opening catalogue file
fh = open (file_input, 'r')

# reading catalogue line-by-line
for line in fh:
    # Harvard Revised Number of star
    HR = line[0:4].strip ()
    # name
    name = line[4:14].strip ()
    # Vmag
    mag_V = line[102:107].strip ()
    # B-V colour
    colour_BV = line[109:114].strip ()
    # dynamical parallax flag
    dynamical_parallax = line[160].strip ()
    # spectral type
    sptype = line[127:147].strip ()
    # parallax
    parallax = line[161:166].strip ()

    # skip, if any of mag_V, colour_BV, parallax is missing
    if ( (mag_V == '') or (colour_BV == '') or (parallax == '') ):
        continue
    # skip, if parallax is negative
    if (parallax[0] == '-'):
        continue
    # skip, if parallax is dynamical parallax
    if (dynamical_parallax == 'D'):
        continue
    # reformat parallax
    if (parallax[:2] == '+.'):
        parallax = '+0.' + parallax[2:]

    # conversion from string to float
    mag_V     = float (mag_V)
    colour_BV = float (colour_BV)
    parallax  = float (parallax)

    # skip, if parallax is zero
    if (parallax < 10**-4):
        continue
    
    # distance in parsec
    dist_pc = 1.0 / parallax

    # absolute magnitude
    absmag_V = mag_V - 5.0 * numpy.log10 (dist_pc) + 5.0

    # constructing the dictionary
    stars[HR] = {}
    stars[HR]["mag_V"]     = mag_V
    stars[HR]["colour_BV"] = colour_BV
    stars[HR]["parallax"]  = parallax
    stars[HR]["dist_pc"]   = dist_pc
    stars[HR]["absmag_V"]  = absmag_V
    stars[HR]["sptype"]    = sptype
    stars[HR]["name"]      = name
    
# closing catalogue file
fh.close ()

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = '(B-V) Colour Index'
label_y = 'Absolute Magnitude [mag]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting a figure
ax.invert_yaxis ()
box = ax.get_position ()
ax.set_position ([box.x0, box.y0, box.width * 0.59, box.height])
# plotting data
i = 0
j = 0
for key, value in sorted (stars.items (), key=lambda x: x[1]['mag_V']):
    if (stars[key]['mag_V'] >= 1.5):
        break
    if (i > 9):
        i -= 9
        j += 1
    if (stars[key]['mag_V'] >= 1.5):
        break
    label = "%s (%s)" % (stars[key]['name'], stars[key]['sptype'])
    if (j == 0):
        ax.plot (stars[key]['colour_BV'], stars[key]['absmag_V'], 'o', \
                 label=label)
    elif (j == 1):
        ax.plot (stars[key]['colour_BV'], stars[key]['absmag_V'], 's', \
                 label=label)
    i += 1
ax.legend (bbox_to_anchor=(1.0, 1.05), loc='upper left')

# saving the figure to a file
fig.savefig (file_output)
