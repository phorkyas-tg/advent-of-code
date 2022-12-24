import os
import re
from datetime import datetime
from functools import cache


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


@cache
def getDim(boardKeys, pos):
    minRowX = min([p[0] for p in boardKeys if p[1] == pos[1]])
    maxRowX = max([p[0] for p in boardKeys if p[1] == pos[1]])
    minRowY = min([p[1] for p in boardKeys if p[0] == pos[0]])
    maxRowY = max([p[1] for p in boardKeys if p[0] == pos[0]])
    return minRowX, maxRowX, minRowY, maxRowY


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

        minRowX, maxRowX, minRowY, maxRowY = getDim(tuple(board.keys()), pos)

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


def specialMove(facing, face, pos, newPos):
    if facing == "R":
        if face == "A":
            # A --> C
            d = pos[1] - 150
            newPos = (50 + d, 149)
            newFacing = "U"
        elif face == "C":
            # C --> F
            d = pos[1] - 100
            newPos = (149, 49 - d)
            newFacing = "L"
        elif face == "D":
            # D --> F
            d = pos[1] - 50
            newPos = (100 + d, 49)
            newFacing = "U"
        elif face == "F":
            # F --> C
            d = pos[1]
            newPos = (99, 149 - d)
            newFacing = "L"
    elif facing == "D":
        if face == "A":
            # A --> F
            d = pos[0]
            newPos = (100 + d, 0)
            newFacing = "D"
        elif face == "C":
            # C --> A
            d = pos[0] - 50
            newPos = (49, 150 + d)
            newFacing = "L"
        elif face == "F":
            # F --> D
            d = pos[0] - 100
            newPos = (99, 50 + d)
            newFacing = "L"
    elif facing == "L":
        if face == "A":
            # A --> E
            d = pos[1] - 150
            newPos = (50 + d, 0)
            newFacing = "D"
        elif face == "B":
            # B --> E
            d = pos[1] - 100
            newPos = (50, 49 - d)
            newFacing = "R"
        elif face == "D":
            # D --> B
            d = pos[1] - 50
            newPos = (d, 100)
            newFacing = "D"
        elif face == "E":
            # E --> B
            d = pos[1]
            newPos = (0, 149 - d)
            newFacing = "R"
    elif facing == "U":
        if face == "B":
            # B --> D
            d = pos[0]
            newPos = (50, 50 + d)
            newFacing = "R"
        elif face == "E":
            # E --> A
            d = pos[0] - 50
            newPos = (0, 150 + d)
            newFacing = "R"
        elif face == "F":
            # F --> A
            d = pos[0] - 100
            newPos = (d, 199)
            newFacing = "U"
    else:
        raise ValueError()

    return newPos, newFacing


def moveCube(board, commands, startPos):
    facing = "R"
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    turns = {"RR": "D", "RL": "U",
             "LR": "U", "LL": "D",
             "UR": "R", "UL": "L",
             "DR": "L", "DL": "R"}

    def getFace(pos):
        """
          E F
          D
        B C
        A
        """
        faceCalc = (pos[0] // 50, pos[1] // 50)
        if faceCalc == (2, 0): return "F"
        if faceCalc == (1, 0): return "E"
        if faceCalc == (1, 1): return "D"
        if faceCalc == (1, 2): return "C"
        if faceCalc == (0, 2): return "B"
        if faceCalc == (0, 3): return "A"
        raise ValueError(pos, faceCalc)

    pos = startPos
    for command in commands:
        if command.isnumeric():
            steps = int(command)
            turn = None
        else:
            steps = int(command[:-1])
            turn = command[-1]

        for __ in range(steps):
            direction = directions[facing]
            newPos = (pos[0] + direction[0], pos[1] + direction[1])
            newFacing = facing
            face = getFace(pos)

            invalidPos = newPos not in board
            if invalidPos:
                newPos, newFacing = specialMove(facing, face, pos, newPos)

            if board[newPos] == "#":
                break

            pos = newPos
            facing = newFacing

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
    assert b == 4578
