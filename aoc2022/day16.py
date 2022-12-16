import os
import re
import heapq
from datetime import datetime


def parse(lines):
    paths = {}
    flowRates = {}
    valves = []
    cachedPaths = {}

    for line in lines:
        flowRate = list(map(int, re.findall('[-+]?[0-9]+', line)))[0]
        valve = line.strip().split("has flow")[0].split()[1].strip()
        flowRates[valve] = flowRate
        valves.append(valve)
        try:
            nextValves = line.strip().split("to valves")[1].strip().split(", ")
        except IndexError:
            nextValves = [line.strip().split("to valve")[1].strip()]

        paths[valve] = nextValves

    for v1 in valves:
        for v2 in valves:
            newPath = dijkstraHeap(paths, startPos=v1, stopPos=v2)
            inBetween = ["__"] * (len(newPath) - 2)
            inBetween.append(newPath[-1])
            cachedPaths[(v1, v2)] = inBetween
    return paths, flowRates, valves, cachedPaths


def dijkstraHeap(paths, startPos, stopPos):
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, startPos))

    dist = {}

    for key in paths:
        dist[key] = (None, None)

    dist[startPos] = (0, None)

    while len(queue) > 0:
        t, valve = heapq.heappop(queue)
        if valve == stopPos:
            break

        currentTime, lastValve = dist.get(valve)

        for nextValve in paths[valve]:
            newTime = currentTime + 1
            if dist[nextValve][0] is None or newTime < dist[nextValve][0]:
                dist[nextValve] = (newTime, valve)
                heapq.heappush(queue, (newTime, nextValve))

    nextValve = stopPos
    path = [nextValve]

    while nextValve != startPos:
        nextValve = dist[nextValve][1]
        path.append(nextValve)
    return path[::-1]


def completePaths(valves, paths, knownPaths, complete, flowRates, pressureCache, maxLength,
                  cachedPaths):
    newKnownPaths = []

    if len(knownPaths) == 0:
        return complete

    for knownPath in knownPaths:
        if len(knownPath) >= maxLength:
            complete.append(knownPath.copy())
            continue

        vis = ",".join(sorted(set([valve for valve in knownPath if valve != "__"])))
        pres = calcPressure(flowRates, knownPath, maxLength)
        if pres < pressureCache.get(vis, 0):
            continue

        startPos = knownPath[-1]
        isComplete = True
        for valve in valves:
            if valve not in knownPath:
                newKnownPath = knownPath.copy()

                # only go the path if the target valve has a flow rat
                if flowRates[valve] == 0:
                    continue

                extendPath = cachedPaths[(startPos, valve)]
                newKnownPath.extend(extendPath)
                pressure = calcPressure(flowRates, newKnownPath, maxLength)
                visited = ",".join(sorted(set([valve for valve in newKnownPath if valve != "__"])))

                if pressure > pressureCache.get(visited, 0):
                    pressureCache[visited] = pressure
                    newKnownPaths.append(newKnownPath)

                isComplete = False
        if isComplete and knownPath not in complete:
            complete.append(knownPath.copy())

    return completePaths(valves, paths, newKnownPaths, complete, flowRates, pressureCache,
                         maxLength=maxLength, cachedPaths=cachedPaths)


def calcPressure(flowRates, path, steps, debug=False):
    pressure = 0
    pos = 0
    visitedValves = ["AA"]
    for t in range(steps):
        if debug:
            print()
            print("=== MIN {0} ===".format(t + 1))
        pressurePerMinute = sum([flowRates[valve] for valve in visitedValves if valve != "__"])
        if debug:
            if pressurePerMinute == 0:
                print("No valves are open.")
            else:
                print("Valve {0} is open, releasing {1} pressure.".format(visitedValves, pressurePerMinute))
        pressure += pressurePerMinute

        if pos >= len(path):
            continue
        if path[pos] in visitedValves or path[pos] == "__":
            pos += 1
            if debug:
                print("You're on the move")
        elif path[pos] != "__":
            if debug:
                print("You open valve {0}.".format(path[pos]))
            visitedValves.append(path[pos])

    return pressure


def completePathsB(valves, paths, knownPaths, complete, flowRates, pressureCache, maxLength,
                   cachedPaths):
    newKnownPaths = []

    if len(knownPaths) == 0:
        return complete

    for knownPath in knownPaths:
        if len(knownPath) >= maxLength:
            complete.append(knownPath.copy())
            continue

        op = False
        if knownPath[-1][0] != "__" and knownPath[-1][1] != "__":
            op = True
        vis = ";".join(sorted(set([v[0] for v in knownPath]))) + str(op)
        pres = calcPressureB(flowRates, knownPath, maxLength)
        if pres < pressureCache.get(vis, 0):
            continue

        isComplete = True
        for valve in valves:

            if list(valve) not in knownPath:
                # only go the path if the target valve has a flow rate
                if flowRates[valve[0]] == 0 or flowRates[valve[1]] == 0:
                    continue

                newKnownPathMe = [val[0] for val in knownPath]
                newKnownPathEle = [val[1] for val in knownPath]

                startMe = [val[0] for val in knownPath if val[0] != "__"][-1]
                startEle = [val[1] for val in knownPath if val[1] != "__"][-1]

                indexMe = newKnownPathMe.index(startMe)
                indexEle = newKnownPathEle.index(startEle)

                newKnownPathMe = newKnownPathMe[:indexMe + 1]
                newKnownPathEle = newKnownPathEle[:indexEle + 1]

                extendPathMe = cachedPaths[(startMe, valve[0])]
                extendPathEle = cachedPaths[(startEle, valve[1])]

                newKnownPathMe.extend(extendPathMe)
                newKnownPathEle.extend(extendPathEle)

                visitedBeforeMe = ";".join(newKnownPathMe[:-1])
                visitedBeforeEle = ";".join(newKnownPathEle[:-1])
                if valve[0] in visitedBeforeMe or valve[1] in visitedBeforeEle:
                    continue

                length = max([len(newKnownPathMe), len(newKnownPathEle)])
                newKnownPathMe = newKnownPathMe + ["__"] * (length - len(newKnownPathMe))
                newKnownPathEle = newKnownPathEle + ["__"] * (length - len(newKnownPathEle))
                newKnownPath = list(map(list, zip(newKnownPathMe, newKnownPathEle)))

                onPoint = False
                if newKnownPathMe[-1] != "__" and newKnownPathEle[-1] != "__":
                    onPoint = True

                visitedMe = ";".join(sorted(set(newKnownPathMe))) + str(onPoint)
                pressure = calcPressureB(flowRates, newKnownPath, maxLength)

                if pressure > pressureCache.get(visitedMe, 0):
                    pressureCache[visitedMe] = pressure
                    newKnownPaths.append(newKnownPath)

                isComplete = False

        if isComplete:
            complete.append(knownPath.copy())

    return completePathsB(valves, paths, newKnownPaths, complete, flowRates, pressureCache,
                          maxLength=maxLength, cachedPaths=cachedPaths)


def calcPressureB(flowRates, path, steps):
    pressure = 0
    posMe = 0
    posEle = 0
    visitedValves = ["AA"]

    for t in range(steps):
        pressurePerMinute = sum([flowRates[valve] for valve in visitedValves if valve != "__"])
        pressure += pressurePerMinute

        try:
            if path[posMe][0] in visitedValves or path[posMe][0] == "__":
                posMe += 1

            elif path[posMe][0] != "__":
                visitedValves.append(path[posMe][0])
        except IndexError:
            pass

        try:
            if path[posEle][1] in visitedValves or path[posEle][1] == "__":
                posEle += 1

            elif path[posEle][1] != "__":
                visitedValves.append(path[posEle][1])
        except IndexError:
            pass

    return pressure


def puzzleA(lines):
    paths, flowRates, valves, cachedPaths = parse(lines)
    complete = []
    knownPaths = [["AA"]]
    pressureCache = {}
    completePaths(valves, paths, knownPaths, complete, flowRates, pressureCache, maxLength=30,
                  cachedPaths=cachedPaths)

    return max(pressureCache.values())


def puzzleB(lines):
    paths = {}
    flowRates = {}
    valves = []

    for line in lines:
        flowRate = list(map(int, re.findall('[-+]?[0-9]+', line)))[0]
        valve = line.strip().split("has flow")[0].split()[1].strip()
        flowRates[valve] = flowRate
        valves.append(valve)
        try:
            nextValves = line.strip().split("to valves")[1].strip().split(", ")
        except IndexError:
            nextValves = [line.strip().split("to valve")[1].strip()]

        paths[valve] = nextValves

    valvePairs = []
    for v1 in valves:
        for v2 in valves:
            if v1 != v2:
                valvePairs.append((v1, v2))

    cachedPaths = {}
    for v1 in valves:
        for v2 in valves:
            newPath = dijkstraHeap(paths, startPos=v1, stopPos=v2)
            inBetween = ["__"] * (len(newPath) - 2)
            inBetween.append(newPath[-1])
            cachedPaths[(v1, v2)] = inBetween

    complete = []
    knownPaths = [[["AA", "AA"]]]
    pressureCache = {}

    completePathsB(valvePairs, paths, knownPaths, complete, flowRates, pressureCache,
                   maxLength=26, cachedPaths=cachedPaths)

    return max(pressureCache.values())


if __name__ == '__main__':
    day = "16"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    start = datetime.now()
    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)

    stop = datetime.now()
    print("time: {0}".format(stop - start))
    # assert a == 2265
    # assert b == 2811
