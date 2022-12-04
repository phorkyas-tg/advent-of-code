import os

def puzzleA(lines):
    isInCounter = 0

    for line in lines:
        s1, s2 = line.strip().split(",")

        s1Min, s1Max = map(int, s1.split("-"))
        s2Min, s2Max = map(int, s2.split("-"))

        # s1 is in s2
        if s1Min >= s2Min and s1Max <= s2Max:
            isInCounter += 1

        # s2 is in s1
        elif s2Min >= s1Min and s2Max <= s1Max:
            isInCounter += 1

    return isInCounter


def puzzleB(lines):
    overlapCounter = 0

    for line in lines:
        s1, s2 = line.strip().split(",")

        s1Min, s1Max = map(int, s1.split("-"))
        s2Min, s2Max = map(int, s2.split("-"))

        # s1 overlap s2
        if s1Min >= s2Min and s1Min <= s2Max:
            overlapCounter += 1

        # s2 overlap s1
        elif s2Min >= s1Min and s2Min <= s1Max:
            overlapCounter += 1
        
    return overlapCounter


if __name__ == '__main__':
    day = "04"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding = 'utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 526
    assert b == 886
