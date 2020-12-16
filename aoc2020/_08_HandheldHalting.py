def BuildInstructionDict(puzzleInput, switch=None):
    result = {}
    switchCounter = 0
    for i in range(len(puzzleInput)):
        op, nmb = puzzleInput[i].split(" ")

        if switch is not None and op in ("nop", "jmp"):
            if switchCounter == switch:
                if op == "nop":
                    op = "jmp"
                else:
                    op = "nop"
            switchCounter += 1

        result[i] = [op, int(nmb), 0]
    return result


def RunInstructions(instructions):
    instructionsLength = len(instructions.keys())
    acc = 0
    infiniteLoop = True

    i = 0

    while i < instructionsLength:
        op, nmb, visited = instructions[i]

        if visited > 0:
            break
        # increase visited
        instructions[i][2] += 1

        if op == "nop":
            pass
        elif op == "acc":
            acc += nmb
        elif op == "jmp":
            i += nmb-1

        i += 1
    else:
        infiniteLoop = False

    return acc, infiniteLoop


def GetLastAcc(puzzleInput):
    instructions = BuildInstructionDict(puzzleInput)
    return RunInstructions(instructions)[0]


def GetLastAccAfterTermination(puzzleInput):
    for switch in range(len(puzzleInput)):
        instructions = BuildInstructionDict(puzzleInput.copy(), switch)
        acc, infiniteLoop = RunInstructions(instructions)
        if infiniteLoop is False:
            return acc
