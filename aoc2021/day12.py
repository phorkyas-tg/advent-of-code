def isVisitedA(nextCave, lowerCaves):
    return nextCave in lowerCaves and lowerCaves[nextCave] > 1


def isVisitedB(nextCave, lowerCaves):
    return sum(lowerCaves.values()) > len(lowerCaves.keys()) + 1


def getPathsRecursive(board, currentPath, lowerCaves, paths, isVisited):
    nextCaves = board[currentPath[-1]]

    for nextCave in nextCaves:
        if nextCave == "start":
            continue

        newLowerCaves = lowerCaves.copy()
        if nextCave.islower():
            newLowerCaves.setdefault(nextCave, 0)
            newLowerCaves[nextCave] += 1

        if isVisited(nextCave, newLowerCaves):
            continue

        newPath = currentPath.copy()
        newPath.append(nextCave)

        if nextCave == "end":
            paths.setdefault("-".join(newPath), newPath)
            continue

        getPathsRecursive(board, newPath, newLowerCaves, paths, isVisited)


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
    getPathsRecursive(board, ["start"], {"start": 1}, paths, isVisitedA)
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
    getPathsRecursive(board, ["start"], {"start": 1}, paths, isVisitedB)
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
