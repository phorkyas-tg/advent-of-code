def puzzleA(lines):
    hor = 0
    depth = 0

    for line in lines:
        cmd, nmb = line.split(" ")
        nmb = int(nmb)

        if cmd == "forward":
            hor += nmb
        elif cmd == "down":
            depth += nmb
        elif cmd == "up":
            depth -= nmb
        else:
            raise NotImplementedError

    return hor * depth


def puzzleB(lines):
    hor = 0
    depth = 0
    aim = 0

    for line in lines:
        cmd, nmb = line.split(" ")
        nmb = int(nmb)

        if cmd == "forward":
            hor += nmb
            depth += nmb * aim
        elif cmd == "down":
            aim += nmb
        elif cmd == "up":
            aim -= nmb
        else:
            raise NotImplementedError

    return hor * depth


if __name__ == '__main__':
    file = open("input\\input_02.txt", 'r')
    inputLines = file.readlines()
    file.close()

    print(puzzleA(inputLines))
    print(puzzleB(inputLines))
