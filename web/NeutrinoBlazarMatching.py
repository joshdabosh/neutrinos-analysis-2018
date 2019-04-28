from math import *
import os
import json

blazar1 = open(os.path.join(os.getcwd(),"blazar2.json")).read()
blazar1 = json.loads(blazar1)

def RatoLon(x):
    """
    Converts right ascension given in HH:MM:SS to Longitude (degrees).
    
    Keyword arguments:
    x -- the right ascension value (HH:MM:SS)
    """
    
    h,m,s = x.split()
    return 15*(int(h.lstrip('0'))+ int(m.lstrip('0'))/60 + int(s.lstrip('0'))/3600)

def getCoords(alpha, theta, r):
    """
    Returns a vector in cartesian coordinates given two angles and the magnitude
    of the vector.
    
    Keyword arguments:
    alpha -- the angle of a vector from the positive y axis (in radians)
    theta -- the angle of a vector from the negative x axis (in radians)
    """
    
    alpha, theta = alpha*pi/180, theta*pi/180
    x = r * sin(alpha) * cos(theta)
    y = r * sin(theta) * sin(alpha)
    z = r * cos(alpha)

    return x, y, z

def calcMagnitude(x, y, z):
    """
    Returns the magnitude of a vector's elements.
    
    Can be called with calcMagnitude(*vector) when vector has 3 elements
    
    Keyword arguments:
    x -- the first element in the vector
    y -- the second element in the vector
    z -- the third element in the vector
    """
    
    return sqrt(x**2 + y**2 + z**2)

def getVectorDist(b, n):
    """
    Returns the distance between two vectors by projecting one onto the other.
    
    Keyword arguments:
    b -- the blazar vector
    n -- the neutrino vector
    """
    
    factor = abs(sum(map(lambda x: x[0]*x[1], zip(b, n))))
    
    projection = tuple(map(lambda x: x * factor, n))

    vect_diff = tuple(map(lambda x: x[0] - x[1], zip(b, projection)))    

    ret_dist = calcMagnitude(*vect_diff)
    return ret_dist

def angular_comparison(NtrRA, NtrDE):
    """
    Compares blazars based on the angular difference to the neutrino event.

    Keyword arguments:
    NtrRA -- The right ascension of the neutrino event
    NtrDE -- The declination of the neutrino event
    """
    
    if NtrDE < 0:
        n_alpha = abs(float(NtrDE)) + 90

    else:
        n_alpha = 90 - abs(float(NtrDE))

    n_theta = float(NtrRA)

    listBlzInfo = []
    for blazar in blazar1:
        b_theta = float(blazar["ra"])
        b_alpha = float(blazar["de"])
                    
        b_name = blazar["a"]

        if b_alpha < 0:
            b_alpha = abs(b_alpha) + 90

        else:
            b_alpha = 90 - abs(b_alpha)

        difRA = n_theta - b_theta
        difDE = n_alpha - b_alpha

        n_b_distance = sqrt(difRA ** 2 + difDE ** 2)
        
        listBlzInfo.append({"angular_dist" : n_b_distance, "blazar":blazar})

    possibles = sorted(listBlzInfo, key=lambda x: x["angular_dist"])

    return possibles[:10]

def vectors_comparison(NtrRA, NtrDE):
    """
    Compares blazars based on the vector distance difference to the neutrino
    event.

    Keyword arguments:
    NtrRA -- The right ascension of the neutrino event
    NtrDE -- The declination of the neutrino event
    """

    if NtrDE < 0:
        n_alpha = abs(float(NtrDE)) + 90

    else:
        n_alpha = 90 - abs(float(NtrDE))

    n_theta = float(NtrRA)

    n_vector = getCoords(n_alpha, n_theta, 1)

    listBlzInfo = []
    for blazar in blazar1:
        b_theta = float(blazar["ra"])
        b_alpha = float(blazar["de"])

        b_redshift = blazar['z']

        if float(b_redshift) <= 0.25:
            continue
                    
        b_name = blazar["a"]

        b_mag = float(b_redshift) * 2997992.458 / 70

        if b_alpha < 0:
            b_alpha = abs(b_alpha) + 90

        else:
            b_alpha = 90 - abs(b_alpha)

        b_vector = getCoords(b_alpha, b_theta, b_mag)

        n_b_distance = getVectorDist(b_vector, n_vector)
        
        listBlzInfo.append({"n_b_dist" : n_b_distance, "e_b_dist": b_mag,"blazar":blazar, "b_vec": b_vector})

    possibles = sorted(listBlzInfo, key=lambda x: x["n_b_dist"])

    return possibles[:10]

def main(n_ra, n_de, verbose=True):
    """
    Runs both of the functions and returns their data / prints them based on
    if parameter verbose is true.

    Keyword arguments:
    n_ra -- the right ascension of the neutrino event in degrees
    n_de -- the declination of the neutrino event in degrees
    verbose -- if the program should print the results (true) or return them (false) -- default: True
    """
    
    n_ra, n_de = float(n_ra), float(n_de)
    
    a_closest = angular_comparison(n_ra, n_de)
    v_closest = vectors_comparison(n_ra, n_de)

    intersects = []

    if a_closest[0]["blazar"]["a"] == v_closest[0]["blazar"]["a"]:
        temp = dict(a_closest[0])
        temp["n_b_dist"] = v_closest[0]["n_b_dist"]
        temp["e_b_dist"] = v_closest[0]["e_b_dist"]

        top_both = [temp]

    else:
        top_both = []

    if not verbose:
        return a_closest, v_closest, top_both

    blazarTemplateTotal = """
{name: <20}{ra: <20}{de: <20}{ann_dist: <30}{n_b_dist: <30}{e_b_dist: <30}
    """.strip()

    blazarTemplateAnn = """
{name: <20}{ra: <20}{de: <20}{ann_dist: <30}
    """.strip()

    blazarTemplateVec = """
{name: <20}{ra: <20}{de: <20}{n_b_dist: <30}{e_b_dist: <30}
    """.strip()
    
    print()
    print()

    print("Closest according to both lists (intersection of both):")

    print("-"*len("Closest according to both lists (intersection of both):"))

    print()
    print(blazarTemplateTotal.format(
        name="Blazar Name",
        ra="Right Ascension",
        de="Declination",
        ann_dist="Angular Distance",
        n_b_dist="Neutrino-Blazar distance",
        e_b_dist="Earth-Blazar distance"
    ))

    for b in intersects:
        print(blazarTemplateTotal.format(
            name=b["blazar"]["a"],
            ra=b["blazar"]["ra"],
            de=b["blazar"]["de"],
            ann_dist=b["angular_dist"],
            n_b_dist=b["n_b_dist"],
            e_b_dist=b["e_b_dist"]
        ))
        
    ###
        
    print()
    print()

    print("Closest according to angular comparisons:")

    print("-"*len("Closest according to angular comparisons:"))

    print()
    print(blazarTemplateAnn.format(
        name="Blazar Name",
        ra="Right Ascension",
        de="Declination",
        ann_dist="Angular Distance"
    ))

    for b in a_closest:
        print(blazarTemplateAnn.format(
            name=b["blazar"]["a"],
            ra=b["blazar"]["ra"],
            de=b["blazar"]["de"],
            ann_dist=b["angular_dist"]
    ))

    print()
    print()

    ###

    print("Closest according to vector comparisons: ", end="\n")

    print("-"*len("Closest according to vector comparisons:"))

    print(blazarTemplateVec.format(
        name="Blazar Name",
        ra="Right Ascension",
        de="Declination",
        n_b_dist="Neutrino-Blazar distance",
        e_b_dist="Earth-Blazar distance"
    ))

    for b in v_closest:
        print(blazarTemplateVec.format(
            name=b["blazar"]["a"],
            ra=b["blazar"]["ra"],
            de=b["blazar"]["de"],
            n_b_dist=b["n_b_dist"],
            e_b_dist=b["e_b_dist"]
    ))
