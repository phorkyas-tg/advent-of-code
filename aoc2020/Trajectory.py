def CountTreesWhileTraversing(mapInput, right=3, down=1):
    objects = {"#": 0, ".": 0}
    lineWidth = len(mapInput[0])

    for i in range(down, len(mapInput), down):
        step = int((i / down) * right)
        line = mapInput[i]
        stepSize = (step % lineWidth)
        objects[line[stepSize]] += 1

    return objects["#"]


def CountMultipleSlopes(mapinput):
    trees = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees *= CountTreesWhileTraversing(mapinput.copy(), right, down)
    return trees
