#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:49:36 (CST) daisuke>
#

# data file name
file_data = 'apj480431t2_ascii.txt'

# printing header
print ("# HD61005")
print ("# wavelength in micron, flux in Jy, flux error in Jy")

# opening data file
with open (file_data, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # if the word '+or-' is found, then we process the line
        if ('+or-' in line):
            # splitting data
            data = line.split ('+or-')
            # wavelength and flux
            (wl, flux) = data[0].split ()
            # error of flux
            data2 = data[1].split ()
            flux_error = data2[0]
            source = data2[1]
            # printing data
            print ("%7.3f %7.3f %7.3f # %s" \
                   % (float (wl), float (flux), float (flux_error), source ) )
