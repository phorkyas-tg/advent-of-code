from collections import Counter


def GetMostCommon(d):
    highest = max(d.values())
    allHighest = [char for char, val in d.items() if val == highest]
    for h in allHighest:
        del d[h]
    allHighest.sort()
    return "".join(allHighest)


def SumValidRoomIds(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    idSum = 0
    for line in inputLines:
        line = line.strip().split("-")

        name = Counter("".join(line[:-1]))

        mostCommon = ""
        while len(mostCommon) < 5:
            mostCommon += GetMostCommon(name)
        mostCommon = mostCommon[:5]

        num, checkSum = line[-1].split("[")
        num = int(num)
        checkSum = checkSum[:-1]

        if checkSum == mostCommon:
            idSum += num
    return idSum


def ShiftCypher(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    for line in inputLines:
        line = line.strip().split("-")

        name = "_".join(line[:-1])
        num = int(line[-1].split("[")[0])

        decriptedName = ""
        for char in name:
            if char == "_":
                decriptedName += " "
                continue

            rollChar = ord(char) + (num % 26)
            decriptedName += chr(rollChar if rollChar <= 122
                                 else 97 + rollChar - 123)
        if decriptedName == "northpole object storage":
            return num
    return 0




