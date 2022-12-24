import heapq
import os
from datetime import datetime


def printBoard(board):
    minX = min([pos[0] for pos in board.keys()])
    maxX = max([pos[0] for pos in board.keys()])
    minY = min([pos[1] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])

    print()
    for y in range(minY, maxY + 1):
        line = ""
        for x in range(minX, maxX + 1):
            c =  board.get((x, y), ["."])
            line += c[0] if len(c) == 1 else str(len(c))
        print(line)

def hashBoard(board):
    minX = min([pos[0] for pos in board.keys()])
    maxX = max([pos[0] for pos in board.keys()])
    minY = min([pos[1] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])

    line = ""
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            c =  board.get((x, y), ["."])
            line += c[0] if len(c) == 1 else str(len(c))
    
    return hash(line)

def stepHurricanes(board):
    newBoard = dict()

    maxX = max([pos[0] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])

    for pos, items in board.items(): 
        for item in items:
            if item == "#":
                newPos = pos
            elif item == ">":
                if pos[0] + 1 == maxX:
                    newPos = (1, pos[1])
                else:
                    newPos = (pos[0] + 1, pos[1])
            elif item == "<":
                if pos[0] - 1 == 0:
                    newPos = (maxX - 1, pos[1])
                else:
                    newPos = (pos[0] - 1, pos[1])
            elif item == "v":
                if pos[1] + 1 == maxY:
                    newPos = (pos[0], 1)
                else:
                    newPos = (pos[0], pos[1] + 1)
            elif item == "^":
                if pos[1] - 1 == 0:
                    newPos = (pos[0], maxY - 1)
                else:
                    newPos = (pos[0], pos[1] - 1)
            else:
                raise NotImplementedError()
            
            newBoard.setdefault(newPos, [])
            newBoard[newPos].append(item)
    return newBoard


def getAdjacent(pos, board, maxY):
    adjacent = []

    for p in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        newPos = (pos[0] + p[0], pos[1] + p[1])

        if newPos not in board and newPos[1] >= 0 and newPos[1] <= maxY:
            adjacent.append(newPos)

    return adjacent


def dijkstraHeap(initialBoard, startPos, stopPos, stopState=1):
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, startPos, 0))

    hurricanStates = {0: initialBoard}

    cache = {}

    maxY = max([pos[1] for pos in initialBoard.keys()])

    while len(queue) > 0:
        currentTime, pos, state = heapq.heappop(queue)
        if pos == stopPos and state == stopState:
            return currentTime

        if currentTime + 1 not in hurricanStates:
            hurricanStates[currentTime + 1] = stepHurricanes(hurricanStates[currentTime])
        
        for adjacentPos in getAdjacent(pos, hurricanStates[currentTime + 1], maxY):
            priority = currentTime + 1

            newState = state
            if newState in (0, 2) and adjacentPos == stopPos:
                newState += 1
            elif newState == 1 and adjacentPos == startPos:
                newState += 1

            if (priority, adjacentPos, newState) in cache:
                continue
            cache[(priority, adjacentPos, newState)] = "#"
            
            heapq.heappush(queue, (priority, adjacentPos, newState))

    
    return None


def puzzleA(lines):
    board = dict()

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == ".":
                continue
            board[(x, y)] = [c]


    maxX = max([pos[0] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])
    t = dijkstraHeap(board, (1, 0), (maxX - 1, maxY))

    return t


def puzzleB(lines):
    board = dict()

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == ".":
                continue
            board[(x, y)] = [c]


    maxX = max([pos[0] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])
    t = dijkstraHeap(board, (1, 0), (maxX - 1, maxY), stopState=3)

    return t


if __name__ == '__main__':
    day = "24"
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
    assert a == 281
    assert b == 807
