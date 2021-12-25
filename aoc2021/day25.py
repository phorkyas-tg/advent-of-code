def puzzleA(lines):
    board = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != ".":
                board[(x, y)] = char

    maxX = max([pos[0] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])

    i = 0
    while True:
        newBoard = {}

        # for y in range(maxY + 1):
        #     pLine = ""
        #     for x in range(maxX + 1):
        #         pLine += board.get((x, y), ".")
        #     print(pLine)
        # print()

        hasMoved = False

        # first east
        for pos, char in board.items():
            if char == ">":
                # check if free
                newPos = (pos[0] + 1, pos[1]) if pos[0] < maxX else (0, pos[1])
                if newPos in board:
                    newBoard[pos] = char
                else:
                    newBoard[newPos] = char
                    hasMoved = True
            else:
                newBoard[pos] = char

        board = newBoard
        newBoard = {}

        # then south
        for pos, char in board.items():
            if char == "v":
                # check if free
                newPos = (pos[0], pos[1] + 1) if pos[1] < maxY else (pos[0], 0)
                if newPos in board:
                    newBoard[pos] = char
                else:
                    newBoard[newPos] = char
                    hasMoved = True
            else:
                newBoard[pos] = char

        board = newBoard
        i += 1

        if not hasMoved:
            break

    return i


def puzzleB(lines):
    return 0


if __name__ == '__main__':
    day = "25"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 560
    assert b == 0
