def puzzleA(lines):
    lines = list(map(int, lines))

    count = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            count += 1
    return count


def puzzleB(lines):
    lines = list(map(int, lines))

    newArray = []
    for i in range(len(lines) - 2):
        newArray.append(lines[i] + lines[i+1] + lines[i+2])
    return puzzleA(newArray)


if __name__ == '__main__':
    file = open("input\\input_01.txt", 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 1292
    assert b == 1262
