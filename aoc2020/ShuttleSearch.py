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
    for i in range(len(schedule)):
        if schedule[i] == "x":
            continue
        busIds.append([int(schedule[i]), i])

    pairs = []
    # get all busIds that happen at the same time. this is if the position of a busID can be
    # divided by another busId. example:
    # 7,13,x,x,59,x,31,19
    # 7 and 19 happen at the same time because 19 has the position 7 --> pairs = [7, 19]
    # additional append the relative position between the two busIds --> pairs = [7, 19, 7]
    for busId1 in busIds:
        for busId2 in busIds:
            if busId1[0] == busId2[0]:
                continue
            if (busId2[1] - busId1[1]) % busId1[0] == 0:
                pairs.append([busId1[0], busId2[0], (busId2[1] - busId1[1])])

    # the start pair is the first pair that was found
    pair = [0, 0, 0] if len(pairs) == 0 else pairs[0]
    # jump at least the distance of the product of the start pair. if there are other pairs which
    # share the same partner as the start pair multiply this number as well
    # Example:
    # pairs = [7, 100], [19, 100], [23, 140], [50, 100]
    # jump = start pair product * partner pairs = (7 * 100) * 19 * 50
    jump = 1 if pair == [0, 0, 0] else (pair[0] * pair[1])
    for i in range(1, len(pairs)):
        if pairs[i][1] == pairs[0][1]:
            jump *= pairs[i][0]

    j = jump
    while True:
        for i in range(len(schedule)):
            if schedule[i] == "x":
                continue
            # check if this value is dividable by the current busId
            # the pair happens both at the jump so you need to adjust the value by adding the
            # current position and subtract the relative position from the start pair
            # Example 7,13,x,x,59,x,31,19

            # pair = [7, 19, 7]
            # jump = 133

            # 1068780    .       .       .       .       .
            # 1068781    D       .       .       .       .
            # 1068782    .       D       .       .       .
            # 1068783    .       .       .       .       .
            # 1068784    .       .       .       .       .
            # 1068785    .       .       D       .       .
            # 1068786    .       .       .       .       .
            # 1068787    .       .       .       D       .
            # 1068788    D       .       .       .       D
            # 1068789    .       .       .       .       .

            # the time both busIds are the same is 1068788 - so you always jump to this position.
            # to check all values you need to start at 1068781 which is
            # 1068781 = 1068788 + (i=0 - 7)
            # 1068782 = 1068788 + (i=1 - 7)
            # ...
            if (j + (i - pair[2])) % int(schedule[i]) == 0:
                if i == len(schedule) - 1:
                    return j - pair[0]
            else:
                break
        j += jump
