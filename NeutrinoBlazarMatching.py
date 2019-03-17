from math import *
import json

blazar1 = open("data/blazar2.json").read()
blazar1 = json.loads(blazar1)

def RatoLon(x):
    print(x)
    h,m,s = x.split()
    return 15*(int(h.lstrip('0'))+ int(m.lstrip('0'))/60 + int(s.lstrip('0'))/3600)

def getCoords(alpha, theta, r):
    alpha, theta = alpha*pi/180, theta*pi/180
    x = r * sin(alpha) * cos(theta)
    y = r * sin(theta) * sin(alpha)
    z = r * cos(alpha)

    return x, y, z

def calcMagnitude(x, y, z):
    return sqrt(x**2 + y**2 + z**2)

def getVectorDist(b, n):
    factor = abs(sum(map(lambda x: x[0]*x[1], zip(b, n))))
    
    projection = tuple(map(lambda x: x * factor, n))

    vect_diff = tuple(map(lambda x: x[0] - x[1], zip(b, projection)))    

    ret_dist = calcMagnitude(*vect_diff)
    return ret_dist

def angular_comparison(NtrRA, NtrDE):
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
    #print(*possibles[:10], sep = "\n\n")

    return possibles[:10]

def vectors_comparison(NtrRA, NtrDE):
    #NtrRA = input('Enter the Right Ascension of the neutrino event (HH MM SS): ')
    #NtrDE = float(input('Enter the Declination of the neutrino event (degrees): '))

    #blazar1 = [{"ra":"2 34 45", "de" : -85.456, "a": 'bobitybog', "z" : 0.789},{"ra": "2 45 45", "de" : 83.456, "a": 'bobiasdfog', "z" : 2.21}]
    #z = velocity/c, velocity = hubbleconstant(roughly 70)*distance

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

        b_mag = float(b_redshift) * 2997992458 / 70

        if b_alpha < 0:
            b_alpha = abs(b_alpha) + 90

        else:
            b_alpha = 90 - abs(b_alpha)

        b_vector = getCoords(b_alpha, b_theta, b_mag)

        n_b_distance = getVectorDist(b_vector, n_vector)
        
        listBlzInfo.append({"relative_dist" : n_b_distance, "blazar":blazar, "b_vec": b_vector})

    possibles = sorted(listBlzInfo, key=lambda x: x["relative_dist"])
    #print(*possibles[:10], sep = "\n\n")

    return possibles[:10]

def main(n_ra, n_de):
    a_closest = angular_comparison(n_ra, n_de)
    v_closest = vectors_comparison(n_ra, n_de)

    intersects = [a.update({"relative_dist":b["relative_dist"]}) for a, b in zip(a_closest, v_closest) if a["blazar"]["a"] == b["blazar"]["a"]]

    print()
    print()

    print("Closest according to both lists (intersection of both): ", end="")

    print(intersects)

    print()

    print("Closest according to angular comparisons: ", end="")

    print(a_closest[:2])

    print()

    print("Closest according to vector5 comparisons: ", end="")

    print(v_closest[:2])
















