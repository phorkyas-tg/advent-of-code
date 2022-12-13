import os


def compare(left, right):
    # 0 = left == right
    # 1 = left < right
    # -1 = left > right
    setIndex = 0

    # print("Compare {0} vs {1}".format(left, right))
    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            try:
                setIndex = compare(left[i], right[i])
            except IndexError:
                setIndex = -1

            if setIndex in (-1, 1):
                return setIndex
        # left side ran out of items
        if setIndex == 0 and len(left) < len(right):
            return 1

    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            # print("Left side is smaller, so inputs are in the right order")
            return 1
        elif left == right:
            return 0
        # print("Right side is smaller, so inputs are not in the right order")
        return -1

    elif isinstance(left, list) and isinstance(right, int):
        right = [right]
        setIndex = compare(left, right)
        if setIndex in (-1, 1):
            return setIndex

    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        setIndex = compare(left, right)
        if setIndex in (-1, 1):
            return setIndex

    return setIndex


def bubbleSort(packets):
    swapped = True
    while swapped:
        swapped = False

        for i in range(1, len(packets)):
            comp = compare(packets[i-1], packets[i])
            # swap
            if comp == -1:
                p1 = packets[i-1]
                p2 = packets[i]

                packets[i] = p1
                packets[i - 1] = p2
                swapped = True

    return packets


def puzzleA(lines):
    packetPairs = []

    pair = []
    for line in lines:
        if line.strip() == "":
            packetPairs.append(pair)
            pair = []
            continue

        pair.append(eval(line.strip()))
    if pair:
        packetPairs.append(pair)

    indices = []
    for i, pair in enumerate(packetPairs):
        setIndex = compare(pair[0], pair[1])

        if setIndex == 1:
            indices.append(i + 1)

    return sum(indices)


def puzzleB(lines):
    packets = [[[2]], [[6]]]

    for line in lines:
        if line.strip() == "":
            continue

        packets.append(eval(line.strip()))

    packets = bubbleSort(packets)

    result = 1
    for i, p in enumerate(packets):
        if p in ([[2]], [[6]]):
            result *= i + 1

    return result


if __name__ == '__main__':
    day = "13"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 5905
    assert b == 21691
