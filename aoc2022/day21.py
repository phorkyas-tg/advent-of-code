import os
from datetime import datetime


def puzzleA(lines):
    operations = []
    for line in lines:
        operations.append(line.strip().replace(":", " ="))

    while len(operations) > 0:
        newOperations = []
        for op in operations:
            try:
                exec(op)
            except NameError:
                newOperations.append(op)
        operations = newOperations

    return eval("int(root)")


def puzzleB(lines):
    operations = {}

    rootOp = ""
    for line in lines:
        var, op = line.strip().split(":")
        if var.startswith("humn"):
            continue

        if var.startswith("root"):
            rootOp = op.replace("+", "==").strip()
            continue

        operations[var.strip()] = op.strip()

    changed = True
    while changed:
        changed = False
        for var, op in operations.items():
            if var in rootOp:
                rootOp = rootOp.replace(var, op if op.isnumeric() else "({0})".format(op))
                changed = True

    left, right = rootOp.split(" == ")
    right = eval(right)

    i = 0
    step = 1000000000000

    while True:
        humn = i
        if eval(left) == right:
            return int(humn)
        if eval(left) < right:
            i -= step
            step /= 10

        i += step


if __name__ == '__main__':
    day = "21"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding='utf-8') as file:
        inputLines = file.readlines()

    start = datetime.now()
    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    stop = datetime.now()
    print(a)
    print(b)
    print("time: {0}".format(stop - start))
    assert a == 85616733059734
    assert b == 3560324848168
