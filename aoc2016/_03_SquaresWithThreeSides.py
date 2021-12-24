def GetValidTriangles(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    count = 0

    for line in inputLines:
        a, b, c = list(map(int, line.strip().split()))
        if a + b > c and a + c > b and b + c > a:
            count += 1

    return count


def GetValidVerticalTriangles(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    count = 0

    for i in range(0, len(inputLines), 3):
        a1, a2, a3 = list(map(int, inputLines[i].strip().split()))
        b1, b2, b3 = list(map(int, inputLines[i + 1].strip().split()))
        c1, c2, c3 = list(map(int, inputLines[i + 2].strip().split()))

        if a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1:
            count += 1
        if a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2:
            count += 1
        if a3 + b3 > c3 and a3 + c3 > b3 and b3 + c3 > a3:
            count += 1

    return count





