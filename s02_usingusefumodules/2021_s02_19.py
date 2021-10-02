#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:41:44 (CST) daisuke>
#

# importing datetime module
import datetime

# current time in local time
time_now_local = datetime.datetime.now ()
# current time in UTC
time_now_utc   = datetime.datetime.now (tz=datetime.timezone.utc)

# printing results
print ("local time:  ", time_now_local)
print ("UTC:         ", time_now_utc)

# YYYY/MM/DD hh:mm:ss
YYYY = time_now_local.year
MM   = time_now_local.month
DD   = time_now_local.day
hh   = time_now_local.hour
mm   = time_now_local.minute
ss   = time_now_local.second

# printing results
print ("current time: %04d/%02d/%02d %02d:%02d:%02d" \
       % (YYYY, MM, DD, hh, mm, ss) )
