import os
import math

def getPrio(char):
    asciiVal = ord(char)
    if asciiVal >= ord("a"):
        asciiVal -= ord("a")
        asciiVal += 1
    else:
        asciiVal -= ord("A")
        asciiVal += 27
    return asciiVal


def puzzleA(lines):
    prios = 0

    for line in lines:
        line = line.strip()

        middle = math.floor(len(line)/2)
        comp1 = line[0:middle]
        comp2 = line[middle:]

        for char in comp1:
            if char in comp2:
                prios += getPrio(char)
                break

    return prios


def puzzleB(lines):
    prios = 0
    for i in range(0, len(lines), 3):
        ruck1 = lines[i].strip()
        ruck2 = lines[i + 1].strip()
        ruck3 = lines[i + 2].strip()

        for char in ruck1:
            if char in ruck2 and char in ruck3:
                prios += getPrio(char)
                break

    return prios


if __name__ == '__main__':
    day = "03"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 7568
    assert b == 2780
