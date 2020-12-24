tileDirs = {"nw": (-1, -1), "ne": (1, -1), "se": (1, 1), "sw": (-1, 1), "e": (2, 0), "w": (-2, 0)}


def ParseBlackTiles(puzzleInput):
    # e, se, sw, w, nw, ne

    blackTiles = {}
    for line in puzzleInput.splitlines():
        i = 0
        currentPos = (0, 0)
        while i < len(line):
            if line[i:i+2] in tileDirs:
                direction = tileDirs[line[i:i+2]]
                i += 1
            else:
                direction = tileDirs[line[i:i+1]]
            currentPos = (currentPos[0] + direction[0],
                          currentPos[1] + direction[1])
            i += 1

        if currentPos in blackTiles:
            blackTiles.pop(currentPos)
        else:
            blackTiles[currentPos] = 1

    return blackTiles


def CountAdjacentBlackTiles(pos, blackTiles, terminate):
    count = 0
    for p in [(pos[0] + x, pos[1] + y) for x, y in tileDirs.values()]:
        if p in blackTiles:
            count += 1
            if count >= terminate:
                return count
    return count


def SkipOneDay(blackTiles):
    xMin = xMax = yMin = yMax = 0
    for x, y in blackTiles.keys():
        if x > xMax:
            xMax = x
        if x < xMin:
            xMin = x
        if y > yMax:
            yMax = y
        if y < yMin:
            yMin = y

    xMin -= 2
    xMax += 2
    yMin -= 1
    yMax += 1

    newBlackTiles = {}
    for x in range(xMin, xMax + 1):
        for y in range(yMin, yMax + 1):
            count = CountAdjacentBlackTiles((x, y), blackTiles, 3)
            if (x, y) in blackTiles and count in (1, 2):
                newBlackTiles[(x, y)] = 1
            elif (x, y) not in blackTiles and count == 2:
                newBlackTiles[(x, y)] = 1
    return newBlackTiles


def GetBlackTiles(puzzleInput):
    return sum(ParseBlackTiles(puzzleInput).values())


def BlackTilesAfterNDays(puzzleInput):
    blackTiles = ParseBlackTiles(puzzleInput)

    for __ in range(100):
        blackTiles = SkipOneDay(blackTiles)

    return sum(blackTiles.values())
