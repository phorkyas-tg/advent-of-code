def calcFuelA(crabPos, pos):
    return abs(crabPos - pos)


def calcFuelB(crabPos, pos):
    steps = abs(crabPos - pos)
    # small gauss
    return int((steps * (steps + 1)) / 2)


def calcMinimalFuel(lines, calcFuel):
    positions = [int(i) for i in lines[0].strip().split(",")]
    minPos = min(positions)
    maxPos = max(positions)

    posToFuel = {}

    for pos in range(minPos, maxPos + 1):
        posToFuel.setdefault(pos, 0)
        for crabPos in positions:
            posToFuel[pos] += calcFuel(crabPos, pos)

    return min(posToFuel.values())


def puzzleA(lines):
    return calcMinimalFuel(lines, calcFuelA)


def puzzleB(lines):
    return calcMinimalFuel(lines, calcFuelB)


if __name__ == '__main__':
    day = "07"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 344735
    assert b == 96798233
