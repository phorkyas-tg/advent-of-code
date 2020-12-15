def GetNextBus(puzzleInput):
    startTime = int(puzzleInput[0])
    busIds = [int(p) for p in puzzleInput[1].split(",") if p != "x"]

    currentTime = startTime
    while True:
        for busId in busIds:
            if currentTime % busId == 0:
                return (currentTime - startTime) * busId
        currentTime += 1


def GetSpecialScheduleTime(puzzleInput):

    schedule = puzzleInput[1].split(",")

    busIds = []
    # get all busIds and the position
    for i, busId in enumerate(schedule):
        if busId != "x":
            busIds.append([int(busId), i])

    pairStruct = {}
    # get all busIds that occur at the same time
    for busId1 in busIds:
        for busId2 in busIds:
            if busId1[0] != busId2[0] and (busId2[1] - busId1[1]) % busId1[0] == 0:
                pairStruct.setdefault(busId2[0], [])
                pairStruct[busId2[0]].append(busId1[0])
    # add all other busIds to the struct
    for busId in busIds:
        for key, values in pairStruct.items():
            if busId[0] == key or busId in values:
                break
        else:
            pairStruct.setdefault(busId[0], [])

    jumps = []
    for key, values in pairStruct.items():
        j = key
        for value in values:
            j *= value
        for busId in busIds:
            if busId[0] == key:
                jumps.append([j, busId[1]])
                break
    jumps.sort()
    jumps = jumps[::-1]

    jumpWidth = jumps[0][0]
    offset = jumps[0][1]

    j = jumpWidth
    while True:
        for jump in jumps[1:]:
            if (j + (jump[1] - offset)) % jump[0] != 0:
                break
        else:
            return j - offset
        j += jumpWidth
