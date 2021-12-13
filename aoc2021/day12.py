def isVisitedA(nextMove, currentPath):
    return nextMove.islower() and nextMove in currentPath


def isVisitedB(nextMove, currentPath):
    if nextMove.islower():
        lowerCaves = {}
        for cave in currentPath.split("-"):
            if cave.islower():
                lowerCaves.setdefault(cave, 0)
                lowerCaves[cave] += 1

        if max(lowerCaves.values()) > 1 and nextMove in lowerCaves:
            return True
    return False


def getPathsRecursive(board, currentPath, paths, isVisited):
    start = currentPath.split("-")[-1]
    nextMoves = board[start]

    for nextMove in nextMoves:
        if nextMove == "start":
            continue

        newPath = currentPath + "-" + nextMove
        if nextMove == "end":
            paths.setdefault(newPath, len(newPath.split("-")))
            continue

        if isVisited(nextMove, currentPath):
            continue

        getPathsRecursive(board, newPath, paths, isVisited)


def puzzleA(lines):
    board = {}
    for line in lines:
        source, dest = line.strip().split("-")
        board.setdefault(source, [])
        if dest not in board[source]:
            board[source].append(dest)

        board.setdefault(dest, [])
        if source not in board[dest]:
            board[dest].append(source)

    paths = {}
    getPathsRecursive(board, "start", paths, isVisitedA)
    return len(paths.keys())


def puzzleB(lines):
    board = {}
    for line in lines:
        source, dest = line.strip().split("-")
        board.setdefault(source, [])
        if dest not in board[source]:
            board[source].append(dest)

        board.setdefault(dest, [])
        if source not in board[dest]:
            board[dest].append(source)

    paths = {}
    getPathsRecursive(board, "start", paths, isVisitedB)
    return len(paths.keys())


if __name__ == '__main__':
    day = "12"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 3450
    assert b == 96528
