import os
from collections import deque
from datetime import datetime


def move(board, directions):
    proposals = dict()
    lookAhead = {"N": [(-1, -1), (0, -1), (1, -1)],
                 "S": [(-1, 1), (0, 1), (1, 1)],
                 "W": [(-1, -1), (-1, 0), (-1, 1)],
                 "E": [(1, -1), (1, 0), (1, 1)]}

    goto = {"N": (0, -1),
            "S": (0, 1),
            "W": (-1, 0),
            "E": (1, 0)}

    for pos in board.keys():
        isSomethingAround = False
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue
                if (pos[0] + x, pos[1] + y) in board:
                    isSomethingAround = True

        if not isSomethingAround:
            proposals.setdefault(pos, [])
            proposals[pos].append(pos)
            continue

        for d in directions:
            for look in lookAhead[d]:
                if (pos[0] + look[0], pos[1] + look[1]) in board:
                    break
            else:
                newPos = (pos[0] + goto[d][0], pos[1] + goto[d][1])
                proposals.setdefault(newPos, [])
                proposals[newPos].append(pos)
                break
        else:
            proposals.setdefault(pos, [])
            proposals[pos].append(pos)

    newBoard = dict()
    moved = False
    for newPos, oldPositions in proposals.items():
        if len(oldPositions) == 1:
            newBoard[newPos] = "#"
            if newPos != oldPositions[0]:
                moved = True
            continue

        for pos in oldPositions:
            newBoard[pos] = "#"

    return newBoard, moved


def printBoard(board):
    minX = min([pos[0] for pos in board.keys()])
    maxX = max([pos[0] for pos in board.keys()])
    minY = min([pos[1] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])

    print()
    for y in range(minY, maxY + 1):
        line = ""
        for x in range(minX, maxX + 1):
            line += board.get((x, y), ".")
        print(line)


def countEmptyTiles(board):
    minX = min([pos[0] for pos in board.keys()])
    maxX = max([pos[0] for pos in board.keys()])
    minY = min([pos[1] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])

    counter = 0
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            counter += 1 if (x, y) not in board else 0
    return counter

def puzzleA(lines):
    board = dict()

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == "#":
                board[(x, y)] = c


    directions = deque(["N", "S", "W", "E"])
    for __ in range(10):
        board, __ = move(board, directions)
        directions.rotate(-1)

    return countEmptyTiles(board)


def puzzleB(lines):
    board = dict()

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == "#":
                board[(x, y)] = c


    directions = deque(["N", "S", "W", "E"])
    moved = True
    i = 0

    while moved:
        board, moved = move(board, directions)
        directions.rotate(-1)
        i += 1

    return i


if __name__ == '__main__':
    day = "23"
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
    assert a == 4336
    assert b == 1005
