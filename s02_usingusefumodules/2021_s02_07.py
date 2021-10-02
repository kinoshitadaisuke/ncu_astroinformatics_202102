#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:01 (CST) daisuke>
#

# importing os module
import os

# current working directory
cwd = os.getcwd ()
print ("current working directory:")
print (cwd)

# environment variable
env_user = os.getenv ('USER')
env_home = os.getenv ('HOME')
print ("environment varialbe \"USER\":", env_user)
print ("environment varialbe \"HOME\":", env_home)

# listdir
dir = '/home'
files = os.listdir (dir)
print ("list of files in the directory \"%s\":" % dir)
print (files)

# mkdir, rmdir, and stat
print ("making a new directory...")
dir_new = '/tmp/new_directory'
os.mkdir (dir_new)
print ("successfully made a new directory!")
os.chdir (dir_new)
cwd = os.getcwd ()
print ("now at the directory", cwd)
statinfo = os.stat (dir_new)
print ("size =", statinfo[6], "byte")
os.rmdir (dir_new)
print ("deleted new directory.")
