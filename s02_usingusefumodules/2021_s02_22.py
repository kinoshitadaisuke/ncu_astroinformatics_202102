#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:55 (CST) daisuke>
#

# importing pathlib module
import pathlib

# importing shutil module
import shutil

# file
file_src = '/bin/ls'
file_dst = '/tmp/ls'

# constructing pathlib objects
path_src = pathlib.Path (file_src)
path_dst = pathlib.Path (file_dst)

# copying file
shutil.copy2 (path_src, path_dst)
