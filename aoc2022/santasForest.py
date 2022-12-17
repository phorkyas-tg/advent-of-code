import math
import os
from datetime import datetime


def puzzleA(lines):
    return len(lines)


def puzzleB(lines):
    trees = set()
    for line in lines:
        pos = tuple(map(int, line.strip().split(";")))
        trees.add(pos)
    return len(trees)


def puzzleC(lines):
    trees = set()
    for line in lines:
        pos = tuple(map(int, line.strip().split(";")))
        trees.add(pos)

    xmin = min([pos[0] for pos in trees])
    xmax = max([pos[0] for pos in trees])
    ymin = min([pos[1] for pos in trees])
    ymax = max([pos[1] for pos in trees])

    area = abs(xmax + 1 - xmin) * abs(ymax + 1 - ymin)
    area -= len(trees)
    return math.ceil(area / 13)


def countAdjacent(pos, trees):
    count = 0
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == 0 and y == 0:
                continue
            if (pos[0] + x, pos[1] + y) in trees:
                count += 1
    return count


def grow(trees, xmin, xmax, ymin, ymax):
    newTrees = dict()
    countCutDown = 0

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            pos = (x, y)
            count = countAdjacent(pos, trees)
            if pos in trees and count in (2, 3):
                newTrees[pos] = "#"
            elif pos in trees and count not in (2, 3):
                countCutDown += 1
            elif pos not in trees and count == 3:
                newTrees[pos] = "#"

    return newTrees, countCutDown


def printTrees(trees):
    xmin = min([pos[0] for pos in trees]) - 2
    xmax = max([pos[0] for pos in trees]) + 2
    ymin = min([pos[1] for pos in trees]) - 2
    ymax = max([pos[1] for pos in trees]) + 2

    for y in range(ymin, ymax):
        line = "{0}".format(y)
        for x in range(xmin, xmax):
            line += trees.get((x, y), ".")

        print(line)
    print("")


def puzzleD(lines):
    trees = dict()
    for line in lines:
        pos = tuple(map(int, line.strip().split(";")))
        trees[pos] = "#"

    xmin = min([pos[0] for pos in trees])
    xmax = max([pos[0] for pos in trees])
    ymin = min([pos[1] for pos in trees])
    ymax = max([pos[1] for pos in trees])

    i = 1
    while True:
        newTrees, __ = grow(trees, xmin, xmax, ymin, ymax)
        if list(sorted(trees.keys())) == list(sorted(newTrees.keys())):
            break
        trees = newTrees
        i += 1

    return i


def puzzleE(lines):
    trees = dict()
    for line in lines:
        pos = tuple(map(int, line.strip().split(";")))
        trees[pos] = "#"

    xmin = min([pos[0] for pos in trees])
    xmax = max([pos[0] for pos in trees])
    ymin = min([pos[1] for pos in trees])
    ymax = max([pos[1] for pos in trees])

    count = 0
    while True:
        newTrees, countCutDown = grow(trees, xmin, xmax, ymin, ymax)
        if list(sorted(trees.keys())) == list(sorted(newTrees.keys())):
            break
        trees = newTrees
        count += countCutDown

    return count


def puzzleF(lines):
    trees = dict()

    for line in lines:
        pos = tuple(map(int, line.strip().split(";")))
        if pos[1] not in (-3, -1):
            trees[pos] = "#"

    i = 0
    xmin = min([pos[0] for pos in trees])
    xmax = max([pos[0] for pos in trees])
    ymin = min([pos[1] for pos in trees])
    ymax = max([pos[1] for pos in trees])

    while True:
        if i == 150:
            break

        newTrees, __ = grow(trees, xmin, xmax, ymin, ymax)

        trees = newTrees
        i += 1

    return len(trees.keys())


def puzzleG(lines):
    trees = dict()
    count = 0

    doubles = []

    for line in lines:
        pos = tuple(map(int, line.strip().split(";")))
        if pos[1] not in (-3, -1):
            trees[pos] = "#"
        elif pos not in doubles:
            count += 1
            doubles.append(pos)

    i = 0
    xmin = min([pos[0] for pos in trees])
    xmax = max([pos[0] for pos in trees])
    ymin = min([pos[1] for pos in trees])
    ymax = max([pos[1] for pos in trees])

    while True:
        if i == 150:
            break

        newTrees, countCutDown = grow(trees, xmin, xmax, ymin, ymax)
        count += countCutDown

        trees = newTrees
        i += 1

    return count


if __name__ == '__main__':
    day = "01"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format("santasForest")
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    start = datetime.now()
    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    c = puzzleC(inputLines)
    d = puzzleD(inputLines)
    e = puzzleE(inputLines)
    f = puzzleF(inputLines)
    g = puzzleG(inputLines)
    stop = datetime.now()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print("time: {0}".format(stop - start))
    assert a == 255
    assert b == 175
    assert c == 47
    assert d == 52
    assert e == 2097
    assert f == 86
    assert g == 6010
