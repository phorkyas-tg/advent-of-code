import os
from datetime import datetime
from collections import deque


def puzzleA(lines):
    queue = deque([])
    init = []
    for i, line in enumerate(lines):
        numb = int(line.strip())
        queue.append((numb, i))
        init.append(numb)

    for i, numb in enumerate(init):
        numbIndex = queue.index((numb, i))
        queue.rotate(-numbIndex)
        current, __ = queue.popleft()
        queue.rotate(-numb)
        queue.appendleft((current, True))

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
        numb = int(line.strip()) * key
        queue.append((numb, i))
        init.append(numb)

    for loop in range(10):
        for i, numb in enumerate(init):
            numbIndex = queue.index((numb, i))
            queue.rotate(-numbIndex)
            current, __ = queue.popleft()
            queue.rotate(-numb)
            queue.appendleft((current, i if loop < 9 else True))

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
