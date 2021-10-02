#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:05 (CST) daisuke>
#

# importing sys module
import sys

# command-line arguments
print ("len (sys.argv) =", len (sys.argv))
for i in range (len (sys.argv)):
    print ("argv[%d] = %s" % (i, sys.argv[i]) )

# module search path
module_search_path = sys.path
print ("module search path:")
for path in module_search_path:
    print (path)

# exit Python
print ("Now exit from Python.")
sys.exit ()
