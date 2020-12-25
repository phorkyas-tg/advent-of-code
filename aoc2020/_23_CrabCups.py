def GetNextValue(value, maxValue, blackList):
    while True:
        value -= 1
        if value in blackList:
            continue
        if value == 0:
            value = maxValue + 1
            continue
        return value


def ComputeCupLabels(cups, moves):
    maxValue = max(cups)

    # Example
    # (3) -> 8 -> 9 -> 1 -> 2 -> 5 -> 4 -> 6 -> 7 ->
    # Linked List (every value (index) points to the next value)
    # [0, 2, 5, 8, 6, 4, 7, 3, 9, 1]
    cupsLinkedList = [0] * (len(cups) + 1)
    for i in range(len(cups)):
        if i < len(cups) - 1:
            cupsLinkedList[cups[i]] = cups[i+1]
        else:
            cupsLinkedList[cups[i]] = cups[0]

    # currentCup = 3
    currentCup = cups[0]

    for i in range(moves):
        # picked up cups:
        # first, second, third = 8, 9, 1
        first = cupsLinkedList[currentCup]
        second = cupsLinkedList[first]
        third = cupsLinkedList[second]
        # nextCup = 2
        nextCup = cupsLinkedList[third]
        # get the nextValue after which the picked up cups must be placed
        # nextValue = 2
        nextValue = GetNextValue(currentCup, maxValue, [first, second, third])
        # get the value after the nextValue
        # valueAfter = 5
        valueAfter = cupsLinkedList[nextValue]

        # put everything together
        # currentCup points to nextCup: 3 -> 2
        cupsLinkedList[currentCup] = nextCup
        # nextValue points to first of the picked up cups: 2 -> 8
        cupsLinkedList[nextValue] = first
        # the last of the picked up cups points to the valueAfter: 1 -> 5
        cupsLinkedList[third] = valueAfter

        # the new currentCup is the nextCup: currentCup = 2
        # new LinkedList
        # 3 -> (2) -> 8 -> 9 -> 1 -> 5 -> 4 -> 6 -> 7 ->
        # which corresponds to
        # [0, 5, 8, 2, 6, 4, 7, 3, 9, 1]
        currentCup = nextCup

    return cupsLinkedList


def GetCupLabels(puzzleInput, moves):
    cups = list(map(int, [i for i in puzzleInput]))
    cupsLinkedList = ComputeCupLabels(cups, moves)

    result = ""
    cc = 1
    for __ in range(len(cups) - 1):
        cc = cupsLinkedList[cc]
        result += str(cc)
    return int(result)


def GetCupLabelsAdvanced(puzzleInput, numberOfCups, moves):
    cups = list(map(int, [i for i in puzzleInput]))
    maxValue = max(cups)
    addedValues = [i for i in range(maxValue + 1, numberOfCups + 1)]
    cups.extend(addedValues)

    cupsLinkedList = ComputeCupLabels(cups, moves)

    first = cupsLinkedList[1]
    second = cupsLinkedList[first]
    return first * second
