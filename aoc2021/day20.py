def getBounds(board):
    minX = min([pos[0] for pos in board.keys()])
    maxX = max([pos[0] for pos in board.keys()])

    minY = min([pos[1] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])

    return minX, minY, maxX, maxY


def printBoard(board):
    minX, minY, maxX, maxY = getBounds(board)
    for y in range(minY, maxY + 1):
        line = ""
        for x in range(minX, maxX + 1):
            line += "#" if board.get((x, y), 0) == 1 else "."
        print(line)
    print("")


def getSequence(board, pos):
    sequence = ""
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            sequence += str(board.get((pos[0] + x, pos[1] + y), 0))
    return int(sequence, 2)


def enhance(board, algorithm):
    newBoard = {}

    minX, minY, maxX, maxY = getBounds(board)
    for y in range(minY - 5, maxY + 6):
        for x in range(minX - 5, maxX + 6):
            sequence = getSequence(board, (x, y))
            newPixel = 1 if algorithm[sequence] == "#" else 0
            if newPixel:
                newBoard[(x, y)] = newPixel
    return newBoard


def cutBorder(board, border=8):
    newBoard = {}

    minX, minY, maxX, maxY = getBounds(board)
    for y in range(minY + border, maxY - border + 1):
        for x in range(minX + border, maxX - border + 1):
            if (x, y) in board:
                newBoard[(x, y)] = board[(x, y)]
    return newBoard


def puzzleA(lines):
    algorithm = lines[0]

    board = {}
    for y in range(2, len(lines)):
        for x, char in enumerate(lines[y]):
            if char == "#":
                board[(x, y - 2)] = 1

    board = enhance(board, algorithm)
    board = enhance(board, algorithm)
    if algorithm[0] == "#":
        board = cutBorder(board)

    return len(board.keys())


def puzzleB(lines):
    algorithm = lines[0]

    board = {}
    for y in range(2, len(lines)):
        for x, char in enumerate(lines[y]):
            if char == "#":
                board[(x, y - 2)] = 1

    for i in range(25):
        board = enhance(board, algorithm)
        board = enhance(board, algorithm)
        if algorithm[0] == "#":
            board = cutBorder(board)
    return len(board.keys())


if __name__ == '__main__':
    day = "20"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 5361
    assert b == 16826
