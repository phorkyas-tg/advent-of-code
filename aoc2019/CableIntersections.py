import re
import operator


def UpdateCoordinates(coordinates, lastCoordinate, operation, pos):
    newCoordinate = lastCoordinate.copy()
    newCoordinate[pos] = operation(newCoordinate[pos], 1)

    if newCoordinate[0] not in coordinates:
        coordinates[newCoordinate[0]] = [newCoordinate[1]]
    else:
        coordinates[newCoordinate[0]].append(newCoordinate[1])
    return newCoordinate.copy()


def GetCoordinates(input):
    coordinates = {}
    coordinateList = []

    lastCoordinate = [0, 0]
    for sequence in input:
        command = re.findall(r'[UDLR]', sequence)[0]
        number = int(re.findall(r'\d+', sequence)[0])

        if command == "U":
            for i in range(number):
                lastCoordinate = UpdateCoordinates(coordinates, lastCoordinate, operator.add, 1)
                coordinateList.append(lastCoordinate.copy())

        elif command == "D":
            for i in range(number):
                lastCoordinate = UpdateCoordinates(coordinates, lastCoordinate, operator.sub, 1)
                coordinateList.append(lastCoordinate.copy())

        elif command == "R":
            for i in range(number):
                lastCoordinate = UpdateCoordinates(coordinates, lastCoordinate, operator.add, 0)
                coordinateList.append(lastCoordinate.copy())

        elif command == "L":
            for i in range(number):
                lastCoordinate = UpdateCoordinates(coordinates, lastCoordinate, operator.sub, 0)
                coordinateList.append(lastCoordinate.copy())

    return coordinates, coordinateList


def GetIntersectionPoints(c1, c2):
    intersection = []
    for key, valList in c1.items():
        if key in c2:
            for val in c2[key]:
                if val in valList:
                    intersection.append([key, val])

    return intersection


def GetLowestManhattanDistance(intersections):
    dist = None
    for intersection in intersections:
        tempDist = abs(intersection[0]) + abs(intersection[1])
        if dist is None or tempDist < dist:
            dist = tempDist
    return dist


def GetLowestDistanceFromStart(c1, c2, intersections):
    dist = None
    for intersection in intersections:
        dist1 = 0
        for i in range(len(c1)):
            if intersection == c1[i]:
                dist1 = i + 1

        dist2 = 0
        for i in range(len(c2)):
            if intersection == c2[i]:
                dist2 = i + 1

        if dist is None or (dist1 + dist2) < dist:
            dist = dist1 + dist2
    return dist


def ReadIntersections(input1, input2):
    commands1, commandList1 = GetCoordinates(input1.copy())
    commands2, commandList2 = GetCoordinates(input2.copy())
    intersection = GetIntersectionPoints(commands1, commands2)

    return commandList1, commandList2, intersection

