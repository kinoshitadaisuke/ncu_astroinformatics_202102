#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/24 13:44:56 (CST) daisuke>
#

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing astropy module
import astropy.time

# importing rebound module
import rebound

# date/time now
now = datetime.datetime.now ()

# simulation file
file_sim = 'iss.bin'

# output file
file_output = 'iss.data'

# parameters
year       = 2.0 * numpy.pi
t_epoch    = '2020-12-17 00:00'
t_interval = 0.1 # 0.1 ==> 365.25/(2.0*pi) * 0.1 = 5.81 days
n_output   = 3000

# objects
objects = [
    'Sun',
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto',
    ]

# number of asteroids
n_asteroids = 3000

# reading simulation from file
sim = rebound.Simulation (file_sim)
sim.integrator = 'mercurius'
sim.dt = +0.01
sim.move_to_com ()

# particles
ps = sim.particles

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    fh.write ("#\n")
    fh.write ("# results of orbital integration using rebound\n")
    fh.write ("#\n")
    fh.write ("#   start of integration: %s\n" % now)
    fh.write ("#\n")
    fh.write ("#   list of objects:\n")
    for name in objects:
        fh.write ("#     %s\n" % name)
    fh.write ("#     and %d asteroids\n" % n_asteroids)
    fh.write ("#\n")
    fh.write ("#   format of the data:\n")
    fh.write ("#     JD, date/time, x,y,z,vx,vy,vz of obj1, ")
    fh.write ("x,y,z,vx,vy,vz of obj2, ...\n")
    fh.write ("#\n")

    # epoch
    datetime_epoch = datetime.datetime.fromisoformat (t_epoch)

    # orbital integration
    for i in range (n_output):
        # target time
        time = t_interval * i
        # integration
        sim.integrate (time)
        # time after a step of integration
        datetime_current \
            = datetime_epoch + datetime.timedelta (days=365.25*sim.t/year)
        tastropy_current = astropy.time.Time (datetime_current.isoformat (),
                                              format='isot', scale='utc')
        jd_current = tastropy_current.jd

        # writing data to file
        fh.write ("%.8f|%s" % (jd_current, tastropy_current) )
        for j in range (9 + n_asteroids):
            fh.write ("|%+.15f,%+.15f,%+.15f,%+.15f,%+.15f,%+.15f" \
                      % (ps[j].x, ps[j].y, ps[j].z, \
                         ps[j].vx, ps[j].vy, ps[j].vz) )
        fh.write ("\n")

        # printing status
        if ( (i + 1) % 10 == 0 ):
            print ("  status: %d / %d" % (i + 1, n_output) )
