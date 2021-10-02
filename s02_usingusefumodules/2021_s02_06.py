#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:58 (CST) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# command-line arguments analysis
parser = argparse.ArgumentParser (description='counting numbers')
parser.add_argument ('-f', help='filename')
args = parser.parse_args()

# input parameters
filename = args.f

# initialisation of a list
numbers = [ 0 ] * 10

if (filename == None):
    # stop processing if the file name is not given
    print ("File name has to be specified.")
    sys.exit (1)
else:
    # opening the file
    fh = open (filename, 'r')
    # reading the file line-by-line
    for line in fh:
        # total number of digits
        length = len (line)
        # processing digits one-by-one
        for i in range (length):
            # counting numbers appearing in pi
            n = int (line[i])
            numbers[n] += 1
    # closing the file
    fh.close ()

# printing results
for i in range (10):
    print ("%d : %8d" % (i, numbers[i]) )
