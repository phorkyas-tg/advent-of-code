import os

def puzzleA(lines):
    totalScore = 0

    for line in lines:
        l, r = line.strip().split(" ")
        
        l = ord(l) - ord("A") + 1
        r = ord(r) - ord("X") + 1

        totalScore += r

        if l == r:
            totalScore += 3
        elif (l + 1 == r) or (l == 3 and r == 1):
            totalScore += 6

    return totalScore


def puzzleB(lines):
    totalScore = 0

    # map the score points for each condition to the left input
    loose = {"A": 3, "B": 1, "C": 2}
    draw = {"A": 1, "B": 2, "C": 3}
    win = {"A": 2, "B": 3, "C": 1}

    for line in lines:
        l, r = line.strip().split(" ")
        
        if r == "X":
            totalScore += loose.get(l)
        elif r == "Y":
            totalScore += 3
            totalScore += draw.get(l)
        else:
            totalScore += 6
            totalScore += win.get(l)

    return totalScore


if __name__ == '__main__':
    day = "02"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 11603
    assert b == 12725
