def CountObjectsWhileTraversing(mapInput, right=3, down=1):
    objects = {}
    lineWidth = len(mapInput[0])

    # start is (0, 0)
    # always skip 'down' lines
    for i in range(0, len(mapInput), down):
        # normalise right step
        rightStep = int((i / down) * right)
        line = mapInput[i]
        # modulo for step size so that there is no overflow
        stepSize = rightStep % lineWidth

        char = line[stepSize]
        objects.setdefault(char, 0)
        objects[char] += 1

    return objects


def CountTreesWhileTraversing(mapInput, right=3, down=1):
    return CountObjectsWhileTraversing(mapInput, right, down)["#"]


def CountMultipleSlopes(mapinput):
    trees = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees *= CountTreesWhileTraversing(mapinput.copy(), right, down)
    return trees
