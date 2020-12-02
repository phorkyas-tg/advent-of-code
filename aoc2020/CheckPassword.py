def ParsePasswordPolicy(inputString):
    occourance, letter, password = inputString.split(" ")
    minOccourance, maxOccourance = occourance.split("-")
    letter = letter[0]

    return int(minOccourance), int(maxOccourance), letter, password


def CountLetters(inputString, char):
    occourance = 0
    for letter in inputString:
        if letter == char:
            occourance += 1
    return occourance


def CheckValidPasswords(inputStrings):
    validPasswords = 0

    for inputString in inputStrings:
        minOccourance, maxOccourance, letter, password = ParsePasswordPolicy(inputString)
        occourance = CountLetters(password, letter)
        if minOccourance <= occourance <= maxOccourance:
            validPasswords += 1
    return validPasswords


def CheckValidPasswordsAdvanced(inputStrings):
    validPasswords = 0

    for inputString in inputStrings:
        firstOccourance, secondOccourance, letter, password = ParsePasswordPolicy(inputString)
        if (password[firstOccourance-1] == letter and password[secondOccourance-1] != letter) or (
                password[firstOccourance-1] != letter and password[secondOccourance-1] == letter):
            validPasswords += 1
    return validPasswords

