def GetSpokenNumber(puzzleInput, terminate):
    numbers = {}
    start = 0
    lastNumber = 0

    for i, number in enumerate(puzzleInput):
        numbers.setdefault(number, [])
        numbers[number].append(i)

        start = i
        lastNumber = number

    for i in range(start + 1, terminate):
        if len(numbers[lastNumber]) == 1:
            number = 0
        else:
            number = numbers[lastNumber][1] - numbers[lastNumber][0]

        numbers.setdefault(number, [])
        numbers[number].append(i)
        if len(numbers[number]) == 3:
            numbers[number].pop(0)
        lastNumber = number

    return lastNumber
