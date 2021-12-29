import re
from collections import Counter


def GetSubCount(line, oldFactor=1):
    count = Counter()

    while True:
        match = re.search("\((.*?)\)", line)

        if match is None:
            if line != "":
                count[line] += 1
            break

        start, stop = match.span()
        length, factor = map(int, re.findall("\d+", match.group()))

        pre = line[0:start]
        if pre != "":
            count[pre] += 1

        commandLine = line[stop: stop + length]
        count[commandLine] += factor * oldFactor

        line = line[stop + length:]

    return count


def GetDecombressedLength(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    line = inputLines[0].strip()
    count = GetSubCount(line)

    total = 0
    for substring, factor in count.items():
        total += len(substring) * factor

    return total


def GetFullDecombressedLength(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    line = inputLines[0].strip()
    count = GetSubCount(line)

    foundNewSubstring = True
    while foundNewSubstring:
        foundNewSubstring = False

        for substring, factor in count.items():
            match = re.search("\((.*?)\)", substring)

            if match is None:
                continue

            count += GetSubCount(substring, factor)
            del count[substring]
            foundNewSubstring = True
            break

        if not foundNewSubstring:
            break

    total = 0
    for substring, factor in count.items():
        total += len(substring) * factor

    return total





