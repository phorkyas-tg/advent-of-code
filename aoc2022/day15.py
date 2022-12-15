import os
import re


def overlaps(s1Min, s1Max, s2Min, s2Max):
    if s2Min <= s1Min <= s2Max:
        return True

    elif s1Min <= s2Min <= s1Max:
        return True

    elif s1Max + 1 == s2Min:
        return True

    elif s2Max + 1 == s1Min:
        return True

    return False


def addRange(covered, y, left, right):
    covered.setdefault(y, [])

    newRange = (left, right)
    toDelete = None
    for r in covered[y]:
        if overlaps(newRange[0], newRange[1], r[0], r[1]):
            if toDelete is None:
                toDelete = [(r[0], r[1])]
            else:
                toDelete.append((r[0], r[1]))
            newRange = (min(newRange[0], r[0]), max(newRange[1], r[1]))

    if toDelete is not None:
        for r in toDelete:
            covered[y].remove(r)
    covered[y].append(newRange)
    return covered


def parseCoverage(lines):
    covered = {}
    sensorsAndBeacons = {}

    for line in lines:
        print(line.strip())
        sx, sy, bx, by = list(map(int, re.findall('[-+]?[0-9]+', line)))
        manhattan = abs(sx - bx) + abs(sy - by)

        sensorsAndBeacons[(sx, sy)] = "S"
        sensorsAndBeacons[(bx, by)] = "B"

        for y in range(manhattan + 1):
            up = sy - y
            down = sy + y
            left = sx - (manhattan - y)
            right = sx + (manhattan - y)

            if 0 <= up <= 4000000:
                covered = addRange(covered, up, left, right)

            if 0 <= down <= 4000000:
                covered = addRange(covered, down, left, right)
    return covered, sensorsAndBeacons


def puzzleA(covered, sensorsAndBeacons):
    count = 0
    row = 2000000
    for r in covered[row]:
        count += r[1] + 1 - r[0]
        for sAndB in [key for key in sensorsAndBeacons.keys() if key[1] == row]:
            if overlaps(sAndB[0], sAndB[1], r[0], r[1]):
                count -= 1
    return count


def puzzleB(covered):
    for y, rList in covered.items():
        if len(rList) == 2:
            x = min([pos[1] for pos in rList]) + 1
            return 4000000 * x + y


if __name__ == '__main__':
    day = "15"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    coveredDict, sensorsAndBeaconsDict = parseCoverage(inputLines)
    a = puzzleA(coveredDict, sensorsAndBeaconsDict)
    b = puzzleB(coveredDict)
    print(a)
    print(b)
    assert a == 4985193
    assert b == 11583882601918
