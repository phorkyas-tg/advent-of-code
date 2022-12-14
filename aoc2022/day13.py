import os
from functools import cmp_to_key


def compare(left, right):
    # 0 = left == right or unknown
    # -1 = left < right
    # 1 = left > right
    result = 0

    # print("Compare {0} vs {1}".format(left, right))
    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            try:
                result = compare(left[i], right[i])
            except IndexError:
                # print("Right side ran out of items, so inputs are not in the right order")
                result = 1

            if result in (-1, 1):
                return result
        if result == 0 and len(left) < len(right):
            # print("Left side ran out of items, so inputs are in the right order")
            return -1

    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            # print("Left side is smaller, so inputs are in the right order")
            return -1
        elif left == right:
            return 0
        # print("Right side is smaller, so inputs are not in the right order")
        return 1

    elif isinstance(left, list) and isinstance(right, int):
        right = [right]
        # print("Mixed types; convert right to {0} and retry comparison".format(right))
        result = compare(left, right)
        if result in (-1, 1):
            return result

    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        # print("Mixed types; convert right to {0} and retry comparison".format(left))
        result = compare(left, right)
        if result in (-1, 1):
            return result

    return result


def bubbleSort(packets):
    swapped = True
    while swapped:
        swapped = False

        for i in range(1, len(packets)):
            comp = compare(packets[i-1], packets[i])
            # swap
            if comp == 1:
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
        comp = compare(pair[0], pair[1])

        if comp == -1:
            indices.append(i + 1)

    return sum(indices)


def puzzleB(lines):
    packets = [[[2]], [[6]]]

    for line in lines:
        if line.strip() == "":
            continue

        packets.append(eval(line.strip()))

    packets.sort(key=cmp_to_key(compare))
    # As an alternative you can use bubble sort
    # packets = bubbleSort(packets)

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
