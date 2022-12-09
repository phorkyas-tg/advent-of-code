import os

def puzzleA(lines):
    line = lines[0].strip()
    markerLenght = 4

    for i in range(len(line) - (markerLenght - 1)):
        marker = set(line[i:i+markerLenght])
        if len(marker) == markerLenght:
            return i + markerLenght

    return 0


def puzzleB(lines):
    line = lines[0].strip()
    markerLenght = 14

    for i in range(len(line) - (markerLenght - 1)):
        marker = set(line[i:i+markerLenght])
        if len(marker) == markerLenght:
            return i + markerLenght

    return 0


if __name__ == '__main__':
    day = "06"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 1987
    assert b == 3059
