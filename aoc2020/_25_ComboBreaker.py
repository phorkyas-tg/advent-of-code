def GetLoopSize(publicKey, subjectNumber=7):
    loopSize = 0
    value = 1
    while True:
        if value == publicKey:
            return loopSize
        value *= subjectNumber
        value = value % 20201227
        loopSize += 1


def CalculateEncryptionKey(subjectNumber, loopSize):
    value = 1
    for i in range(loopSize):
        value *= subjectNumber
        value = value % 20201227
        loopSize += 1
    return value


def GetEncryptionKey(puzzleInput):
    l1 = GetLoopSize(puzzleInput[0])
    return CalculateEncryptionKey(puzzleInput[1], l1)
