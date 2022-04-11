#!/usr/bin/env python3

from PIL import Image
import math
import pickle

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


def distance(x1, y1, x2, y2):
    #return civdistance(x1, y1, x2, y2) 
    #return taxidistance(x1, y1, x2, y2) 
    #return dandddistance(x1, y1, x2, y2)
    #return eucliddistance(x1, y1, x2, y2)
    return otherdistance(x1, y1, x2, y2)


def closest(x, y, candidates):
    nearest = sorted(candidates, key=lambda c: distance(x,y,c[0],c[1]))

    return nearest[0]


def color_pixels(cells, pixels):
    num_cells = len(cells)
    width = len(pixels)
    height = len(pixels[0])

    # for each pixel, determine final color

    for x in range(width):
        for y in range(height):
            pixels[x][y] = closest(x, y, cells)

    return pixels


def plot_pixels(pixels, cells):
    width = len(pixels)
    height = len(pixels[0])
    num_cells = len(cells)

    image = Image.new("RGB", (width * 2, height * 2))
    putpixel = image.putpixel

    for x in range(width):
        for y in range(height):
            p = pixels[x][y]
            putpixel((2 * x,     2 * y),     p[-1])
            putpixel((2 * x + 1, 2 * y),     p[-1])
            putpixel((2 * x,     2 * y + 1), p[-1])
            putpixel((2 * x + 1, 2 * y + 1), p[-1])

    # Mark the centers of each cell

    for c in cells:
        putpixel((c[0] * 2 + 1, c[1] * 2 + 1), (0,0,0))
        putpixel((c[0] * 2 + 1, c[1] * 2),     (0,0,0))
        putpixel((c[0] * 2,     c[1] * 2 + 1), (0,0,0))
        putpixel((c[0] * 2,     c[1] * 2),     (0,0,0))

    image.save("VoronoiDiagram%sx%sc%s.png" % (width, height, num_cells), "PNG")
    return image

def main():
    with open('cells.dump', 'rb') as f:
        cells = pickle.load(f)

    width = 200
    height = 200

    pixels = color_pixels(cells,
                          [ [ [] for y in range(height) ] for x in range(width) ])

    return plot_pixels(pixels, cells)

if __name__ == '__main__':
    main()

