def getAdjacent(pos, board):
    positions = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            if (pos[0] + x, pos[1] + y) in board:
                positions.append((pos[0] + x, pos[1] + y))

    return positions


def updateBoard(board):
    for pos in board.keys():
        board[pos] += 1

    newFlash = True
    flashedPositions = []
    while newFlash:
        newFlash = False

        for pos in board.keys():
            if board[pos] >= 10 and pos not in flashedPositions:
                newFlash = True
                flashedPositions.append(pos)

                adjacent = getAdjacent(pos, board)
                for aPos in adjacent:
                    board[aPos] += 1
    return board


def puzzleA(lines):
    board = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            board[(x, y)] = int(char)

    flashing = 0
    for i in range(100):
        board = updateBoard(board)

        for pos in board.keys():
            if board[pos] >= 10:
                board[pos] = 0
                flashing += 1

    return flashing


def puzzleB(lines):
    board = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            board[(x, y)] = int(char)

    i = 0
    while True:
        board = updateBoard(board)

        flashAll = True
        for pos in board.keys():
            if board[pos] >= 10:
                board[pos] = 0
            else:
                flashAll = False

        i += 1

        if flashAll:
            return i


if __name__ == '__main__':
    day = "11"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 1694
    assert b == 346
