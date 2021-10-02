#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:51:25 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# command-line argument analysis
parser = argparse.ArgumentParser (description='Phase Dispersion Minimization')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input file name')
parser.add_argument ('-o', type=str, default="out.data", \
                     help='output file name')
parser.add_argument ('-s', type=float, default=10.0, \
                     help='shortest trial period in min')
parser.add_argument ('-l', type=float, default=300.0, \
                     help='longest trial period in min')
parser.add_argument ('-d', type=float, default=0.1, \
                     help='step size of trial period in min')
parser.add_argument ('-n', type=int, default=10, help='number of bins')
args = parser.parse_args()

# input file name
file_in = args.i

# output file name
file_out = args.o

# shortest trial period
period_min_min = args.s
period_min_day = period_min_min / (60.0 * 24.0)

# longest trial period
period_max_min = args.l
period_max_day = period_max_min / (60.0 * 24.0)

# step size of trial period
step_min = args.d
step_day = step_min / (60.0 * 24.0)

# number of bins
n_bins = args.n

# empty numpy arrays for storing data
data_mjd = numpy.array ([])
data_mag = numpy.array ([])
data_err = numpy.array ([])

# opening file for reading
with open (file_in, 'r') as fh_in:
    # reading data line-by-line
    for line in fh_in:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (datetime, mjd_str, mag_str, err_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        err = float (err_str)
        # appending the data at the end of numpy arrays
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)
        data_err = numpy.append (data_err, err)

# opening file for writing
with open (file_out, 'w') as fh_out:
    # writing header to output file
    header  = "# input file = %s\n" % file_in
    header += "# output file = %s\n" % file_out
    header += "# shortest trial period = %f min\n" % period_min_min
    header += "# longest trial period = %f min\n" % period_max_min
    header += "# step size of trial period = %f min\n" % step_min
    header += "# number of bins = %d\n" % n_bins
    header += "#\n"
    header += "# trial period (day), trial period (hr), trial period (min), "
    header += "total variance\n"
    header += "#\n"
    fh_out.write (header)

    # initial value of trial period
    period_day = period_min_day

    # period search
    while (period_day < period_max_day):
        # calculation of phase with assumed period
        data_phase = numpy.array ([])
        for i in range ( len (data_mjd) ):
            phase = data_mjd[i] / period_day - int (data_mjd[i] / period_day)
            data_phase = numpy.append (data_phase, phase)

        # initialization of parameters
        total_variance = 0.0

        # calculation of variance
        for i in range (n_bins):
            # range of bin
            bin_min = i / n_bins
            bin_max = (i + 1) / n_bins

            # finding data within the bin
            data_bin = numpy.array ([])
            for j in range ( len (data_phase) ):
                if ( (data_phase[j] >= bin_min) and (data_phase[j] < bin_max) ):
                    data_bin = numpy.append (data_bin, data_mag[j])

            # if no data in the bin, then we skip.
            if (len (data_bin) == 0):
                continue

            # variance
            variance_in_bin = numpy.var (data_bin)
            # sum of variance
            total_variance += variance_in_bin

        # writing data to file
        output = "%12.10f %12.8f %12.6f %10.6f\n" \
            % (period_day, period_day * 24.0, period_day * 24.0 * 60.0, \
               total_variance)
        fh_out.write (output)

        # next trial period
        period_day += step_day
