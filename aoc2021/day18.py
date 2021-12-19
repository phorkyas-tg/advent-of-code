import re
import math


def explode(line):
    countOpenBrackets = 0
    for i, char in enumerate(line):
        if char == "[":
            countOpenBrackets += 1
        elif char == "]":
            countOpenBrackets -= 1

        if countOpenBrackets == 5:
            subString = line[i:]
            array = subString[0:subString.index("]") + 1]

            leftString = line[:i]
            rightString = subString.replace(array, "", 1)

            arr = eval(array)
            leftNumbers = re.findall(r'\d+', leftString)
            if len(leftNumbers) > 0:
                new = str(arr[0] + int(leftNumbers[-1]))
                leftString = new.join(leftString.rsplit(str(leftNumbers[-1]), 1))

            rightNumbers = re.findall(r'\d+', rightString)
            if len(rightNumbers) > 0:
                rightString = rightString.replace(str(rightNumbers[0]),
                                                  str(arr[1] + int(rightNumbers[0])), 1)

            return leftString + "0" + rightString
    return line


def split(line):
    numbers = [int(x) for x in re.findall(r'\d+', line) if int(x) > 9]
    firstNumber = None if len(numbers) == 0 else numbers[0]

    if firstNumber:
        array = "[{0},{1}]".format(int(math.floor(firstNumber / 2)),
                                   int(math.ceil(firstNumber / 2)))
        return line.replace(str(firstNumber), array, 1)
    return line


def getMagnitude(line):
    found = True

    while found:
        found = False
        for i, char in enumerate(line):
            if char == "[":
                nextClosingBracket = line.index("]", i + 1)
                try:
                    nextOpeningBracket = line.index("[", i + 1)
                except ValueError:
                    nextOpeningBracket = nextClosingBracket + 1

                if nextClosingBracket < nextOpeningBracket:
                    found = True
                    array = line[i:nextClosingBracket + 1]
                    arr = eval(array)

                    line = line.replace(array, str((3 * arr[0]) + (2 * arr[1])))
                    break

    return int(line)


def addLines(line1, line2):
    return "[" + line1 + "," + line2 + "]"


def reduce(line):
    while True:
        exlodedLine = explode(line)
        if exlodedLine != line:
            line = exlodedLine
            continue

        splittedLine = split(line)
        if splittedLine != line:
            line = splittedLine
            continue

        break
    return line


def puzzleA(lines):

    line = lines[0].strip()
    for i in range(1, len(lines)):
        nextLine = lines[i].strip()

        line = addLines(line, nextLine)
        line = reduce(line)

    return getMagnitude(line)


def puzzleB(lines):
    highestMagnitude = 0
    for i1 in range(len(lines)):
        firstLine = lines[i1].strip()
        for i2 in range(len(lines)):
            if i1 == i2:
                continue
            nextLine = lines[i2].strip()

            line = addLines(firstLine, nextLine)
            line = reduce(line)

            magnitude = getMagnitude(line)
            if magnitude > highestMagnitude:
                highestMagnitude = magnitude

    return highestMagnitude


if __name__ == '__main__':
    day = "18"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 3725
    assert b == 4832
