#!/usr/bin/env python3

import math
import random

def eucliddistance(x1, y1, x2, y2):
    xdist = abs(x1 - x2)
    ydist = abs(y1 - y2)
    return math.sqrt( (xdist ** 2) + (ydist ** 2) )

def taxidistance(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2))

def civdistance(x1, y1, x2, y2):
    return (max(abs(x1 - x2), abs(y1 - y2)))

def dandddistance(x1, y1, x2, y2):
    mindist = min(abs(x1 - x2), abs(y1 - y2))
    maxdist = max(abs(x1 - x2), abs(y1 - y2))
    return ((maxdist - mindist) + (1.5 * mindist))

def otherdistance(x1, y1, x2, y2):
    mindist = min(abs(x1 - x2), abs(y1 - y2))
    maxdist = max(abs(x1 - x2), abs(y1 - y2))
    return ((maxdist - mindist) + (1.4 * mindist))


def main():
    # generate a list of 300 random points

    points = [ (random.randrange(200), random.randrange(200))
               for x in range(300) ]

    # get the euclidean distance from origin to each point

    base_distances = [ eucliddistance(0,0,p[0],p[1])
                       for p in points ]

    # now, we run through each of the other distance
    # measures, and take the total differences

    taxidiff = 0
    civdiff = 0
    dandddiff = 0
    otherdiff = 0

    for i in range(len(points)):
        p = points[i]
        bd = base_distances[i]

        taxidiff  += abs(taxidistance(0,0,p[0],p[1]) - bd)
        civdiff   += abs(civdistance(0,0,p[0],p[1]) - bd)
        dandddiff += abs(dandddistance(0,0,p[0],p[1]) - bd)
        otherdiff += abs(otherdistance(0,0,p[0],p[1]) - bd)

    print("taxi  diff: %d" % (taxidiff))
    print("civ   diff: %d" % (civdiff))
    print("dandd diff: %d" % (dandddiff))
    print("other diff: %d" % (otherdiff))


if __name__ == '__main__':
    main()
