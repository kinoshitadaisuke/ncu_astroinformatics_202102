#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:40:23 (CST) daisuke>
#

# input file name
file_input = 'site.data'

# output file name
file_output = 'site_2.data'

# opening a file for reading
fh_read = open (file_input, 'r')

# opening a file for writing
fh_write = open (file_output, 'w')

# writing a header to output file
header = "# site, lon, lon (deg), lat, lat (deg), altitude, timezone\n"
fh_write.write (header)

# reading input file line-by-line
for line in fh_read:
    # if the line starts with '#', skip the line
    if (line[0] == '#'):
        continue

    # splitting the data
    (site, lon_ddmmss, lat_ddmmss, altitude, timezone) = line.split ()

    # calculating longitude in decimal degree
    lon_sign = lon_ddmmss[0]
    (lon_dd, lon_mm, lon_ss) = lon_ddmmss[1:].split (':')
    lon_d = int (lon_dd)
    lon_m = int (lon_mm)
    lon_s = float (lon_ss)
    if (lon_sign == '-'):
        lon_deg = (lon_d + lon_m / 60.0 + lon_s / 3600.0) * (-1.0)
    else:
        lon_deg = (lon_d + lon_m / 60.0 + lon_s / 3600.0)

    # calculating latitude in decimal degree
    lat_sign = lat_ddmmss[0]
    (lat_dd, lat_mm, lat_ss) = lat_ddmmss[1:].split (':')
    lat_d = int (lat_dd)
    lat_m = int (lat_mm)
    lat_s = float (lat_ss)
    if (lat_sign == '-'):
        lat_deg = (lat_d + lat_m / 60.0 + lat_s / 3600.0) * (-1.0)
    else:
        lat_deg = (lat_d + lat_m / 60.0 + lat_s / 3600.0)

    # writing data to output file
    data = "%-8s  %10s  %+10.5f  %10s  %+10.5f  %4d  %+3d\n" \
        % (site, lon_ddmmss, lon_deg, lat_ddmmss, lat_deg, \
           float (altitude), float (timezone) )
    fh_write.write (data)
        
# closing files
fh_read.close ()
fh_write.close ()
