def CalculateHammingDistance(word1, word2):
    hammingDistance = 0
    commonChars = ""

    if len(word1) != len(word2):
        raise NotImplementedError

    for n in range(len(word1)):
        if word1[n] != word2[n]:
            hammingDistance += 1
        else:
            commonChars += word1[n]

    return hammingDistance, commonChars


def GetCommonCharsFromIds(input):
    for i1 in range(len(input)):
        for i2 in range(i1 + 1, len(input)):
            hd, cc = CalculateHammingDistance(input[i1], input[i2])
            if hd == 1:
                return cc
    return None
