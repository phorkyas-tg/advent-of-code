import os
from datetime import datetime
from collections import deque


def puzzleA(lines):
    queue = deque([])
    init = []
    for i, line in enumerate(lines):
        number = int(line.strip())
        queue.append((number, i))
        init.append(number)

    for i, number in enumerate(init):
        numberIndex = queue.index((number, i))
        queue.rotate(-numberIndex)
        queue.popleft()
        queue.rotate(-number)
        queue.appendleft((number, True))

    i0 = queue.index((0, True))
    queue.rotate(-i0)

    result = 0
    for __ in range(3):
        queue.rotate(-1000)
        val, __ = queue[0]
        result += val

    return result


def puzzleB(lines):
    queue = deque([])
    init = []

    key = 811589153

    for i, line in enumerate(lines):
        number = int(line.strip()) * key
        queue.append((number, i))
        init.append(number)

    for loop in range(10):
        for i, number in enumerate(init):
            numberIndex = queue.index((number, i))
            queue.rotate(-numberIndex)
            queue.popleft()
            queue.rotate(-number)
            queue.appendleft((number, i if loop < 9 else True))

    i0 = queue.index((0, True))
    queue.rotate(-i0)

    result = 0
    for __ in range(3):
        queue.rotate(-1000)
        val, __ = queue[0]
        result += val

    return result


if __name__ == '__main__':
    day = "20"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    start = datetime.now()
    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    stop = datetime.now()
    print(a)
    print(b)
    print("time: {0}".format(stop - start))
    assert a == 1087
    assert b == 13084440324666
