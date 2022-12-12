import os
import heapq


def getAdjacent(pos, board):
    positions = []
    ordCurrent = ord(board[pos])
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        newPos = (pos[0] + x, pos[1] + y)

        if newPos not in board:
            continue

        ordNext = ord(board[newPos])
        if ordCurrent - ordNext == -1 or ordCurrent >= ordNext:
            positions.append(newPos)
    return positions


def dijkstraHeap(length, maxX, maxY, startPos):
    """
    Algorithm for finding the shortest weighted path

    https://brilliant.org/wiki/dijkstras-short-path-finder/
    """
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, startPos))

    visited = {}
    unvisited = {}
    dist = {}

    for y in range(maxY + 1):
        for x in range(maxX + 1):
            dist[(x, y)] = None
            unvisited[(x, y)] = "#"

    dist[startPos] = 0

    while len(queue) > 0:
        __, pos = heapq.heappop(queue)

        if pos in visited:
            continue
        visited[pos] = unvisited.pop(pos)

        currentDistanceToStart = dist.get(pos)
        for adjacentPos in getAdjacent(pos, length):
            if adjacentPos in visited:
                continue

            priority = currentDistanceToStart + 1
            if dist[adjacentPos] is None or priority < dist[adjacentPos]:
                dist[adjacentPos] = priority
                heapq.heappush(queue, (priority, adjacentPos))
    return dist


def parseBoard(lines):
    board = dict()
    maxX = 0
    maxY = 0
    startPos = None
    endPos = None

    for y, line in enumerate(lines):
        maxY = y if y > maxY else maxY
        for x, c in enumerate(line.strip()):
            if c == "S":
                startPos = (x, y)
                c = "a"
            if c == "E":
                endPos = (x, y)
                c = "z"
            board[(x, y)] = c
            maxX = x if x > maxX else maxX

    return board, startPos, endPos, maxX, maxY


def puzzleA(lines):
    board, startPos, endPos, maxX, maxY = parseBoard(lines)

    dist = dijkstraHeap(board, maxX, maxY, startPos)
    return dist[endPos]


def puzzleB(lines):
    board, startPos, endPos, maxX, maxY = parseBoard(lines)

    distances = []
    for startPos, value in board.items():
        if value == "a":
            dist = dijkstraHeap(board, maxX, maxY, startPos)
            if dist[endPos] is not None:
                distances.append(dist[endPos])

    return min(distances)


if __name__ == '__main__':
    day = "12"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 383
    assert b == 377
