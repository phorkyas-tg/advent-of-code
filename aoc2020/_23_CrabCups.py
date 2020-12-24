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

    cupsLinkedList = [0] * (len(cups) + 1)
    for i in range(len(cups)):
        if i < len(cups) - 1:
            cupsLinkedList[cups[i]] = cups[i+1]
        else:
            cupsLinkedList[cups[i]] = cups[0]

    currentCup = cups[0]

    for i in range(moves):
        first = cupsLinkedList[currentCup]
        second = cupsLinkedList[first]
        third = cupsLinkedList[second]
        nextCup = cupsLinkedList[third]

        nextValue = GetNextValue(currentCup, maxValue, [first, second, third])
        valueAfter = cupsLinkedList[nextValue]

        cupsLinkedList[currentCup] = nextCup
        cupsLinkedList[nextValue] = first
        cupsLinkedList[third] = valueAfter

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
