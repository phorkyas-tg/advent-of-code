def getBoard(lines):
    board = {}

    for y, line in enumerate(lines):
        for x, num in enumerate(line.strip()):
            board[(x, y)] = num
    return board


def getLowPoints(board):
    lowPoints = {}
    for pos, num in board.items():
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            adjacentPos = (pos[0] + d[0], pos[1] + d[1])
            adjacentNum = board.get(adjacentPos, None)
            if adjacentNum is not None:
                if num >= adjacentNum:
                    break
        else:
            lowPoints[pos] = num
    return lowPoints


def puzzleA(lines):
    board = getBoard(lines)
    lowPoints = getLowPoints(board)

    return sum([int(i) + 1 for i in lowPoints.values()])


def puzzleB(lines):
    board = getBoard(lines)
    lowPoints = getLowPoints(board)

    basins = []
    for pos in lowPoints.keys():
        basinPos = [pos]
        newPosFound = True

        while newPosFound:
            newPosFound = False
            newPos = []

            for bPos in basinPos:
                bNum = int(board.get(bPos, None))

                for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    adjacentPos = (bPos[0] + d[0], bPos[1] + d[1])
                    adjacentNum = board.get(adjacentPos, None)

                    if adjacentNum is None or adjacentPos in basinPos or adjacentPos in newPos:
                        continue

                    adjacentNum = int(adjacentNum)
                    if bNum < adjacentNum != 9:
                        newPosFound = True
                        newPos.append(adjacentPos)

            basinPos.extend(newPos)

        basins.append(len(basinPos))

    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


if __name__ == '__main__':
    day = "09"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 572
    assert b == 847044
