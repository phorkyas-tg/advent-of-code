import os

def puzzleA(lines):
    return 0


def puzzleB(lines):
    return 0


if __name__ == '__main__':
    day = "01"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding = 'utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 0
    assert b == 0
