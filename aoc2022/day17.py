import os
from datetime import datetime


def printBoard(board, shape):
    lines = ["+-------+"]
    yMaxBoard = 0 if not board else max([pos[1] for pos in board.keys()]) + 1
    yMaxShape = 0 if not shape else max([pos[1] for pos in shape.keys()]) + 1
    yMax = max([yMaxShape, yMaxBoard, 1])

    for y in range(yMax):
        line = "|"
        for x in range(0, 7):
            pos = (x, y)
            if pos in board:
                line += board.get(pos)
            else:
                line += shape.get(pos, ".")
        line += "|"
        lines.append(line)

    lines = lines[::-1]
    print()
    for line in lines:
        print(line)


def initShape(shapeIndex, board):
    y = 0 if not board else max([pos[1] + 1 for pos in board.keys()])
    shape = dict()
    if shapeIndex == 0:
        for x in range(4):
            shape[(x + 2, y + 3)] = "@"
    elif shapeIndex == 1:
        shape[(3, y + 3)] = "@"
        shape[(2, y + 4)] = "@"
        shape[(3, y + 4)] = "@"
        shape[(4, y + 4)] = "@"
        shape[(3, y + 5)] = "@"
    elif shapeIndex == 2:
        shape[(2, y + 3)] = "@"
        shape[(3, y + 3)] = "@"
        shape[(4, y + 3)] = "@"
        shape[(4, y + 4)] = "@"
        shape[(4, y + 5)] = "@"
    elif shapeIndex == 3:
        shape[(2, y + 3)] = "@"
        shape[(2, y + 4)] = "@"
        shape[(2, y + 5)] = "@"
        shape[(2, y + 6)] = "@"
    elif shapeIndex == 4:
        shape[(2, y + 3)] = "@"
        shape[(2, y + 4)] = "@"
        shape[(3, y + 3)] = "@"
        shape[(3, y + 4)] = "@"
    else:
        raise NotImplementedError()

    return shape


def moveShape(command, shape, board):
    rested = False

    # first push the shape
    x = 1 if command == ">" else -1
    canPush = True
    newShape = dict()
    for shapePos in shape.keys():
        pushPos = (shapePos[0] + x, shapePos[1])
        newShape[pushPos] = "@"
        if pushPos in board or pushPos[0] < 0 or pushPos[0] > 6:
            canPush = False
            break
    if canPush:
        shape = newShape

    # then let it fall
    y = -1
    canFall = True
    newShape = dict()
    for shapePos in shape.keys():
        fallPos = (shapePos[0], shapePos[1] + y)
        newShape[fallPos] = "@"
        if fallPos in board or fallPos[1] < 0:
            canFall = False
            break
    if canFall:
        shape = newShape
    else:
        rested = True
        for shapePos in shape.keys():
            board[shapePos] = "#"

    return rested, shape


def getHash(board, shapeIndex, commandIndex):
    y = max([pos[1] for pos in board.keys()])
    hashValue = (shapeIndex, commandIndex)
    return hashValue, y


def puzzleA(lines):
    commands = lines[0].strip()
    shapeIndex = 0
    board = dict()

    rested = True
    shape = {}
    pieceCount = 0

    while pieceCount < 2022:
        for command in commands:
            if rested:
                shape = initShape(shapeIndex, board)

            rested, shape = moveShape(command, shape, board)
            if rested:
                shapeIndex = (shapeIndex + 1) % 5
                pieceCount += 1
                if pieceCount >= 2022:
                    break

    return max([pos[1] for pos in board.keys()]) + 1


def puzzleB(lines):
    commands = lines[0].strip()
    shapeIndex = 0
    board = dict()

    rested = True
    shape = {}
    pieceCount = 0
    cache = {}

    extraHeight = 0
    extraPieces = 0
    commandRollOver = False
    pieceTarget = 1000000000000

    while pieceCount + extraPieces < pieceTarget:
        for commandIndex, command in enumerate(commands):
            if pieceCount + extraPieces >= pieceTarget:
                break

            if rested:
                shape = initShape(shapeIndex, board)

            rested, shape = moveShape(command, shape, board)
            if rested:
                shapeIndex = (shapeIndex + 1) % 5
                pieceCount += 1

                if not commandRollOver:
                    continue

                hashValue, height = getHash(board, shapeIndex, commandIndex)

                if hashValue in cache:
                    lastHeight, lastPieceCount = cache[hashValue]

                    deltaHeight = height - lastHeight
                    deltaPieceCount = pieceCount - lastPieceCount

                    repeat = (pieceTarget - (pieceCount + extraPieces)) // pieceCount
                    extraPieces += repeat * deltaPieceCount
                    extraHeight += repeat * deltaHeight

                cache[hashValue] = (height, pieceCount)
        commandRollOver = True

    height = max([pos[1] for pos in board.keys()]) + 1
    return height + extraHeight


if __name__ == '__main__':
    day = "17"
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
    assert a == 3141
    assert b == 1561739130391
