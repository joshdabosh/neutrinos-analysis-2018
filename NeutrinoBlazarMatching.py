from math import *
import json

"""
blazar1 = open("blazar1.json").read()
blazar1 = json.loads(blazar1)
"""

def RatoLon(x):
    h,m,s = x.split()
    return 15*(int(h)+ int(m)/60 + int(s)/3600)

NtrRA = float(input('Enter the Right Ascension of the neutrino event: '))
NtrDE = float(input('Enter the Declination of the neutrino event: '))

blazar1 = [{"ra":"2 34 45", "de" : -85.456, "a": 'bobitybog', "z" : 0.789},{"ra": "2 45 45", "de" : 83.456, "a": 'bobiasdfog', "z" : 2.21}]
#z = velocity/c, velocity = hubbleconstant(roughly 70)*distance

listBlzInfo = []
for blazar in blazar1:
    BlzRA = blazar["ra"]
    BlzDE = float(blazar["de"])
    BlzLon = RatoLon(BlzRA)
    
    BlzName = blazar["a"]

    theta = BlzLon
    alpha = abs(BlzDE) - 90

    
    
    difRA = NtrRA - BlzLon
    difDE = NtrDE - BlzDE
    RS = blazar['z']

    velocity = RS * 2997992458
    radius = velocity/70

    RADistance = difRA/360 * radius * 2 * 3.1415
    DEDistance = difDE/360 * radius * 2 * 3.1415

    distance = (RADistance ** 2 + DEDistance ** 2) ** 0.5

    x = cos(theta)*distance*sin(alpha)
    y = sin(theta)*distance*sin(alpha)
    z = distance*cos(alpha)
    print(x,y,x)       
    listBlzInfo.append({"dist" : distance, "name": BlzName})

smallestdistance = sorted(listBlzInfo, key=lambda x: x["dist"])[0]
print(smallestdistance)


           
