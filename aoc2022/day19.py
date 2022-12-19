import os
import re
from datetime import datetime
from functools import cache


@cache
def canBuild(bluePrint, recources, robots, timeLeft):
    canGeo = recources[0] >= bluePrint[3][0] and recources[2] >= bluePrint[3][2]
    # if we can build a geode robot we should do it
    if canGeo:
        return False, False, False, True

    canOre = recources[0] >= bluePrint[0][0]
    # If we have more ore than needed to build every other robot than don't build another ore robot
    maxOre = max(cost[0] for cost in bluePrint)
    if maxOre + (maxOre - robots[0]) * timeLeft <= robots[0]:
        canOre = False

    canCla = recources[0] >= bluePrint[1][0]
    # clay is only needed to build obsidian robots
    # if we have more clay than needed to build obsidian robots stop building clay robots
    maxClay = bluePrint[2][1]
    if maxClay + (maxClay - robots[1]) * timeLeft <= robots[1]:
        canCla = False

    canObs = (recources[0] >= bluePrint[2][0] and recources[1] >= bluePrint[2][1])
    # obsidian is only needed to buils geode robots
    # if we have more obsidian needed to build geode robots stop building obsidian robots
    maxObs = bluePrint[3][2]
    if maxObs + (maxObs - robots[2]) * timeLeft <= robots[2]:
        canObs = False

    return canOre, canCla, canObs, canGeo


@cache
def payRecource(bluePrint, recource, robotIndex):
    return tuple([value - bluePrint[robotIndex][i] for i, value in enumerate(recource)])


def getMostGeodes(bluePrint, robotsAndRecources, resourceCache, time=0, maxTime=24):
    newRobotsAndRecources = []

    # how many geodes you can produce till the end?
    maxGeodesCrackedTillEnd = 1
    for i in range(1, maxTime - time):
        maxGeodesCrackedTillEnd *= i
    currentMaxGeodes = max([rar[1][-1] for rar in robotsAndRecources])

    for robots, recources in robotsAndRecources:
        numberOfGeodes = recources[-1]
        if numberOfGeodes + maxGeodesCrackedTillEnd <= currentMaxGeodes:
            continue

        canBuildRobot = canBuild(bluePrint, recources, robots, maxTime - time - 1)
        newRecources = tuple([recources[i] + robot for i, robot in enumerate(robots)])

        for i, canBld in enumerate(canBuildRobot):
            if canBld:
                newRobots = tuple([robot if i != j else robot + 1
                                   for j, robot in enumerate(robots)])
                payedRecource = payRecource(bluePrint, newRecources, i)
                if not (newRobots, payedRecource) in resourceCache:
                    newRobotsAndRecources.append([newRobots, payedRecource])
                    resourceCache[(newRobots, payedRecource)] = time

        # or don't build anything
        if not (robots, newRecources) in resourceCache:
            newRobotsAndRecources.append([robots, newRecources])
            resourceCache[(robots, newRecources)] = time

    time += 1
    if time >= maxTime:
        return newRobotsAndRecources

    return getMostGeodes(bluePrint, newRobotsAndRecources, resourceCache, time, maxTime)


def parseBluePrints(lines):
    bluePrints = {}
    for line in lines:
        numbers = list(map(int, re.findall('[-+]?[0-9]+', line)))
        # ore, clay, obsidian, geodes
        oreRobot = (numbers[1], 0, 0, 0)
        clayRobot = (numbers[2], 0, 0, 0)
        obsidianRobot = (numbers[3], numbers[4], 0, 0)
        geodeRobot = (numbers[5], 0, numbers[6], 0)

        bluePrints[numbers[0]] = (oreRobot, clayRobot, obsidianRobot, geodeRobot)
    return bluePrints


def puzzleA(lines):
    bluePrints = parseBluePrints(lines)

    print()
    print("=== PUZZLE A ===")

    result = 0
    for bluePrintNumber, bluePrint in bluePrints.items():
        s = datetime.now()
        resourceCache = {}
        getMostGeodes(bluePrint, [[(1, 0, 0, 0), (0, 0, 0, 0)]], resourceCache)
        qualityLevel = max([rar[1][-1] for rar in resourceCache.keys()])
        result += qualityLevel * bluePrintNumber
        e = datetime.now()
        print("BluePrint [{0}]: {1} ({2} s)".format(bluePrintNumber, qualityLevel, e - s))
    print("")
    print("Result: {0}".format(result))

    return result


def puzzleB(lines):
    bluePrints = parseBluePrints(lines)

    print()
    print("=== PUZZLE B ===")

    result = 1
    for bluePrintNumber, bluePrint in bluePrints.items():
        if bluePrintNumber > 3:
            continue
        s = datetime.now()
        resourceCache = {}
        getMostGeodes(bluePrint, [[(1, 0, 0, 0), (0, 0, 0, 0)]], resourceCache, time=0, maxTime=32)
        qualityLevel = max([rar[1][-1] for rar in resourceCache.keys()])
        result *= qualityLevel
        e = datetime.now()
        print("BluePrint [{0}]: {1} ({2} s)".format(bluePrintNumber, qualityLevel, e - s))
    print("")
    print("Result: {0}".format(result))

    return result


if __name__ == '__main__':
    day = "19"
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
    assert a == 1981
    assert b == 10962
