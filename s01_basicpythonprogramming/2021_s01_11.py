#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:39:43 (CST) daisuke>
#

# constant
i = 0
n = 30

# a loop using control flow statement "while"
while (True):
    # condition to stop the loop
    if (i > n):
        break
    # adding 1 to i
    i += 1
    # if the number is not divisible by 3, go to next
    if (i % 3 != 0):
        continue
    # printing the number
    print (i)
