import os


def puzzleA(lines):
    trees = {}
    visibleTrees = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            trees[(x, y)] = int(c)
            visibleTrees[(x, y)] = 1

    xMax, yMax = max(trees.keys())

    def setVisibleTrees(pos, highestTree):
        value = trees[pos]

        if pos[0] == 0 or pos[0] == xMax or pos[1] == 0 or pos[1] == yMax or value > highestTree:
            visibleTrees[pos] = 0

        if highestTree < value:
            highestTree = value
        return highestTree

    def lookAtTreesHorizontal(x1, x2, xStep):
        for _y in range(yMax + 1):
            highestTree = -1
            for _x in range(x1, x2, xStep):
                highestTree = setVisibleTrees((_x, _y), highestTree)

    def lookAtTreesVertical(y1, y2, yStep):
        for _x in range(xMax + 1):
            highestTree = -1
            for _y in range(y1, y2, yStep):
                highestTree = setVisibleTrees((_x, _y), highestTree)

    # from left
    lookAtTreesHorizontal(0, xMax + 1, 1)
    # from right
    lookAtTreesHorizontal(xMax, -1, -1)
    # from up
    lookAtTreesVertical(0, yMax + 1, 1)
    # from down
    lookAtTreesVertical(yMax, -1, -1)

    return len(visibleTrees.keys()) - sum(visibleTrees.values())


def puzzleB(lines):
    trees = {}
    visibleTrees = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            trees[(x, y)] = int(c)
            visibleTrees[(x, y)] = 0

    xMax, yMax = max(trees.keys())

    for pos, value in trees.items():
        right = left = up = down = 1

        if pos[0] == 0 or pos[0] == xMax or pos[1] == 0 or pos[1] == yMax:
            continue

        for x in range(pos[0] + 1, xMax):
            if value > trees[(x, pos[1])]:
                right += 1
            else:
                break
        
        for x in range(pos[0] - 1, 0, -1):
            if value > trees[(x, pos[1])]:
                left += 1
            else:
                break

        for y in range(pos[1] + 1, yMax):
            if value > trees[(pos[0], y)]:
                down += 1
            else:
                break

        for y in range(pos[1] - 1, 0, -1):
            if value > trees[(pos[0], y)]:
                up += 1
            else:
                break

        visibleTrees[pos] = right * left * up * down

    return max(visibleTrees.values())


if __name__ == '__main__':
    day = "08"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 1794
    assert b == 199272
