import os


def parsePuzzleInput(lines):
    crates = {}
    moves = []

    isMoves = False
    for line in lines:
        if line == "\n":
            isMoves = True
            continue

        if isMoves:
            command = []
            for move in line.strip().split(" "):
                if move.isnumeric():
                    command.append(int(move))
            moves.append(command)
            continue

        # get the crates
        crate = line.replace("    ", "?")
        crate = crate.replace("[", "").replace("]", "")
        crate = crate.replace(" ", "").strip()
        
        for i, c in enumerate(crate):
            if c == "?" or c.isnumeric():
                continue
            crates.setdefault(i + 1, [])
            crates[i + 1].append(c)

    # reverse the crates
    for key in crates.keys():
        crates[key] = crates[key][::-1]

    return crates, moves


def puzzleA(lines):
    crates, moves = parsePuzzleInput(lines)

    for move in moves:
        for __ in range(move[0]):
            crates[move[2]].append(crates[move[1]].pop())

    topStack = ""
    for key in range(len(crates.keys())):
        topStack += crates[key + 1].pop()

    return topStack


def puzzleB(lines):
    crates, moves = parsePuzzleInput(lines)

    for move in moves:
        stack = []
        for __ in range(move[0]):
            stack.append(crates[move[1]].pop())
        crates[move[2]].extend(stack[::-1])

    topStack = ""
    for key in range(len(crates.keys())):
        topStack += crates[key + 1].pop()

    return topStack


if __name__ == '__main__':
    day = "05"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == "VQZNJMWTR"
    assert b == "NLCDCLVMQ"
