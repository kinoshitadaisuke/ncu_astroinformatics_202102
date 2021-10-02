#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/10/02 12:47:01 (CST) daisuke>
#

# importing math module
import math

# catalogue file
file_catalogue = 'catalog'

sql_table = "create table bsc (HR integer primary key, name text, " \
    + "DM text, HD integer, SAO integer, FK5 integer, IRflag text, " \
    + "double text, ADS text, varID text, RA_str text, DEC_str text, " \
    + "RA_hr real, RA_deg real, DEC_deg real, RA_rad real, DEC_rad real, " \
    + "Glon real, Glat real, Vmag real, Vmag_code text, BV real, UB real, " \
    + "RI real, SpType text, pmRA real, pmDEC real, pm_total real, " \
    + "parallax real, radvel real, rotvel real, magdiff real, sep real);"
print (sql_table)

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

    sql_adddata = "insert into bsc values (%d, \"%s\", \"%s\", %d, %d, %d, " \
        % (HR, name, DM, HD, SAO, FK5)
    sql_adddata += "\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", " \
        % (IRflag, double, ADS, varID, RA_str, DEC_str)
    sql_adddata += "%f, %f, %f, %f, %f, %f, %f, " \
        % (RA_hr, RA_deg, DEC_deg, RA_rad, DEC_rad, Glon, Glat)
    sql_adddata += "%f, \"%s\", %f, %f, %f, \"%s\", %f, %f, %f, " \
        % (Vmag, Vmag_code, BV, UB, RI, SpType, pmRA, pmDEC, pm_total)
    sql_adddata += "%f, %f, %f, %f, %f);" \
        % (parallax, radvel, rotvel, magdiff, sep)
    print (sql_adddata)
        
# closing file
fh.close ()
