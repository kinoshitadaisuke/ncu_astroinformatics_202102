#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:21 (CST) daisuke>
#

# importing decimal module
import decimal

# importing math module
import math

# precision
decimal.getcontext ().prec = 50

# number of terms
n = 10**9

# a constant
k = 10

# initial value of pi
pi = decimal.Decimal ('0.0')

# calculation of pi using Leibniz formula
for i in range (n):
    pi += decimal.Decimal ('4.0') / (2 * i + 1) * (-1)**i
    if ( (i + 1) % k == 0):
        print (pi, "(n=%d)" % k)
        k *= 10

# printing math.pi
print (math.pi, "(math.pi)")
