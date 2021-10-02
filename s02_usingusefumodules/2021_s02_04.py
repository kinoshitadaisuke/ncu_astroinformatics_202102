#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:52 (CST) daisuke>
#

# importing argparse module
import argparse

# command-line arguments analysis
parser = argparse.ArgumentParser (description='multiplication')
parser.add_argument ('-a', type=float, default=1.0, help='multiplicand')
parser.add_argument ('-b', type=float, default=1.0, help='multiplier')
args = parser.parse_args()

# multiplicand
a = args.a
# multiplier
b = args.b

# printing a and b
print ("a = %f" % a)
print ("b = %f" % b)

# calculation of the product of a and b
c = a * b

# printing result of calculation
print ("c = a * b = %f" % c)
