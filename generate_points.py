#!/usr/bin/env python3

import random
import pickle

def generate_cells(width, height, num_cells):
    cells = []
    for i in range(num_cells):
        cell = [random.randrange(width),
                random.randrange(height),
                (random.randrange(256),
                 random.randrange(256),
                 random.randrange(256))]
        cells.append(cell)

    return cells

def main():
    cells = generate_cells(200, 200, 150)
    with open('cells.dump', 'wb') as f:
        pickle.dump(cells, f)


if __name__ == '__main__':
    main()

