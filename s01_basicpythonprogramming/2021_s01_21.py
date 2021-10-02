#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 13:52:05 (CST) daisuke>
#

# sample string
sample_string = "National Central University"

# printing a string
print ("sample_string       =", sample_string)

# using slice for a string
print ("sample_string[9:]   =", sample_string[9:])
print ("sample_string[:16]  =", sample_string[:16])
print ("sample_string[9:16] =", sample_string[9:16])

# using replace method
sample_string_2 = sample_string.replace ("Central", "Tsing-Hua")
print ("sample_string_2     =", sample_string_2)
