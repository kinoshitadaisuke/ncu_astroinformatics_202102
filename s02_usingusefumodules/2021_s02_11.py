#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:14 (CST) daisuke>
#

# importing random module
import random
# importing statistics module
import statistics

# number of random numbers to be generated
n = 10**6

# minimum and maximum values of random numbers of uniform distribution
n_min =   0.0
n_max = 100.0

# mean and stddev of random numbers of Gaussian distribution
mean   = 50.0
stddev = 10.0

# lists to store random numbers
list_uniform = []
list_gauss   = []

# initialisation of random number generator
random.seed ()

# generating random numbers (n) times
for i in range (n):
    # generating a random number of uniform distribution
    r_uniform = random.uniform (n_min, n_max)
    # appending generated random number to the list
    list_uniform.append (r_uniform)

    # generating a random number of Gaussian distribution
    r_gauss   = random.gauss (mean, stddev)
    # appending generated random number to the list
    list_gauss.append (r_gauss)

# calculations of statistical values
uniform_mean     = statistics.mean (list_uniform)
uniform_median   = statistics.median (list_uniform)
uniform_variance = statistics.pvariance (list_uniform)
uniform_stddev   = statistics.pstdev (list_uniform)

gauss_mean     = statistics.mean (list_gauss)
gauss_median   = statistics.median (list_gauss)
gauss_variance = statistics.pvariance (list_gauss)
gauss_stddev   = statistics.pstdev (list_gauss)

# printing results
print ("Uniform distribution (%4.1f <= n < %4.1f):" % (n_min, n_max) )
print ("  mean     = %6.2f" % uniform_mean)
print ("  median   = %6.2f" % uniform_median)
print ("  variance = %6.2f" % uniform_variance)
print ("  stddev   = %6.2f" % uniform_stddev)

print ("Gaussian distribution (mean=%4.1f, stddev=%4.1f):" % (mean, stddev) )
print ("  mean     = %6.2f" % gauss_mean)
print ("  median   = %6.2f" % gauss_median)
print ("  variance = %6.2f" % gauss_variance)
print ("  stddev   = %6.2f" % gauss_stddev)
