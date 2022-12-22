import os
import re
from datetime import datetime


def parseBoard(lines):
    board = dict()
    commands = []
    endOfMap = False

    startPos = None

    for y, line in enumerate(lines):

        if line == "\n":
            endOfMap = True
            continue

        if endOfMap:
            commands = re.findall('[-+]?[0-9]+[A-Z]?', line)
            break

        for x, c in enumerate(line):
            if c in (" ", "\n"):
                continue
            if startPos is None:
                startPos = (x, y)
            board[(x, y)] = c

    return board, commands, startPos


def move(board, commands, startPos):
    facing = "R"
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    turns = {"RR": "D", "RL": "U",
             "LR": "U", "LL": "D",
             "UR": "R", "UL": "L",
             "DR": "L", "DL": "R"}

    pos = startPos
    for command in commands:
        if command.isnumeric():
            steps = int(command)
            turn = None
        else:
            steps = int(command[:-1])
            turn = command[-1]

        minRowX = min([p[0] for p in board.keys() if p[1] == pos[1]])
        maxRowX = max([p[0] for p in board.keys() if p[1] == pos[1]])
        minRowY = min([p[1] for p in board.keys() if p[0] == pos[0]])
        maxRowY = max([p[1] for p in board.keys() if p[0] == pos[0]])

        for s in range(steps):
            direction = directions[facing]
            newPos = (pos[0] + direction[0], pos[1] + direction[1])

            if facing == "R" and newPos[0] > maxRowX:
                newPos = (minRowX, newPos[1])
            elif facing == "L" and newPos[0] < minRowX:
                newPos = (maxRowX, newPos[1])

            elif facing == "D" and newPos[1] > maxRowY:
                newPos = (newPos[0], minRowY)
            elif facing == "U" and newPos[1] < minRowY:
                newPos = (newPos[0], maxRowY)

            if board[newPos] == "#":
                break

            pos = newPos

        if turn is not None:
            facing = turns[facing + turn]

    return pos, facing


def moveCube(board, commands, startPos):
    facing = "R"
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    turns = {"RR": "D", "RL": "U",
             "LR": "U", "LL": "D",
             "UR": "R", "UL": "L",
             "DR": "L", "DL": "R"}

    # face number: xmin/max, ymin/max
    faces = {1: (8, 11, 0, 3),
             2: (0, 3, 4, 7),
             3: (4, 7, 4, 7),
             4: (8, 11, 4, 7),
             5: (8, 11, 8, 11),
             6: (12, 15, 8, 11)}

    faceDirections = {"1U": "2D", "1D": "4D", "1R": "6L", "1L": "3D",
                      "2U": "1D", "2D": "5U", "2R": "3R", "2L": "6U"}

    pos = startPos
    for command in commands:
        if command.isnumeric():
            steps = int(command)
            turn = None
        else:
            steps = int(command[:-1])
            turn = command[-1]

        minRowX = min([p[0] for p in board.keys() if p[1] == pos[1]])
        maxRowX = max([p[0] for p in board.keys() if p[1] == pos[1]])
        minRowY = min([p[1] for p in board.keys() if p[0] == pos[0]])
        maxRowY = max([p[1] for p in board.keys() if p[0] == pos[0]])

        for s in range(steps):
            direction = directions[facing]
            newPos = (pos[0] + direction[0], pos[1] + direction[1])

            if facing == "R" and newPos[0] > maxRowX:
                newPos = (minRowX, newPos[1])
            elif facing == "L" and newPos[0] < minRowX:
                newPos = (maxRowX, newPos[1])

            elif facing == "D" and newPos[1] > maxRowY:
                newPos = (newPos[0], minRowY)
            elif facing == "U" and newPos[1] < minRowY:
                newPos = (newPos[0], maxRowY)

            if board[newPos] == "#":
                break

            pos = newPos

        if turn is not None:
            facing = turns[facing + turn]

    return pos, facing


def puzzleA(lines):
    board, commands, startPos = parseBoard(lines)

    pos, facing = move(board, commands, startPos)
    facingPoints = {"R": 0, "L": 2, "U": 3, "D": 1}
    password = 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + facingPoints[facing]

    return password


def puzzleB(lines):
    board, commands, startPos = parseBoard(lines)

    pos, facing = moveCube(board, commands, startPos)
    facingPoints = {"R": 0, "L": 2, "U": 3, "D": 1}
    password = 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + facingPoints[facing]

    return password


if __name__ == '__main__':
    day = "22"
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
    assert a == 131052
    # assert b == 0
