import os


def moveTail(head, tail):
    distanceX = head[0] - tail[0]
    distanceY = head[1] - tail[1]

    if head[1] == tail[1]:
        if abs(distanceX) not in (0, 1):
            tail = (int(tail[0] + (distanceX / abs(distanceX))), tail[1])
    elif head[0] == tail[0]:
        if abs(distanceY) not in (0, 1):
            tail = (tail[0], int(tail[1] + (distanceY / abs(distanceY))))
    else:
        if abs(distanceX) not in (0, 1) or abs(distanceY) not in (0, 1):
            tail = (int(tail[0] + (distanceX / abs(distanceX))),
                    int(tail[1] + (distanceY / abs(distanceY))))
    return tail


def moveHead(head, command):
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
            head = moveHead(head, command)
            tail = moveTail(head, tail)

            visites.add(tail)
    return len(visites)


def puzzleB(lines):
    links = [(0, 0)] * 10
    visites = {links[-1]}

    for line in lines:
        command, steps = line.strip().split(" ")
        for __ in range(int(steps)):
            tempLinks = [moveHead(links[0], command)]
            for i, tail in enumerate(links):
                if i == 0:
                    continue
                tempLinks.append(moveTail(tempLinks[-1], tail))
            links = tempLinks

            visites.add(links[-1])
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
