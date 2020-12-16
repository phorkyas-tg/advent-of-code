def GetFirstWrongNumber(puzzleInput, preambleLength):
    currentPreamble = [puzzleInput[p] for p in range(preambleLength)]
    for i in range(preambleLength, len(puzzleInput)):
        for p in currentPreamble:
            if puzzleInput[i] - p != p and puzzleInput[i] - p in currentPreamble:
                break
        else:
            return puzzleInput[i]
        currentPreamble.pop(0)
        currentPreamble.append(puzzleInput[i])


def GetContiguousNumber(puzzleInput, invalidNumber):
    for start in range(len(puzzleInput)):
        contiguousNumbers = [puzzleInput[start]]
        result = puzzleInput[start]
        for n in range(start+1, len(puzzleInput)):
            result += puzzleInput[n]
            contiguousNumbers.append(puzzleInput[n])
            if result == invalidNumber:
                return min(contiguousNumbers) + max(contiguousNumbers)
            elif result > invalidNumber:
                break
