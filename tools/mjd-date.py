import math

def convert(mjd):
    jd = int(mjd) + 2400001

    F, I = math.modf(jd)
    I = int(I)

    A = math.trunc((I - 1867216.25)/36524.25)

    if I > 2299160:
        B = I + 1 + A - math.trunc(A / 4)

    else:
        B = I

    C = B + 1524
    
    D = math.trunc((C - 122.1) / 365.25)

    E = math.trunc(365.25 * D)

    G = math.trunc((C - E) / 30.6001)

    day = C - E + F - math.trunc(30.6001 * G)

    if G < 13.5:
        month = G - 1

    else:
        month = G - 13

    if month > 2.5:
        year = D - 4716

    else:
        year = D - 4715

    return year, month, day
