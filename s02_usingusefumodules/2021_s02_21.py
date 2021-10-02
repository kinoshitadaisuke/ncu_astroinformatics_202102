#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:52 (CST) daisuke>
#

# importing pathlib module
import pathlib

# file
file = '/etc/fstab'

# constructing pathlib object
path_file = pathlib.Path (file)

# existence test
print ('file "%s" exists?: %s' % (path_file, path_file.exists () ) )

# file size
info = path_file.stat ()
print ("size of %s = %d byte" % (path_file, int (info[6]) ) )

# reading file
with path_file.open () as fh:
    lines = fh.readlines ()

# printing file contents    
for line in lines:
    print (line, end='')
    
