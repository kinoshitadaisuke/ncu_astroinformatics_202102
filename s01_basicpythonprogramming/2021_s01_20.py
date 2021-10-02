#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 13:51:57 (CST) daisuke>
#

# importing pathlib module
import pathlib

# output file name
filename = "primenumbers_2.data"

# constructing a pathlib object
path_primenumbers = pathlib.Path (filename)

# start and end numbers
n_start = 2
n_end   = 10**5

# initialisation of a string to store data
primenumbers = ''

# checking numbers from n_start to n_end
for i in range (n_start, n_end + 1):
    # resetting the parameter "count"
    count = 0
    # examining if the number is divisible by numbers between 2 and (i-1)
    for j in range (2, i):
        # if the number is divisible, then adding 1 to "count"
        if (i % j == 0):
            count += 1
            # if count is >= 1, the number is not a prime number
            break
    # if the number is a prime number, writing the result into the file.
    if (count == 0):
        result = "%d is a prime number.\n" % i
        primenumbers += result

# writing data into a file
path_primenumbers.write_text (primenumbers)
