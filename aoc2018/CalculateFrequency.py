def CalculateFrequency(input):
    frequency = 0
    for i in input:
        frequency += i
    return frequency


def CalculateFrequencyDuplicate(input):
    currentFrequency = 0
    visitedFrequencies = {0: 0}

    while True:
        for i in input:
            currentFrequency += i
            if currentFrequency in visitedFrequencies:
                return currentFrequency
            visitedFrequencies[currentFrequency] = currentFrequency
