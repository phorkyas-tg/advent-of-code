def BinarySpacePartitioning(inputString, highBit):
    value = ""
    for bit in inputString:
        if bit == highBit:
            value += "1"
        else:
            value += "0"
    return int(value, 2)


def GetRowColumnIdFromInputStr(inputStr):
    row = BinarySpacePartitioning(inputStr[:-3], highBit="B")
    column = BinarySpacePartitioning(inputStr[-3:], highBit="R")
    return row, column, (row * 8) + column


def GetBSPDict(listOfInput):
    bspDict = {}
    for inputStr in listOfInput:
        row, column, seatId = GetRowColumnIdFromInputStr(inputStr)
        bspDict[inputStr] = seatId
    return bspDict


def GetHigherstSeatID(listOfInput):
    bspDict = GetBSPDict(listOfInput)
    highestId = 0
    for sid in bspDict.values():
        if sid > highestId:
            highestId = sid
    return highestId


def GetMySeatID(listOfInput):
    bspDict = GetBSPDict(listOfInput)
    sortedIds = []
    for seatId in bspDict.values():
        sortedIds.append(seatId)
    sortedIds.sort()

    for i in range(len(sortedIds)):
        if sortedIds[i] + 2 == sortedIds[i+1]:
            return sortedIds[i] + 1
