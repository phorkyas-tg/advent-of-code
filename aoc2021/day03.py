def puzzleA(lines):
    msb = ""
    lsb = ""
    for i in range(len(lines[0]) - 1):
        zeros, ones = getBitCount(lines, i)

        if ones > zeros:
            msb += "1"
            lsb += "0"
        else:
            msb += "0"
            lsb += "1"

    return int(msb, 2) * int(lsb, 2)


def getBitCount(lines, i):
    zeros = 0
    ones = 0

    for line in lines:
        if line[i] == "0":
            zeros += 1
        else:
            ones += 1
    return zeros, ones


def puzzleB(lines):
    o = oxygenGeneratorRating(lines)
    s = c02scrubberRating(lines)
    return int(o, 2) * int(s, 2)


def c02scrubberRating(lines):
    return rating(lines, "0", "1")


def oxygenGeneratorRating(lines):
    return rating(lines, "1", "0")


def rating(lines, condition1, condition2):
    newLines = lines.copy()
    for i in range(len(lines[0]) - 1):
        zeros, ones = getBitCount(newLines, i)

        tempLines = []
        for line in newLines:
            if (ones > zeros or ones == zeros) and line[i] == condition1:
                tempLines.append(line)
            elif zeros > ones and line[i] == condition2:
                tempLines.append(line)

        newLines = tempLines.copy()
        if len(newLines) == 1:
            break

    return newLines[0]


if __name__ == '__main__':
    day = "03"
    file = open("input\\input_{0}.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 2595824
    assert b == 2135254
