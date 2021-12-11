def stripLine(line):
    line = line.strip()
    lineLength = len(line)
    while True:
        line = line.replace("()", "").replace("<>", "").replace("{}", "").replace("[]", "")
        if lineLength > len(line):
            lineLength = len(line)
            continue
        return line


def puzzleA(lines):
    ret = 0

    for line in lines:
        line = stripLine(line)

        firstAppearance = [line.find(")"), line.find("]"), line.find("}"), line.find(">")]
        lowestNumbers = [i for i in firstAppearance if i >= 0]
        lowestIndex = None if len(lowestNumbers) == 0 else firstAppearance.index(min(lowestNumbers))

        if lowestIndex == 0:
            ret += 3
        elif lowestIndex == 1:
            ret += 57
        elif lowestIndex == 2:
            ret += 1197
        elif lowestIndex == 3:
            ret += 25137

    return ret


def puzzleB(lines):
    pointList = []

    for line in lines:
        line = stripLine(line)

        firstAppearance = [line.find(")"), line.find("]"), line.find("}"), line.find(">")]

        # incomplete lines
        if max(firstAppearance) == -1:
            line = line[::-1]

            points = 0
            for c in line:
                points = points * 5
                if c == "(":
                    points += 1
                elif c == "[":
                    points += 2
                elif c == "{":
                    points += 3
                elif c == "<":
                    points += 4
            pointList.append(points)

    pointList.sort()

    return pointList[len(pointList) // 2]


if __name__ == '__main__':
    day = "10"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 243939
    assert b == 2421222841
