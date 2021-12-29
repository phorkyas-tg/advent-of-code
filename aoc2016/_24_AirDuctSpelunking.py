import heapq
from itertools import permutations


def GetAdjacent(pos, board):
    positions = []
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (pos[0] + x, pos[1] + y) in board:
            positions.append((pos[0] + x, pos[1] + y))
    return positions


def DijkstraHeap(length, startPos):
    """
    Algorithm for finding the shortest weighted path

    https://brilliant.org/wiki/dijkstras-short-path-finder/
    """

    s = {}

    cache = []
    heapq.heapify(cache)
    heapq.heappush(cache, (0, startPos))

    dist = {}
    q = {}
    for pos in length.keys():
        dist[pos] = None
        q[pos] = "#"

    dist[startPos] = 0

    while len(q) > 0 and len(cache) > 0:
        v, pos = heapq.heappop(cache)
        if pos in s:
            continue
        s[pos] = q.pop(pos)

        d = dist.get(pos)
        for u in GetAdjacent(pos, length):
            if u in s:
                continue

            alt = d + length[u]
            if dist[u] is None or alt < dist[u]:
                dist[u] = alt
                heapq.heappush(cache, (alt, u))

    return dist


def GetFewestNumberOfSteps(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    board = {}
    points = {}

    for y, line in enumerate(inputLines):
        for x, char in enumerate(line.strip()):
            if char == "." or char.isdigit():
                board[(x, y)] = 1
            if char.isdigit():
                points[int(char)] = (x, y)

    distances = {}
    for p1, startPos in points.items():
        dist = DijkstraHeap(board, startPos)
        for p2, pos in points.items():
            distances["{0}-{1}".format(p1, p2)] = dist[pos]

    perm = [i for i in list(permutations([i for i in points.keys()])) if i[0] == 0]

    fewestSteps = None
    for p in perm:
        steps = 0
        for i in range(len(p) - 1):
            steps += distances["{0}-{1}".format(p[i], p[i + 1])]
        if fewestSteps is None or steps < fewestSteps:
            fewestSteps = steps

    return fewestSteps


def GetFewestNumberOfStepsReturn(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    board = {}
    points = {}

    for y, line in enumerate(inputLines):
        for x, char in enumerate(line.strip()):
            if char == "." or char.isdigit():
                board[(x, y)] = 1
            if char.isdigit():
                points[int(char)] = (x, y)

    distances = {}
    for p1, startPos in points.items():
        dist = DijkstraHeap(board, startPos)
        for p2, pos in points.items():
            distances["{0}-{1}".format(p1, p2)] = dist[pos]

    perm = [i for i in list(permutations([i for i in points.keys()])) if i[0] == 0]

    fewestSteps = None
    for p in perm:
        steps = 0
        for i in range(len(p) - 1):
            steps += distances["{0}-{1}".format(p[i], p[i + 1])]
        steps += distances["{0}-{1}".format(p[-1], 0)]
        if fewestSteps is None or steps < fewestSteps:
            fewestSteps = steps

    return fewestSteps



