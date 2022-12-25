import os
from datetime import datetime


def numberToSnafu(n):
    b = 5

    digits = []
    while n:
        digits.append(int(n % b))
        n //= b

    snafu = ""
    carryOver = 0
    for d in digits:
        d += carryOver

        carryOver = d // 5
        d = d % 5

        if d == 3:
            snafu += "="
            carryOver += 1
        elif d == 4:
            snafu += "-"
            carryOver += 1
        else:
            snafu += str(d)

    if carryOver:
        snafu += str(carryOver)

    return snafu[::-1]

def puzzleA(lines):
    fuel = 0

    for line in lines:
        line = line.strip()
        length = len(line)
        
        for i, c in enumerate(line):
            if c == "=":
                c = "-2"
            if c == "-":
                c = "-1"
            
            fuel += pow(5, length - i - 1) * int(c)

    return numberToSnafu(fuel)


if __name__ == '__main__':
    day = "25"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    start = datetime.now()
    a = puzzleA(inputLines)
    stop = datetime.now()
    print(a)
    print("time: {0}".format(stop - start))
    assert a == "2=-0=01----22-0-1-10"
