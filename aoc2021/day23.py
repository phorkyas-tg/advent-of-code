ROOM = {"A": 2, "B": 4, "C": 6, "D": 8, 2: "A", 4: "B", 6: "C", 8: "D"}


def getPossibleMoves(board, pos):
    impossiblePositions = [(2, 0), (4, 0), (6, 0), (8, 0)]
    energy = {"A": 1, "B": 10, "C": 100, "D": 1000}

    possibleMoves = []

    char = board.get(pos, None)
    if char is None:
        char = board[ROOM.get(pos[0])][pos[1] - 1]

    for sign in [-1, 1]:
        for i in range(11):
            currentPos = (pos[0] + (sign * i), 0)

            if pos == currentPos:
                continue

            currentChar = board.get(currentPos, None)
            if currentChar != "." or currentChar is None:
                break

            # can it get into the room
            if currentPos[0] == ROOM.get(char) and \
                    board[char].count(char) + board[char].count(".") == len(board[char]) and \
                    board[char].count(".") > 0:

                freeSpot = (currentPos[0], board[char].count("."))
                e = (pos[1] + i + board[char].count(".")) * energy.get(char)
                possibleMoves.append((freeSpot, e))

            if currentPos in impossiblePositions:
                continue

            if pos[1] != 0:
                possibleMoves.append((currentPos, (pos[1] + i) * energy.get(char)))

    return possibleMoves


def getPossibleFigures(board):
    possibleFigures = []
    for pos, char in board.items():

        if pos in ["A", "B", "C", "D"]:
            for i, c in enumerate(char):
                if c != ".":
                    # end position - this is not needed
                    if c == pos and char[i+1:].count(pos) == len(char[i+1:]):
                        break
                    possibleFigures.append((ROOM.get(pos), i + 1))
                    break
            continue

        if char == ".":
            continue

        if pos[1] in [0, 1]:
            possibleFigures.append(pos)
            continue

    return possibleFigures


def isFinished(board):
    return board["A"].count("A") == len(board["A"]) and \
           board["B"].count("B") == len(board["B"]) and \
           board["C"].count("C") == len(board["C"]) and \
           board["D"].count("D") == len(board["D"])


def moveRecursive(board, energy=0, bestEnergy={}, knownBoards={}):
    figs = getPossibleFigures(board)

    for pos in figs:
        for newPos, energyNeeded in getPossibleMoves(board, pos):
            newBoard = board.copy()

            if newPos[1] == 0:
                char = ROOM.get(pos[0])
                newBoard[newPos] = newBoard[char][pos[1] - 1]
                newBoard[char] = newBoard[char][:pos[1] - 1] + "." + newBoard[char][pos[1]:]
            elif pos[1] == 0:
                char = ROOM.get(newPos[0])
                newBoard[pos] = "."
                newBoard[char] = newBoard[char][:newPos[1] - 1] + char + newBoard[char][newPos[1]:]
            else:
                char = ROOM.get(newPos[0])
                newBoard[char] = newBoard[char][:newPos[1] - 1] + char + newBoard[char][newPos[1]:]
                char = ROOM.get(pos[0])
                newBoard[char] = newBoard[char][:pos[1] - 1] + "." + newBoard[char][pos[1]:]

            energyNeeded += energy

            be = bestEnergy.get("e", None)
            if be is not None and be <= energyNeeded:
                continue

            if isFinished(newBoard):
                bestEnergy["e"] = energyNeeded
                continue

            boardString = "-".join(newBoard.values()) + ":" + str(energyNeeded)
            if boardString in knownBoards:
                continue
            knownBoards[boardString] = "#"

            moveRecursive(newBoard, energyNeeded, bestEnergy, knownBoards)


def puzzleA(lines):
    board = {}
    for x, char in enumerate(lines[1][1:-2]):
        board[(x, 0)] = char

    board["A"] = ""
    board["B"] = ""
    board["C"] = ""
    board["D"] = ""
    for line in [lines[2], lines[3]]:
        for x, char in enumerate(line.strip().strip("#").split("#")):
            if x == 0:
                board["A"] += char
            elif x == 1:
                board["B"] += char
            elif x == 2:
                board["C"] += char
            elif x == 3:
                board["D"] += char

    bestEnergy = {"e": None}
    knownBoards = {}
    moveRecursive(board, energy=0, bestEnergy=bestEnergy, knownBoards=knownBoards)

    return bestEnergy.get("e", 0)


def puzzleB(lines):
    board = {}
    for x, char in enumerate(lines[1][1:-2]):
        board[(x, 0)] = char

    board["A"] = ""
    board["B"] = ""
    board["C"] = ""
    board["D"] = ""
    for line in [lines[2], "#D#C#B#A#", "#D#B#A#C#", lines[3]]:
        for x, char in enumerate(line.strip().strip("#").split("#")):
            if x == 0:
                board["A"] += char
            elif x == 1:
                board["B"] += char
            elif x == 2:
                board["C"] += char
            elif x == 3:
                board["D"] += char

    bestEnergy = {"e": None}
    knownBoards = {}
    moveRecursive(board, energy=0, bestEnergy=bestEnergy, knownBoards=knownBoards)

    return bestEnergy.get("e", 0)


if __name__ == '__main__':
    day = "23"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 13495
    assert b == 53767
