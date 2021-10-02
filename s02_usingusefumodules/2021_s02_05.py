#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:55 (CST) daisuke>
#

# importing argparse module
import argparse

# list of available operators
list_operators = ['+', '-', 'x', '/']

# command-line arguments analysis
parser = argparse.ArgumentParser (description='arithmetic calculations')
parser.add_argument ('number1', type=float, help='number1')
parser.add_argument ('operator', choices=list_operators, help='operator')
parser.add_argument ('number2', type=float, help='number2')
args = parser.parse_args()

# input parameters
n1 = args.number1
n2 = args.number2
op = args.operator

# calculation
if (op == '+'):
    result = n1 + n2
elif (op == '-'):
    result = n1 - n2
elif (op == 'x'):
    result = n1 * n2
elif (op == '/'):
    result = n1 / n2

# printing result
print ("%f %s %f = %f" % (n1, op, n2, result) )
