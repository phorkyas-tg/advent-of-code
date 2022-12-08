import os

def puzzleA(lines):
    trees = {}
    visibleTrees = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            trees[(x, y)] = int(c)
            visibleTrees[(x, y)] = 1

    xMax, yMax = max(trees.keys())

    for y in range(yMax + 1):
        highestTree = -1
        for x in range(xMax + 1):
            value = trees[(x, y)]

            if x == 0 or x == xMax or value > highestTree:
                visibleTrees[(x, y)] = 0

            if highestTree < value:
                highestTree = value
            if value == 9:
                break

    for y in range(yMax + 1):
        highestTree = -1
        for x in range(xMax, 0 - 1, -1):
            value = trees[(x, y)]

            if x == 0 or x == xMax or value > highestTree:
                visibleTrees[(x, y)] = 0

            if highestTree < value:
                highestTree = value
            if value == 9:
                break

    for x in range(xMax + 1):
        highestTree = -1
        for y in range(yMax + 1):
            value = trees[(x, y)]

            if y == 0 or y == yMax or value > highestTree:
                visibleTrees[(x, y)] = 0

            if highestTree < value:
                highestTree = value
            if value == 9:
                break

    for x in range(xMax + 1):
        highestTree = -1
        for y in range(yMax, 0 - 1, -1):
            value = trees[(x, y)]

            if y == 0 or y == yMax or value > highestTree:
                visibleTrees[(x, y)] = 0

            if highestTree < value:
                highestTree = value
            if value == 9:
                break
        

    return len(visibleTrees.keys()) - sum(visibleTrees.values())


def puzzleB(lines):
    trees = {}
    visibleTrees = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            trees[(x, y)] = int(c)
            visibleTrees[(x, y)] = 0

    xMax, yMax = max(trees.keys())

    for pos, value in trees.items():
        r = l = u = d = 1

        if pos[0] == 0 or pos[0] == xMax or pos[1] == 0 or pos[1] == yMax:
            continue

        for x in range(pos[0] + 1, xMax):
            if value > trees[(x, pos[1])]:
                r += 1
            else:
                break
        
        for x in range(pos[0] - 1, 0, -1):
            if value > trees[(x, pos[1])]:
                l += 1
            else:
                break

        for y in range(pos[1] + 1, yMax):
            if value > trees[(pos[0], y)]:
                d += 1
            else:
                break

        for y in range(pos[1] - 1, 0, -1):
            if value > trees[(pos[0], y)]:
                u += 1
            else:
                break

        visibleTrees[pos] = r * l * u * d

    return max(visibleTrees.values())


if __name__ == '__main__':
    day = "08"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding = 'utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 1794
    assert b == 199272
