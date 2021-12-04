def puzzleA(lines):
    return 0


def puzzleB(lines):
    return 0


if __name__ == '__main__':
    day = "01"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 0
    assert b == 0
