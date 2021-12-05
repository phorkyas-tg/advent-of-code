def getWinner(boards, dim=5):
    winnerBoards = []
    for bi in range(len(boards)):

        for c in range(dim):
            isRowX = True
            for r in range(dim):
                if boards[bi][c][r] != "X":
                    isRowX = False
                    break
            if isRowX:
                winnerBoards.append(bi)

        for r in range(dim):
            isColumnX = True
            for c in range(dim):
                if boards[bi][c][r] != "X":
                    isColumnX = False
                    break
            if isColumnX:
                winnerBoards.append(bi)
    return winnerBoards


def markBoards(boards, s, dim=5):
    for board in boards:
        for r in board:
            for c in range(dim):
                if r[c] == s:
                    r[c] = "X"


def buildBoards(lines):
    boards = []
    currentBoard = []
    for i in range(2, len(lines)):
        line = lines[i]

        if line == "\n":
            boards.append(currentBoard.copy())
            currentBoard = []

        row = [int(r) for r in lines[i].strip().split(" ") if r != ""]
        if len(row) > 0:
            currentBoard.append(row)

    # append last board
    boards.append(currentBoard.copy())

    return boards


def score(s, board):
    boardScore = 0
    for r in board:
        for c in r:
            if c != "X":
                boardScore += c
    return boardScore * s


def puzzleA(lines):
    sequence = [int(s) for s in lines[0].strip().split(",")]

    boards = buildBoards(lines)

    for s in sequence:
        markBoards(boards, s)

        winnerBoards = getWinner(boards)
        if len(winnerBoards) > 0:
            return score(s, boards[winnerBoards[0]])


def puzzleB(lines):
    sequence = [int(s) for s in lines[0].strip().split(",")]

    boards = buildBoards(lines)

    for s in sequence:
        markBoards(boards, s)

        winnerBoards = getWinner(boards)
        if len(boards) == 1 and len(winnerBoards) > 0:
            return score(s, boards[winnerBoards[0]])

        winnerBoards.reverse()
        for wb in winnerBoards:
            boards.pop(wb)


if __name__ == '__main__':
    day = "04"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 46920
    assert b == 12635
