#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:39:46 (CST) daisuke>
#

# initialisation of a list
list_a = [ 0.1, 2.3, 4.5, 5.6, 6.7, 8.9, 10.1 ]

# printing the list "list_a"
print (list_a)

# printing an element of the list "list_a"
print ("list_a[0] =", list_a[0])
print ("list_a[3] =", list_a[3])
print ("list_a[-2] =", list_a[-2])

# printing elements of the list "list_a" using slicing
print ("list_a[2:5] =", list_a[2:5])

# printing elements of the list "list_a" using slicing
print ("list_a[4:] =", list_a[4:])

# printing elements of the list "list_a" using slicing
print ("list_a[:3] =", list_a[:3])

# adding 1.23 to each element of "list_a"
for i in range ( len (list_a) ):
    list_a[i] += 1.23

# printing the list "list_a"
print (list_a)
