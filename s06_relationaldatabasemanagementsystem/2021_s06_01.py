#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:46:58 (CST) daisuke>
#

# importing math module
import math

# catalogue file
file_catalogue = 'catalog'

# opening file
fh = open (file_catalogue, 'r')

for line in fh:
    # Harvard Revised Number
    HR = int (line[0:4])
    # Name
    name = line[4:14].strip ()
    if (name == ''):
        name = '___NONE___'
    # Durchmusterung Identification
    DM = line[14:25].strip ()
    if (DM == ''):
        DM = '___NONE___'
    # Henry Draper Catalogue number
    HD = line[25:31].strip ()
    if (HD == ''):
        HD = -1
    else:
        HD = int (HD)
    # SAO Catalogue number
    SAO = line[31:37].strip ()
    if (SAO == ''):
        SAO = -1
    else:
        SAO = int (SAO)
    # FK5 star number
    FK5 = line[37:41].strip ()
    if (FK5 == ''):
        FK5 = -1
    else:
        FK5 = int (FK5)
    # IR flag
    IRflag = line[41].strip ()
    if (IRflag == 'I'):
        IRflag = 'Yes'
    else:
        IRflag = 'No'
    # double or multiple star code
    double = line[43].strip ()
    if (double == ''):
        double = '___NONE___'
    # ADS (Aitken's Double Star) designation
    ADS = line[44:49].strip ()
    if (ADS == ''):
        ADS = '___NONE___'
    # variable star ID
    varID = line[51:60].strip ()
    if (varID == ''):
        varID = '___NONE___'
    # RA (J2000)
    RAh = line[75:77].strip ()
    if (RAh == ''):
        continue
    else:
        RAh = int (RAh)
    RAm = int (line[77:79])
    RAs = float (line[79:83])
    # Dec (J2000)
    DECsign = line[83]
    DECd = int (line[84:86])
    DECm = int (line[86:88])
    DECs = int (line[88:90])

    # RA and DEC in string format
    RA_str  = "%02d:%02d:%04.1f" % (RAh, RAm, RAs)
    DEC_str = "%1s%02d:%02d:%02d" % (DECsign, DECd, DECm, DECs)

    # decimal RA and DEC in hr, deg, and radian
    RA_hr  = RAh + RAm / 60.0 + RAs / 3600.0
    RA_deg = RA_hr * 15.0
    RA_rad = RA_deg / 180.0 * math.pi
    DEC_deg = DECd + DECm / 60.0 + DECs / 3600.0
    if (DECsign == '-'):
        DEC_deg *= -1.0
    DEC_rad = DEC_deg / 180.0 * math.pi

    # Galactic longitude
    Glon = float (line[90:96])
    Glat = float (line[96:102])

    # visual magnitude
    Vmag = float (line[102:107])
    Vmag_code = line[107].strip ()
    if (Vmag_code == ''):
        Vmag_code = 'V'

    # (B-V) colour index
    BV = line[109:114].strip ()
    if (BV == ''):
        BV = -99.99
    else:
        BV = float (BV)
    # (U-B) colour index
    UB = line[115:120].strip ()
    if (UB == ''):
        UB = -99.99
    else:
        UB = float (UB)
    # (R-I) colour index
    RI = line[121:126].strip ()
    if (RI == ''):
        RI = -99.99
    else:
        RI = float (RI)

    # SpType
    SpType = line[127:147].strip ()
    if (SpType == ''):
        SpType = '___NONE___'

    # proper motion
    pmRA  = float (line[148:154])
    pmDEC = float (line[154:160])
    pm_total = math.sqrt (pmRA**2 + pmDEC**2)

    # parallax
    parallax = line[161:166].strip ()
    if (parallax == ''):
        parallax = -99.99
    else:
        parallax = float (parallax)

    # radial velocity
    radvel = line[166:170].strip ()
    if (radvel == ''):
        radvel = 999999
    else:
        radvel = float (radvel)

    # rotational velocity
    rotvel = line[176:179].strip ()
    if (rotvel == ''):
        rotvel = 999999
    else:
        rotvel = float (rotvel)

    # magnitude difference of double
    magdiff = line[180:184].strip ()
    if (magdiff == ''):
        magdiff = -99.99
    else:
        magdiff = float (magdiff)

    # separation of double
    sep = line[184:190].strip ()
    if (sep == ''):
        sep = -99.99
    else:
        sep = float (sep)

    print ("HR = %d" % HR)
    print ("  name = \"%s\"" % name)
    print ("  DM = \"%s\"" % DM)
    print ("  HD = %d" % HD)
    print ("  SAO = %d" % SAO)
    print ("  FK5 = %d" % FK5)
    print ("  IR flag = %s" % IRflag)
    print ("  Double = \"%s\"" % double)
    print ("  ADS = \"%s\"" % ADS)
    print ("  varID = \"%s\"" % varID)
    print ("  RA_str  = %s" % RA_str)
    print ("  DEC_str = %s" % DEC_str)
    print ("  RA_deg  = %f" % RA_deg)
    print ("  DEC_deg = %f" % DEC_deg)
    print ("  Glon = %f" % Glon)
    print ("  Glat = %f" % Glat)
    print ("  Vmag = %f" % Vmag)
    print ("  Vmag_code = %s" % Vmag_code)
    print ("  B-V = %f" % BV)
    print ("  U-B = %f" % UB)
    print ("  R-I = %f" % RI)
    print ("  SpType = \"%s\"" % SpType)
    print ("  pmRA  = %f arcsec/yr" % pmRA)
    print ("  pmDEC = %f arcsec/yr" % pmDEC)
    print ("  pm_total = %f arcsec/yr" % pm_total)
    print ("  parallax = %f arcsec" % parallax)
    print ("  radvel = %f km/s" % radvel)
    print ("  rotvel = %f km/s" % rotvel)
    print ("  magdiff = %f" % magdiff)
    print ("  sep = %f arcsec" % sep)

# closing file
fh.close ()
