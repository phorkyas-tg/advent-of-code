def getOverlap(lines, onlyHorizontal=True):
    pipes = []

    xMax = 0
    yMax = 0
    # read pipe coordinates
    for line in lines:
        p1, p2 = line.strip().split(" -> ")
        x1, y1 = [int(p) for p in p1.split(",")]
        x2, y2 = [int(p) for p in p2.split(",")]

        # only horizontal or vertical
        if onlyHorizontal and x1 != x2 and y1 != y2:
            continue

        if max(x1, x2) > xMax:
            xMax = max(x1, x2)

        if max(y1, y2) > yMax:
            yMax = max(y1, y2)

        pipes.append([(x1, y1), (x2, y2)])

    # build board
    board = {}
    for x in range(xMax + 1):
        for y in range(yMax + 1):
            board[(x, y)] = 0

    # draw pipes to board
    for pipe in pipes:
        # generate vector between x/yMin and x/yMax
        x = list(range(min(pipe[0][0], pipe[1][0]), max(pipe[0][0], pipe[1][0]) + 1))
        y = list(range(min(pipe[0][1], pipe[1][1]), max(pipe[0][1], pipe[1][1]) + 1))

        # reverse vector if x1 > x2 to get the correct direction
        if pipe[0][0] > pipe[1][0]:
            x.reverse()
        # horizontal case: extend the x vector to match the y vector
        elif pipe[0][0] == pipe[1][0]:
            x = [pipe[0][0]] * len(y)

        if pipe[0][1] > pipe[1][1]:
            y.reverse()
        elif pipe[0][1] == pipe[1][1]:
            y = [pipe[0][1]] * len(x)

        for p in zip(x, y):
            board[p] += 1

    overlap = 0
    # compute overlap
    for p in board.values():
        if p >= 2:
            overlap += 1
    return overlap


def puzzleA(lines):
    return getOverlap(lines, onlyHorizontal=True)


def puzzleB(lines):
    return getOverlap(lines, onlyHorizontal=False)


if __name__ == '__main__':
    day = "05"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 6841
    assert b == 19258
