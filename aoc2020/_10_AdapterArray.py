def CountJolts(puzzleInput):
    puzzleInput.append(0)
    puzzleInput.append(max(puzzleInput) + 3)
    puzzleInput.sort()

    result = {1: 0, 2: 0, 3: 0}
    for i in range(1, len(puzzleInput)):
        result[puzzleInput[i] - puzzleInput[i-1]] += 1

    return result[1] * result[3]


def GetCombinations(sequence, combination=None, result=None):
    """
    Get all combinations from a sequence. You must visit the first and the last number and can
    only jump 1 - 3 steps

     Note: only works for small sequences

    Example sequence = [1, 2, 3, 4]
    --> possible combinations:
    [1, 2, 3, 4]
    [1, 2, 4]
    [1, 3, 4]
    [1, 4]
    """
    sequence.sort()

    currentValue = sequence[0]
    maxValue = max(sequence)

    if combination is None:
        combination = []
    if result is None:
        result = []
    combination.append(currentValue)

    for i in [1, 2, 3]:
        if currentValue + i in sequence and currentValue + i <= maxValue:
            newSequence = [v for v in sequence if v >= currentValue + i]
            result = GetCombinations(newSequence, combination.copy(), result)

    if combination[-1] == maxValue and combination not in result:
        result.append(combination)
    return result


def CountPossibleArrangements(puzzleInput):
    """
    1) Find all sub sequences - a sub sequence is a list of all numbers where the
    distance to the last sub sequence is 3 (max distance)
    Example:
        sequence = [1, 2, 3, 4, 7, 9] --> [[1, 2, 3, 4], [7, 9]]
        In this example every possible arrangement must use the numbers 1, 4, 7, 9
        because 1 and 9 is the first/last number and there is no way to skip 4 and 7 because
        they have the (max) distance of 3 and nothing in between

    2) the length of one sequence corresponds to the number of possible combinations, e.g.
        len == 2 --> 1 combination
        len == 3 --> 2 combinations
        len == 4 --> 4 combinations
        len == 5 --> 7 combinations
        ...

    3) The result is the product of all possible combinations af all sub sequences:
        sequence = [1, 2, 3, 4, 7, 9]

        --> Possible combinations are:
        [1, 2, 3, 4, 7, 9]
        [1, 2, 4, 7, 9]
        [1, 3, 4, 7, 9]
        [1, 4, 7, 9]

        or with the algorithm:
        result = combinations([1, 2, 3, 4]) * combinations([7, 9]) = 4 * 1 = 4
    """
    puzzleInput.append(0)
    puzzleInput.append(max(puzzleInput) + 3)
    puzzleInput.sort()

    possibleArrangements = 1
    while len(puzzleInput) > 0:
        subSequence = [puzzleInput.pop(0)]

        while len(puzzleInput) > 0:
            if puzzleInput[0] - subSequence[-1] < 3:
                nxt = puzzleInput.pop(0)
                subSequence.append(nxt)
            else:
                break

        # sub sequence must be greater 2, if not the number of combinations are 1 so there is no
        # need to save it
        if len(subSequence) > 2:
            possibleArrangements *= len(GetCombinations(subSequence))

    return possibleArrangements
