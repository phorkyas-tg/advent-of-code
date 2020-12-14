def GetSumOfRegisters(puzzleInput):
    register = {}

    andMask = 0
    orMask = 0
    for command in puzzleInput:
        c, value = command.split(" = ")
        if c == "mask":
            andMask = int(value.replace("X", "1"), 2)
            orMask = int(value.replace("X", "0"), 2)
        else:
            mem = c.split("[")
            regNumber = int(mem[1][:-1])
            register[regNumber] = (int(value) & andMask) | orMask

    return sum(register.values())


def GetMaskCombinations(bitMask):
    # replace all 1s with 0s for the or operation later
    bitMasks = [bitMask.replace("1", "0")]

    while True:
        replaced = False
        bmTemp = []
        for bm in bitMasks:
            if "X" in bm:
                bmTemp.append(bm.replace("X", "1", 1))
                bmTemp.append(bm.replace("X", "0", 1))
                replaced = True
        if replaced is False:
            break
        bitMasks = bmTemp.copy()

    return [int(value, 2) for value in bitMasks]


def GetSumOfFloatingRegisters(puzzleInput):
    register = {}

    orMask = 0
    subMask = 0
    masks = []
    for command in puzzleInput:
        c, value = command.split(" = ")
        if c == "mask":
            masks = GetMaskCombinations(value)
            orMask = int(value.replace("X", "0"), 2)
            subMask = int(value.replace("0", "1").replace("X", "0"), 2)
        else:
            mem = c.split("[")
            regNumber = int(mem[1][:-1])
            # orMask: first mask the signal 0 -> no change, 1 -> overwrite with 1
            # subMask: replace all X pos with 0, the rest must not change
            # mask: put on the mask where the X pos float and the rest is the same
            for r in [((regNumber | orMask) & subMask) | mask for mask in masks]:
                register[r] = int(value)

    return sum(register.values())
