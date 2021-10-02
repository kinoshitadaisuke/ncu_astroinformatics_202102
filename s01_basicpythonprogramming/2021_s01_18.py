#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:17 (CST) daisuke>
#

# output file name
filename = "primenumbers.data"

# opening file for writing
fh = open (filename, 'w')

# start and end numbers
n_start = 2
n_end   = 100

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
        fh.write (result)

# closing file
fh.close ()
