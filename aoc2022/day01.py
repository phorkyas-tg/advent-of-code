import os


def getSumOfCalories(lines):
    sumOfCalories = []

    currentCalories = 0
    for line in lines:
        if line == "\n":
            sumOfCalories.append(currentCalories)
            currentCalories = 0
        else:
            currentCalories += int(line)
    
    return sumOfCalories


def puzzleA(lines):
    return max(getSumOfCalories(lines))


def puzzleB(lines):
    sumOfCalories = getSumOfCalories(lines)

    first = max(sumOfCalories)
    sumOfCalories.remove(first)
    second = max(sumOfCalories)
    sumOfCalories.remove(second)
    third = max(sumOfCalories)

    return first + second + third


if __name__ == '__main__':
    day = "01"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 74711
    assert b == 209481
