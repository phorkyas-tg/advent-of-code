def GetGroupResult(groupInput):
    result = {}
    for declaration in groupInput:
        for letter in declaration:
            result.setdefault(letter, 0)
            result[letter] += 1
    return result


def SumOfDeclarationCounts(puzzleInput):
    count = 0
    for group in puzzleInput:
        count += len(GetGroupResult(group).keys())
    return count


def SumOfDeclarationCountsAdvanced(puzzleInput):
    count = 0
    for group in puzzleInput:
        numberOfAnswers = len(group)
        for value in GetGroupResult(group).values():
            if value == numberOfAnswers:
                count += 1
    return count
