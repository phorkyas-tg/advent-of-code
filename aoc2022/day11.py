import os
import math


def parseMonkeys(lines):
    lineNumber = 0

    monkeys = dict()
    monkeyOrder = []

    name = ""
    startItems = []
    operations = []
    divisible = 0
    ifTrue = ""
    ifFalse = ""

    for line in lines:
        if line.strip() == "":
            continue
        
        if lineNumber == 0:
            name = line.strip().split(":")[0].lower()
        elif lineNumber == 1:
            startItems = [int(item.strip()) for item in line.strip().split(":")[1].split(",")]
        elif lineNumber == 2:
            operations = line.strip().split("=")[1].strip()
        elif lineNumber == 3:
            divisible = int(line.strip().split(" ")[-1])
        elif lineNumber == 4:
            ifTrue = line.strip().split("to")[1].strip()
        elif lineNumber == 5:
            ifFalse = line.strip().split("to")[1].strip()
            monkeys[name] = {"sItems": startItems, "ops": operations, "divisible": divisible, 'ifTrue': ifTrue, "ifFalse": ifFalse}
            monkeyOrder.append(name)
            lineNumber = 0
            continue

        lineNumber += 1
    return monkeys, monkeyOrder


def puzzleA(lines):
    monkeys, monkeyOrder = parseMonkeys(lines)

    monkeyInspections = dict()

    for __ in range(20):
        for monkey in monkeyOrder:
            monkeyInspections.setdefault(monkey, 0)

            for old in monkeys[monkey]["sItems"]:
                monkeyInspections[monkey] += 1

                newVal = eval(monkeys[monkey]["ops"])
                newVal = math.floor(newVal / 3)
                if newVal % monkeys[monkey]["divisible"] == 0:
                    monkeys[monkeys[monkey]["ifTrue"]]["sItems"].append(newVal)
                else:
                    monkeys[monkeys[monkey]["ifFalse"]]["sItems"].append(newVal)
            monkeys[monkey]["sItems"] = []
    

    inspected = list(monkeyInspections.values())
    mValue1 = max(inspected)
    inspected.remove(mValue1)
    mValue2 = max(inspected)

    return mValue1 * mValue2


def puzzleB(lines):
    monkeys, monkeyOrder = parseMonkeys(lines)

    monkeyInspections = dict()
    
    leastCommonMultiple = 1
    for monkey in monkeyOrder:
        leastCommonMultiple *= monkeys[monkey]["divisible"]

    for __ in range(10000):
        for monkey in monkeyOrder:
            monkeyInspections.setdefault(monkey, 0)

            for old in monkeys[monkey]["sItems"]:
                monkeyInspections[monkey] += 1

                newVal = eval(monkeys[monkey]["ops"])
                newVal = newVal % leastCommonMultiple

                if newVal % monkeys[monkey]["divisible"] == 0:
                    monkeys[monkeys[monkey]["ifTrue"]]["sItems"].append(newVal)
                else:
                    monkeys[monkeys[monkey]["ifFalse"]]["sItems"].append(newVal)
            monkeys[monkey]["sItems"] = []
    

    inspected = list(monkeyInspections.values())
    mValue1 = max(inspected)
    inspected.remove(mValue1)
    mValue2 = max(inspected)

    return mValue1 * mValue2


if __name__ == '__main__':
    day = "11"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 90294
    assert b == 18170818354
