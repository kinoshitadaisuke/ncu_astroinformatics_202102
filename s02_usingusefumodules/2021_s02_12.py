#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:17 (CST) daisuke>
#

# importing decimal module
import decimal

# constants a and b
a = 1.1
b = 2.2

# calculation
c = a + b

# printing result
print ("a =", a)
print ("b =", b)
print ("c = a + b =", c)

# constants d and e
d = decimal.Decimal ('1.1')
e = decimal.Decimal ('2.2')

# calculation
f = d + e

# printing result
print ("d =", d)
print ("e =", e)
print ("f = d + e =", f)

# calculation of 1.0/7.0
g = 1.0 / 7.0
print ("g =", g)

# calculation of 1.0/7.0 using decimal module
decimal.getcontext ().prec = 50
h = decimal.Decimal ('1.0') / decimal.Decimal ('7.0')
print ("h =", h)

# sqrt(2)
i = decimal.Decimal ('2.0').sqrt ()
print ("sqrt(2) =", i)
