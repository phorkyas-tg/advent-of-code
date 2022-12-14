import os


def printRock(rockMap):
    minX = min([pos[0] for pos in rockMap.keys()])
    maxX = max([pos[0] for pos in rockMap.keys()])
    minY = min([pos[1] for pos in rockMap.keys()])
    maxY = max([pos[1] for pos in rockMap.keys()])

    print("")
    for y in range(minY, maxY + 1):
        line = ""
        for x in range(minX, maxX + 1):
            line += rockMap.get((x, y), ".")
        print(line)


def newSand(rockMap, maxY):
    sandPos = (500, 0)

    while True:
        # go one down
        if (sandPos[0], sandPos[1] + 1) not in rockMap:
            sandPos = (sandPos[0], sandPos[1] + 1)
        # go diag left
        elif (sandPos[0] - 1, sandPos[1] + 1) not in rockMap:
            sandPos = (sandPos[0] - 1, sandPos[1] + 1)
        # go diag right
        elif (sandPos[0] + 1, sandPos[1] + 1) not in rockMap:
            sandPos = (sandPos[0] + 1, sandPos[1] + 1)
        # found a resting place
        else:
            rockMap[sandPos] = "o"
            # is the resting place blocking the entrance?
            if sandPos == (500, 0):
                return False
            return True

        # is the sand falling of the cliff?
        if sandPos[1] > maxY:
            return False


def parseRockMap(lines):
    rockMap = {(500, 0): "+"}

    for line in lines:
        coordinats = line.strip().split(" -> ")

        path = []
        for c in coordinats:
            path.append(list(map(int, c.split(","))))

        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]

            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    rockMap[(x, y)] = "#"
    return rockMap


def puzzleA(lines):
    rockMap = parseRockMap(lines)

    maxY = max([pos[1] for pos in rockMap.keys()])

    # optional print the start
    # printRock(rockMap)

    newSandPossible = True
    while newSandPossible:
        newSandPossible = newSand(rockMap, maxY)

    # optional print the result
    # printRock(rockMap)

    return sum([1 for s in rockMap.values() if s == "o"])


def puzzleB(lines):
    rockMap = parseRockMap(lines)

    maxY = max([pos[1] for pos in rockMap.keys()]) + 2
    for x in range(500 - maxY - 1, 500 + maxY + 1):
        rockMap[(x, maxY)] = "#"

    # optional print the start
    # printRock(rockMap)

    newSandPossible = True
    while newSandPossible:
        newSandPossible = newSand(rockMap, maxY)

    # optional print the result
    # printRock(rockMap)

    return sum([1 for s in rockMap.values() if s == "o"])


if __name__ == '__main__':
    day = "14"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 897
    assert b == 26683
