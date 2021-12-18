def shoot(vx, vy, x, y):
    xPos = 0
    yPos = 0

    maxY = 0
    while True:
        xPos += vx
        yPos += vy

        if yPos > maxY:
            maxY = yPos

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy = vy - 1

        if yPos < min(y):
            return False, maxY, (xPos, yPos)

        if min(x) <= xPos <= max(x) and min(y) <= yPos <= max(y):
            return True, maxY, (xPos, yPos)


def puzzleA(lines):
    line = lines[0].strip().replace("target area: ", "")
    x, y = line.split(", ")

    x = list(map(int, x.replace("x=", "").split("..")))
    y = list(map(int, y.replace("y=", "").split("..")))

    vy = 1
    maxY = 0
    while vy < 130:
        vx = 1
        while True:
            isHit, _maxY, pos = shoot(vx, vy, x, y)
            if isHit:
                if _maxY > maxY:
                    maxY = _maxY
                break
            elif pos[0] >= max(x):
                break
            vx += 1
        vy += 1

    return maxY


def puzzleB(lines):
    line = lines[0].strip().replace("target area: ", "")
    x, y = line.split(", ")

    x = list(map(int, x.replace("x=", "").split("..")))
    y = list(map(int, y.replace("y=", "").split("..")))

    vy = -130
    initialV = set()
    while vy < 130:
        vx = 1
        while vx < max(x) + 1:
            isHit, __, pos = shoot(vx, vy, x, y)
            if isHit:
                initialV.add((vx, vy))
            vx += 1
        vy += 1

    return len(initialV)


if __name__ == '__main__':
    day = "17"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 5778
    assert b == 2576
