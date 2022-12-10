import os


def puzzleA(lines):
    registerX = 1
    cycleCount = 0

    cycles = dict()

    for line in lines:
        command = line.strip()[:4]

        cycles[cycleCount] = registerX
        cycleCount += 1

        if command == "addx":
            cycles[cycleCount] = registerX
            cycleCount += 1

            number = int(line.strip()[4:])
            registerX += number

    strength = 0
    for c in (20, 60, 100, 140, 180, 220):
        strength += cycles[c - 1] * c
    return strength


def puzzleB(lines):
    registerX = 1

    screen = ""
    row = ""

    def addPixelToRow(row, screen):
        if len(row) in (registerX -1, registerX, registerX + 1):
            row += "#"
        else:
            row += "."
        if len(row) == 40:
            screen += row + "\n"
            row = ""
        return row, screen

    for line in lines:
        command = line.strip()[:4]

        row, screen = addPixelToRow(row, screen)

        if command == "addx":
            row, screen = addPixelToRow(row, screen)

            number = int(line.strip()[4:])
            registerX += number

    return screen


if __name__ == '__main__':
    day = "10"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 13220
    assert b == "###..#..#..##..#..#.#..#.###..####.#..#.\n#..#.#..#.#..#.#.#..#..#.#..#.#....#.#..\n#..#.#..#.#..#.##...####.###..###..##...\n###..#..#.####.#.#..#..#.#..#.#....#.#..\n#.#..#..#.#..#.#.#..#..#.#..#.#....#.#..\n#..#..##..#..#.#..#.#..#.###..####.#..#.\n"
