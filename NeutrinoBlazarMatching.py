from math import *
import json

blazar1 = open("data/blazar2.json").read()
blazar1 = json.loads(blazar1)

"""
    difRA = n_beta - b_beta
    difDE = n_alpha - b_alpha

    n_b_distance = (difRA ** 2 + difDE** 2) ** 0.5
"""

"""


"""

def RatoLon(x):
    print(x)
    h,m,s = x.split()
    return 15*(int(h.lstrip('0'))+ int(m.lstrip('0'))/60 + int(s.lstrip('0'))/3600)

def getCoords(alpha, beta, r):
    alpha, beta = alpha*pi/180, beta*pi/180
    x = r * sin(alpha) * cos(beta)
    y = r * sin(beta) * sin(alpha)
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

def main():
    NtrRA = input('Enter the Right Ascension of the neutrino event (HH MM SS): ')
    NtrDE = float(input('Enter the Declination of the neutrino event (degrees): '))

    #blazar1 = [{"ra":"2 34 45", "de" : -85.456, "a": 'bobitybog', "z" : 0.789},{"ra": "2 45 45", "de" : 83.456, "a": 'bobiasdfog', "z" : 2.21}]
    #z = velocity/c, velocity = hubbleconstant(roughly 70)*distance

    if NtrDE < 0:
        n_alpha = abs(float(NtrDE)) + 90

    else:
        n_alpha = 90 - abs(float(NtrDE))

    n_beta = float(NtrRA)

    n_vector = getCoords(n_alpha, n_beta, 1)
    print(n_vector)
    print("ready")

    listBlzInfo = []
    for blazar in blazar1:
        b_beta = float(blazar["ra"])
        b_alpha = float(blazar["de"])

        b_redshift = blazar['z']

        if float(b_redshift) <= 0:
            continue
                    
        b_name = blazar["a"]

        b_mag = float(b_redshift) * 2997992458 / 70

        if b_alpha < 0:
            b_alpha = abs(b_alpha) + 90

        else:
            b_alpha = 90 - abs(b_alpha)

        b_vector = getCoords(b_alpha, b_beta, b_mag)

        n_b_distance = getVectorDist(b_vector, n_vector)
        
        listBlzInfo.append({"dist" : n_b_distance, "blazar":blazar, "b_vec": b_vector})

    possibles = sorted(listBlzInfo, key=lambda x: x["dist"])
    print(*possibles[:10], sep = "\n\n")

main()
