#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:39:34 (CST) daisuke>
#

# constants
n = 10
divisor = 3

# a loop using control flow statement "for"
for i in range (1, n):
    remainder = i % divisor
    if (remainder == 0):
        print ("%d can be divided by %d, and remainder is 0." \
               % (i, divisor) )
    elif (remainder == 1):
        print ("%d cannot be divided by %d, and remainder is 1." \
               % (i, divisor) )
    else:
        print ("%d cannot be divided by %d, and remainder is 2." \
               % (i, divisor) )
