import string


def GenerateStringPairs():
    uc = string.ascii_uppercase
    lc = string.ascii_lowercase

    stringPairs = []
    for i in range(len(uc)):
        stringPairs.extend(["{0}{1}".format(uc[i], lc[i]), "{1}{0}".format(uc[i], lc[i])])

    return stringPairs


def CalculateLenAfterReactions(polymer):
    stringPairs = GenerateStringPairs()

    lastLength = len(polymer) + 1
    while len(polymer) < lastLength:
        lastLength = len(polymer)
        for sp in stringPairs:
            polymer = polymer.replace(sp, "")

    return len(polymer)


def GetShortestPolymerAfterImprovement(polymer):
    minPolymerLength = len(polymer) + 1
    for letter in string.ascii_lowercase:
        # copy polymer
        polymerTemp = "{:s}".format(polymer)

        polymerTemp = polymerTemp.replace(letter, "")
        polymerTemp = polymerTemp.replace(letter.upper(), "")

        polymerLen = CalculateLenAfterReactions(polymerTemp)
        if polymerLen < minPolymerLength:
            minPolymerLength = polymerLen

    return minPolymerLength
