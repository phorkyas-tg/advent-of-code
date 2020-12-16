from collections import deque


def GetShipManhattanDistance(puzzleInput):

    directions = deque(["N", "E", "S", "W"])

    currentPos = [0, 0]
    currentDirection = "E"

    for i in puzzleInput:
        command = i[0]
        number = int(i[1:])

        if command == "F":
            command = currentDirection

        if command == "N":
            currentPos[0] -= number
        elif command == "W":
            currentPos[1] -= number
        elif command == "S":
            currentPos[0] += number
        elif command == "E":
            currentPos[1] += number
        elif command in ("R", "L"):
            rotate = 1
            if command == "R":
                rotate = -1

            while directions[0] != currentDirection:
                directions.rotate(rotate)
            number = int(number/90)
            directions.rotate(rotate * number)
            currentDirection = directions[0]

    return abs(currentPos[0]) + abs(currentPos[1])


def GetShipWithWaypointManhattanDistance(puzzleInput):
    currentPos = [0, 0]
    waypoint = [-1, 10]

    for i in puzzleInput:
        command = i[0]
        number = int(i[1:])

        if command == "F":
            currentPos[0] += number * waypoint[0]
            currentPos[1] += number * waypoint[1]
        elif command == "N":
            waypoint[0] -= number
        elif command == "W":
            waypoint[1] -= number
        elif command == "S":
            waypoint[0] += number
        elif command == "E":
            waypoint[1] += number
        elif command in ("R", "L"):
            rotate = -1
            if command == "R":
                rotate = 1

            directions = deque([[waypoint[0], waypoint[1]],
                                [-waypoint[1], waypoint[0]],
                                [-waypoint[0], -waypoint[1]],
                                [waypoint[1], -waypoint[0]]])

            number = int(number/90)
            directions.rotate(rotate * number)
            waypoint = directions[0]

    return abs(currentPos[0]) + abs(currentPos[1])
