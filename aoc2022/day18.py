import heapq
import os
from datetime import datetime


def getAdjacent(pos, cubes, maxX, maxY, maxZ):
    adjacent = []
    for d in (-1, 1):
        posX = pos[0] + d
        if posX < -1 or posX > maxX:
            continue

        newPos = (posX, pos[1], pos[2])
        if newPos not in cubes:
            adjacent.append(newPos)
    for d in (-1, 1):
        posY = pos[1] + d
        if posY < -1 or posY > maxY:
            continue
        newPos = (pos[0], posY, pos[2])
        if newPos not in cubes:
            adjacent.append(newPos)
    for d in (-1, 1):
        posZ = pos[2] + d
        if posZ < -1 or posZ > maxZ:
            continue
        newPos = (pos[0], pos[1], posZ)
        if newPos not in cubes:
            adjacent.append(newPos)
    return adjacent


def dijkstraHeap(cubes, maxX, maxY, maxZ, startPos):
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, startPos))

    visited = {}
    unvisited = {}
    dist = {}

    for x in range(-1, maxX + 1):
        for y in range(-1, maxY + 1):
            for z in range(-1, maxZ + 1):
                dist[(x, y, z)] = None
                unvisited[(x, y, z)] = "#"

    dist[startPos] = 0

    while len(queue) > 0:
        __, pos = heapq.heappop(queue)

        if pos in visited:
            continue
        visited[pos] = unvisited.pop(pos)

        currentDistanceToStart = dist.get(pos)
        for adjacentPos in getAdjacent(pos, cubes, maxX, maxY, maxZ):
            if adjacentPos in visited:
                continue

            priority = currentDistanceToStart + 1
            if dist[adjacentPos] is None or priority < dist[adjacentPos]:
                dist[adjacentPos] = priority
                heapq.heappush(queue, (priority, adjacentPos))
    return dist


def parseSurfaces(pos):
    return [",".join(map(str, [pos[0], pos[0], pos[1], pos[1] + 1, pos[2], pos[2] + 1])),
            ",".join(map(str, [pos[0] + 1, pos[0] + 1, pos[1], pos[1] + 1, pos[2],
                               pos[2] + 1])),
            ",".join(map(str, [pos[0], pos[0] + 1, pos[1], pos[1], pos[2], pos[2] + 1])),
            ",".join(map(str, [pos[0], pos[0] + 1, pos[1] + 1, pos[1] + 1, pos[2],
                               pos[2] + 1])),
            ",".join(map(str, [pos[0], pos[0] + 1, pos[1], pos[1] + 1, pos[2], pos[2]])),
            ",".join(map(str, [pos[0], pos[0] + 1, pos[1], pos[1] + 1, pos[2] + 1,
                               pos[2] + 1]))]


def puzzleA(lines):
    cubes = []
    allAreas = {}
    for line in lines:
        pos = tuple(map(int, line.strip().split(",")))
        surfaces = parseSurfaces(pos)
        for area in surfaces:
            allAreas.setdefault(area, 0)
            allAreas[area] += 1
        cubes.append((pos, surfaces))

    sideCount = 0
    for pos, surfaces in cubes:
        for area in surfaces:
            if allAreas[area] == 1:
                sideCount += 1

    return sideCount


def puzzleB(lines):
    cubes = {}
    allAreas = {}

    for line in lines:
        pos = tuple(map(int, line.strip().split(",")))
        cubes[pos] = "#"

    maxX = max([pos[0] for pos in cubes.keys()]) + 1
    maxY = max([pos[1] for pos in cubes.keys()]) + 1
    maxZ = max([pos[2] for pos in cubes.keys()]) + 1

    dist = dijkstraHeap(cubes, maxX, maxY, maxZ, (0, 0, 0))
    positions = [key for key, value in dist.items() if value is None and value not in cubes]

    newCubes = []
    for pos in positions:
        surfaces = parseSurfaces(pos)
        for area in surfaces:
            allAreas.setdefault(area, 0)
            allAreas[area] += 1
        newCubes.append((pos, surfaces))

    sideCount = 0
    for pos, surfaces in newCubes:
        for area in surfaces:
            if allAreas[area] == 1:
                sideCount += 1

    return sideCount


if __name__ == '__main__':
    day = "18"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)

    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    start = datetime.now()
    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    stop = datetime.now()
    print(a)
    print(b)
    print("time: {0}".format(stop - start))
    assert a == 4370
    assert b == 2458
