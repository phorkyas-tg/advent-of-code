def GetTwoEntriesWithSum(input, result):
    for i1 in range(len(input)):
        for i2 in range(i1+1, len(input)):
            if input[i1] + input[i2] == result:
                return input[i1], input[i2]


def MultiplyTwoEntriesWithSum(input, result):
    entry1, entry2 = GetTwoEntriesWithSum(input, result)
    return entry1 * entry2


def GetThreeEntriesWithSum(input, result):
    for i1 in range(len(input)):
        for i2 in range(i1+1, len(input)):
            for i3 in range(i1+1, len(input)):
                if input[i1] + input[i2] + input[i3] == result:
                    return input[i1], input[i2], input[i3]


def MultiplyThreeEntriesWithSum(input, result):
    entry1, entry2, entry3 = GetThreeEntriesWithSum(input, result)
    return entry1 * entry2 * entry3
