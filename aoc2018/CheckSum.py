def CountLetters(inputString):
    result = {}
    for letter in inputString:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result


def CalculateChecksum(input):
    twoLetterWords = 0
    threeLetterWords = 0

    for word in input:
        isTwoLetterWord = False
        isThreeLetterWord = False

        result = CountLetters(word)
        for count in result.values():
            if count == 2:
                isTwoLetterWord = True
            elif count == 3:
                isThreeLetterWord = True

        if isTwoLetterWord:
            twoLetterWords += 1
        if isThreeLetterWord:
            threeLetterWords += 1

    return twoLetterWords * threeLetterWords
