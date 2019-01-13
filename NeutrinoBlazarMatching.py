from math import pi
import json

"""
blazar1 = open("blazar1.json").read()
blazar1 = json.loads(blazar1)
"""

try:
    NtrRA = float(input('Enter the Right Ascension of the neutrino event: '))
    NtrDE = float(input('Enter the Declination of the neutrino event: '))

    blazar1 = [{"ra":56.24730, "de" : -85.456, "a": 'bobitybog', "z" : 0.789},{"ra": 186.24730, "de" : 83.456, "a": 'bobiasdfog', "z" : 2.21}]

    listBlzInfo = []
    for blazar in blazar1:
        BlzRA = float(blazar["ra"])
        BlzDE = float(blazar["de"])
        BlzName = blazar["a"]

        difRA = NtrRA - BlzRA
        difDE = NtrDE - BlzDE
        z = blazar['z']

        velocity = z * 2997992458
        radius = velocity/70

        RADistance = difRA/360 * radius * 2 * math.pi
        DEDistance = difDE/360 * radius * 2 * math.pi

        distance = (RADistance ** 2 + DEDistance ** 2) ** 0.5
        listBlzInfo.append({"dist" : distance, "name": BlzName})

    smallestdistance = sorted(listBlzInfo, key=lambda x: x["dist"])[0]
    print(smallestdistance)

except Exception as e:
    print(e)

           

