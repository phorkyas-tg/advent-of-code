import heapq


def getAdjacent(pos, board):
    positions = []
    # for a dirty hack you can only look right, up and down for this puzzle input
    # and half the execution time
    # this may not work for other puzzle inputs
    # for x, y in [(1, 0), (0, -1), (0, 1)]:
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (pos[0] + x, pos[1] + y) in board:
            positions.append((pos[0] + x, pos[1] + y))
    return positions


def dijkstraHeap(length, maxX, maxY):
    """
    Algorithm for finding the shortest weighted path

    https://brilliant.org/wiki/dijkstras-short-path-finder/
    """

    s = {}

    cache = []
    heapq.heapify(cache)
    heapq.heappush(cache, (0, (0, 0)))

    dist = {}
    q = {}
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            dist[(x, y)] = None
            q[(x, y)] = "#"

    dist[(0, 0)] = 0

    while len(q) > 0:
        v, pos = heapq.heappop(cache)
        if pos in s:
            continue
        s[pos] = q.pop(pos)

        d = dist.get(pos)
        for u in getAdjacent(pos, length):
            if u in s:
                continue

            alt = d + length[u]
            if dist[u] is None or alt < dist[u]:
                dist[u] = alt
                heapq.heappush(cache, (alt, u))

    return dist[(maxX, maxY)]


def dijkstra(board, maxX, maxY):
    """
    Algorithm for finding the shortest weighted path
    This one does not use a heapq so it must make some extra steps
    """
    # start point weight is always 0
    board[(0, 0)] = 0
    distances = {(0, 0): 0}

    adjacentCache = {}
    skipPositions = {}

    distanceChanged = True
    # loop while distances changes
    while distanceChanged:
        distanceChanged = False

        # iterate over every position on the board
        for y in range(maxY + 1):
            for x in range(maxX + 1):
                posChange = False
                currentPos = (x, y)

                if currentPos in skipPositions:
                    continue

                if currentPos not in adjacentCache:
                    adjacentCache[currentPos] = getAdjacent(currentPos, board)

                for ab in adjacentCache.get(currentPos):
                    if ab not in distances:
                        distances[ab] = distances[currentPos] + board[ab]
                        posChange = distanceChanged = True
                    elif distances[currentPos] + board[ab] < distances[ab]:
                        distances[ab] = distances[currentPos] + board[ab]
                        posChange = distanceChanged = True

                # this position has no impact on the adjacent nodes. So in further
                # iterations it can be skipped
                if not posChange:
                    skipPositions[currentPos] = currentPos

    return distances[(maxX, maxY)]


def getBoard(lines, multiply=1):
    board = {}
    maxX = 0
    maxY = 0

    for y, line in enumerate(lines):
        maxY = y if y > maxY else maxY
        for x, char in enumerate(line.strip()):
            maxX = x if x > maxX else maxX
            board[(x, y)] = int(char)

    for y in range(maxY + 1):
        for x in range(maxX + 1):
            for iy in range(1, multiply):
                newPos = (x, y + (iy * (maxY + 1)))
                upperValue = board[x, (y + ((iy - 1) * (maxY + 1)))]
                newValue = upperValue + 1 if upperValue != 9 else 1
                board[newPos] = newValue
    maxY = ((maxY + 1) * multiply) - 1

    for y in range(maxY + 1):
        for x in range(maxX + 1):
            for ix in range(1, multiply):
                newPos = (x + (ix * (maxX + 1)), y)
                leftValue = board[(x + ((ix - 1) * (maxX + 1)), y)]
                newValue = leftValue + 1 if leftValue != 9 else 1
                board[newPos] = newValue
    maxX = ((maxX + 1) * multiply) - 1

    return board, maxX, maxY


def puzzleA(lines):
    board, maxX, maxY = getBoard(lines, multiply=1)
    return dijkstraHeap(board, maxX, maxY)


def puzzleB(lines):
    board, maxX, maxY = getBoard(lines, multiply=5)
    return dijkstraHeap(board, maxX, maxY)


if __name__ == '__main__':
    day = "15"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    from datetime import datetime
    start = datetime.now()
    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    stop = datetime.now()
    print("time: {0}", stop - start)
    print(a)
    print(b)
    assert a == 562
    assert b == 2874
