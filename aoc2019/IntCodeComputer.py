def ReadParameter(commandString, input, i, offset):
    try:
        x = int(commandString[-2 - offset])
    except IndexError:
        x = 0
    try:
        if x == 0:
            return input[input[i + offset]]
        else:
            return input[i + offset]
    except IndexError:
        return 0


def ReadCommand(input, i):
    commandString = str(input[i])

    if len(commandString) == 1:
        opCode = int(commandString[0])
    else:
        opCode = int(commandString[-2] + commandString[-1])

    c = ReadParameter(commandString, input.copy(), i, 1)
    b = ReadParameter(commandString, input.copy(), i, 2)
    a = ReadParameter(commandString, input.copy(), i, 3)

    return opCode, a, b, c


def IntCodeComputer(puzzleInput, inputParameter=1):
    i = 0
    output = []

    while i < len(puzzleInput):
        opCode, a, b, c = ReadCommand(puzzleInput, i)

        jump = 0
        # stop program
        if opCode == 99:
            break
        # add
        elif opCode == 1:
            puzzleInput[puzzleInput[i + 3]] = c + b
            jump += 4
        # mult
        elif opCode == 2:
            puzzleInput[puzzleInput[i + 3]] = c * b
            jump += 4
        # read input
        elif opCode == 3:
            puzzleInput[puzzleInput[i + 1]] = inputParameter
            jump += 2
        # write output
        elif opCode == 4:
            output.append(c)
            jump += 2
        # jump if true
        elif opCode == 5:
            if c != 0:
                i = b
            else:
                jump += 3
        # jump if false
        elif opCode == 6:
            if c == 0:
                i = b
            else:
                jump += 3
        # is less
        elif opCode == 7:
            if c < b:
                puzzleInput[puzzleInput[i + 3]] = 1
            else:
                puzzleInput[puzzleInput[i + 3]] = 0
            jump += 4
        # is less
        elif opCode == 8:
            if c == b:
                puzzleInput[puzzleInput[i + 3]] = 1
            else:
                puzzleInput[puzzleInput[i + 3]] = 0
            jump += 4
        else:
            raise Exception

        i += jump

    return puzzleInput, output


def FindVerbNoun(input, outValue):
    for noun in range(99):
        for verb in range(99):
            inputTemp = input.copy()
            inputTemp[1] = noun
            inputTemp[2] = verb

            try:
                ga = IntCodeComputer(inputTemp)[0]
                if ga[0] == outValue:
                    return (100 * noun) + verb
            except IndexError:
                pass
