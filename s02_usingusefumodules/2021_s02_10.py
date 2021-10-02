#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:11 (CST) daisuke>
#

# importing random module
import random

# initialising random number generator
random.seed ()

# parameters
n_min  =   0.0
n_max  = 100.0
mean   =  50.0
stddev =  10.0

i = 5

# generating random numbers (i) times
for j in range (i):
    # generating a random number of uniform distribution betwee 0 and 100
    n = random.uniform (n_min, n_max)

    # printing result
    print ("generated random number (0<=n<100) =", n)

# generating random numbers (i) times
for j in range (i):
    # generating a random number of Gaussian distribution
    n = random.gauss (mean, stddev)

    # printing result
    print ("generated random number (Gauss, mean=%4.1f, stddev=%4.1f) = %f" \
           % (mean, stddev, n) )
