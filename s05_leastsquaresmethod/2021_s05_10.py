#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:46:07 (CST) daisuke>
#

# importing modules
import argparse
import sys
import numpy
import matplotlib.figure
import matplotlib.backends.backend_agg

# argument analysis
desc = 'plotting a set of data'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', default='', help='input file name')
parser.add_argument ('-o', default='', help='output file name')
args = parser.parse_args ()

# data file name
file_input  = args.i

# output file name
file_output = args.o

# if no file name is specified for input file, then we stop the program.
if (file_input == ''):
    print ("The input file name has to be specified.")
    sys.exit (1)
# if no file name is specified for output file, then we stop the program.
if (file_output == ''):
    print ("The output file name has to be specified.")
    sys.exit (1)
# if output file name is not PDF, PNG, PS, or EPS, then we top the program.
if not ( (file_output[-4:] == '.pdf') or (file_output[-4:] == '.png') \
         or (file_output[-3:] == '.ps') or (file_output[-4:] == '.eps') ):
    print ("The output file has to be PDF or PNG, PS, or EPS.")
    sys.exit (1)

    
# making empty numpy arrays for data
data_x = numpy.array ([])
data_y = numpy.array ([])

# opening file for reading
fh_read = open (file_input, 'r')

for line in fh_read:
    # splitting the line into x and y
    (x_str, y_str) = line.split ()
    # converting string into float
    x_float = float (x_str)
    y_float = float (y_str)
    # appending data to numpy arrays
    data_x = numpy.append (data_x, x_float)
    data_y = numpy.append (data_y, y_float)

# closing file
fh_read.close ()

# printing x and y values
print (data_x)
print (data_y)

# making fig and ax
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'X [arbitrary unit]'
label_y = 'Y [arbitrary unit]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting a figure
ax.plot (data_x, data_y, 'bo', label='synthetic data for least-squares method')
ax.legend ()

# saving the figure to a file
fig.savefig (file_output)
