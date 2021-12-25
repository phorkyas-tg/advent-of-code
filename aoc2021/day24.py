import math


def solve(lines, inpTemp, checkNumber, num=0, startNumber=9):
    while True:
        currentNumber = startNumber

        numberFound = True
        while numberFound:

            essentialInstruction = []
            register = {"w": [0], "x": [0], "y": [0], "z": [0]}
            inp = inpTemp.copy()
            inp[num] = [currentNumber]

            for n, line in enumerate(lines):
                op = line[:3]

                if op == "inp":
                    reg = line.strip()[-1]
                    register[reg] = inp.pop(0)
                    essentialInstruction.append(line)
                else:
                    op, r, val = line.strip().split()

                    reg = register.get(r)
                    if val in register:
                        val = register[val]
                    else:
                        val = [int(val)]

                    newReg = set()
                    for rg in reg:
                        for v in val:
                            if op == "mul":
                                newReg.add(rg * v)
                            elif op == "add":
                                newReg.add(rg + v)
                            elif op == "div":
                                newReg.add(math.floor(rg / v))
                            elif op == "mod":
                                newReg.add(rg % v)
                            elif op == "eql":
                                newReg.add(int(rg == v))
                            else:
                                raise NotImplementedError

                    newReg = list(newReg)
                    newReg.sort()

                    if newReg != reg:
                        essentialInstruction.append(line)
                        register[r] = newReg

            if 0 in register["z"]:
                inpTemp[num] = [currentNumber]
                break
            else:
                currentNumber, inpTemp, num, doBreak = checkNumber(currentNumber, inpTemp, num)
                if doBreak:
                    break

        num += 1
        if num >= 14:
            break

    return int("".join([str(n[0]) for n in inpTemp]))


def highestNumber(currentNumber, inpTemp, num):
    currentNumber -= 1
    doBreak = False

    if currentNumber < 1:
        q = 0
        for i in range(1, 14):
            q = i
            lastReg = inpTemp[num - i][0]
            if lastReg > 1:
                inpTemp[num - i] = [lastReg - 1]
                break
            else:
                inpTemp[num - i] = [i + 1 for i in range(9)]
        num -= q
        doBreak = True

    return currentNumber, inpTemp, num, doBreak


def lowestNumber(currentNumber, inpTemp, num):
    currentNumber += 1
    doBreak = False

    if currentNumber > 9:
        q = 0
        for i in range(1, 14):
            q = i
            lastReg = inpTemp[num - i][0]
            if lastReg < 9:
                inpTemp[num - i] = [lastReg + 1]
                break
            else:
                inpTemp[num - i] = [i + 1 for i in range(9)]
        num -= q
        doBreak = True
    return currentNumber, inpTemp, num, doBreak


def getInitialInp():
    return [[i + 1 for i in range(9)], [i + 1 for i in range(9)], [i + 1 for i in range(9)],
            [i + 1 for i in range(9)], [i + 1 for i in range(9)], [i + 1 for i in range(9)],
            [i + 1 for i in range(9)], [i + 1 for i in range(9)], [i + 1 for i in range(9)],
            [i + 1 for i in range(9)], [i + 1 for i in range(9)], [i + 1 for i in range(9)],
            [i + 1 for i in range(9)], [i + 1 for i in range(9)]]


def puzzleA(lines):
    inpTemp = getInitialInp()

    # this is a brute force algorithm that takes several minutes
    # to make it faster put in the first 3 digits: 91699394894995
    # if you want to get the real solution comment the next 4 lines
    inpTemp[0] = [9]
    inpTemp[1] = [1]
    inpTemp[2] = [6]
    num = 3

    return solve(lines, inpTemp, highestNumber, num, startNumber=9)


def puzzleB(lines):
    inpTemp = getInitialInp()

    num = 0

    # this is a brute force algorithm that takes several minutes
    # to make it faster put in the first 3 digits: 51147191161261
    # if you want to get the real solution comment the next 4 lines
    inpTemp[0] = [5]
    inpTemp[1] = [1]
    inpTemp[2] = [1]
    num = 3

    return solve(lines, inpTemp, lowestNumber, num, startNumber=1)


if __name__ == '__main__':
    day = "24"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 91699394894995
    assert b == 51147191161261
