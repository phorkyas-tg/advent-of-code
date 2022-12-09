import os


def moveTail(head, tail):
    if head[1] == tail[1]:
        distance = head[0] - tail[0]
        if abs(distance) not in (0, 1):
            tail = (int(tail[0] + (distance / abs(distance))), tail[1])
    elif head[0] == tail[0]:
        distance = head[1] - tail[1]
        if abs(distance) not in (0, 1):
            tail = (tail[0], int(tail[1] + (distance / abs(distance))))
    else:
        distanceX = head[0] - tail[0]
        distanceY = head[1] - tail[1]
        if abs(distanceX) not in (0, 1) or abs(distanceY) not in (0, 1):
            tail = (int(tail[0] + (distanceX / abs(distanceX))),
                    int(tail[1] + (distanceY / abs(distanceY))))
    return tail


def processCommand(command, head):
    if command == "R":
        head = (head[0] + 1, head[1])
    elif command == "L":
        head = (head[0] - 1, head[1])
    elif command == "U":
        head = (head[0], head[1] + 1)
    elif command == "D":
        head = (head[0], head[1] - 1)
    return head


def puzzleA(lines):
    # y
    # ^
    # |
    # + - > x

    head = (0, 0)
    tail = (0, 0)
    visites = {tail}

    for line in lines:
        command, steps = line.strip().split(" ")
        for __ in range(int(steps)):
            head = processCommand(command, head)
            tail = moveTail(head, tail)

            visites.add(tail)
    return len(visites)


def puzzleB(lines):
    tails = [(0, 0)] * 10
    visites = {tails[9]}

    for line in lines:
        command, steps = line.strip().split(" ")
        for __ in range(int(steps)):
            tempTails = [processCommand(command, tails[0])]
            for i, tail in enumerate(tails):
                if i == 0:
                    continue
                tempTails.append(moveTail(tempTails[-1], tail))
            tails = tempTails

            visites.add(tails[9])
    return len(visites)


if __name__ == '__main__':
    day = "09"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding = 'utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 6503
    assert b == 2724
