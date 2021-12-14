def foldBoard(board, axis, num):
    toDelete = []
    toAdd = []
    for pos in board.keys():
        if (axis == "x" and pos[0] == num) or (axis == "y" and pos[1] == num):
            toDelete.append(pos)

    for pos in board.keys():
        if axis == "y" and pos[1] > num:
            newY = num - (pos[1] - num)
            toAdd.append((pos[0], newY))
            toDelete.append(pos)
        if axis == "x" and pos[0] > num:
            newX = num - (pos[0] - num)
            toAdd.append((newX, pos[1]))
            toDelete.append(pos)

    for pos in toAdd:
        board.setdefault(pos, "#")

    for pos in toDelete:
        board.pop(pos)


def buildBoard(lines):
    instructionStart = False
    board = {}
    instr = []

    for line in lines:
        if line == "\n":
            instructionStart = True
            continue

        if not instructionStart:
            x, y = map(int, line.strip().split(","))
            board.setdefault((x, y), "#")
        else:
            axis, num = line.strip().replace("fold along ", "").split("=")
            instr.append((axis, int(num)))
    return board, instr


def puzzleA(lines):
    board, instr = buildBoard(lines)

    for axis, num in instr:
        foldBoard(board, axis, num)
        return len(board.keys())


def puzzleB(lines):
    board, instr = buildBoard(lines)

    for axis, num in instr:
        foldBoard(board, axis, num)

    maxX = max([pos[0] for pos in board.keys()])
    maxY = max([pos[1] for pos in board.keys()])

    result = "\n"
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            result += board.get((x, y), ".")
        result += "\n"

    return result


if __name__ == '__main__':
    day = "13"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 942
    assert b == '\n' \
                '..##.####..##..#..#..##..###..###..###.\n' \
                '...#....#.#..#.#..#.#..#.#..#.#..#.#..#\n' \
                '...#...#..#....#..#.#..#.#..#.#..#.###.\n' \
                '...#..#...#.##.#..#.####.###..###..#..#\n' \
                '#..#.#....#..#.#..#.#..#.#....#.#..#..#\n' \
                '.##..####..###..##..#..#.#....#..#.###.\n'

