def GetBounds(activeNodes):
    dimensions = len(next(iter(activeNodes.keys())))
    bounds = [0 for __ in range(dimensions*2)]
    for activeNode in activeNodes.keys():
        for d in range(dimensions):
            if activeNode[d] < bounds[d * 2]:
                bounds[d * 2] = activeNode[d]
            if activeNode[d] > bounds[d * 2 + 1]:
                bounds[d * 2 + 1] = activeNode[d]

    for d in range(dimensions):
        bounds[d * 2] -= 1
        bounds[d * 2 + 1] += 2

    return bounds


def CountAdjacentNodes3D(pos, activeNodes, terminate):
    count = 0
    for x in [pos[0] - 1, pos[0], pos[0] + 1]:
        for y in [pos[1] - 1, pos[1], pos[1] + 1]:
            for z in [pos[2] - 1, pos[2], pos[2] + 1]:
                if (x, y, z) == pos:
                    continue
                if (x, y, z) in activeNodes:
                    count += 1
                    if count >= terminate:
                        return count
    return count


def Cycle3D(activeNodes):
    # getBounds
    xmin, xmax, ymin, ymax, zmin, zmax = GetBounds(activeNodes)

    newActiveNodes = {}
    for z in range(zmin, zmax):
        for y in range(ymin, ymax):
            for x in range(xmin, xmax):
                isActive = False
                if (x, y, z) in activeNodes:
                    isActive = True

                if isActive and CountAdjacentNodes3D((x, y, z), activeNodes, 4) in [2, 3]:
                    newActiveNodes[(x, y, z)] = 1
                elif isActive is False and CountAdjacentNodes3D((x, y, z), activeNodes, 4) == 3:
                    newActiveNodes[(x, y, z)] = 1
    return newActiveNodes


def GetActiveCubes3D(puzzleInput):
    # x, y, z
    activeNodes = {}
    for y, line in enumerate(puzzleInput.splitlines()):
        for x, node in enumerate(line):
            if node == "#":
                activeNodes[(x, y, 0)] = 1

    for __ in range(6):
        activeNodes = Cycle3D(activeNodes)

    return len(activeNodes.values())


def CountAdjacentNodes4D(pos, activeNodes, terminate):
    count = 0
    for x in [pos[0] - 1, pos[0], pos[0] + 1]:
        for y in [pos[1] - 1, pos[1], pos[1] + 1]:
            for z in [pos[2] - 1, pos[2], pos[2] + 1]:
                for w in [pos[3] - 1, pos[3], pos[3] + 1]:
                    if (x, y, z, w) == pos:
                        continue
                    if (x, y, z, w) in activeNodes:
                        count += 1
                        if count >= terminate:
                            return count
    return count


def Cycle4D(activeNodes):
    # getBounds
    xmin, xmax, ymin, ymax, zmin, zmax, wmin, wmax = GetBounds(activeNodes)

    newActiveNodes = {}
    for z in range(zmin, zmax):
        for y in range(ymin, ymax):
            for x in range(xmin, xmax):
                for w in range(wmin, wmax):
                    isActive = False
                    if (x, y, z, w) in activeNodes:
                        isActive = True

                    if isActive and CountAdjacentNodes4D((x, y, z, w), activeNodes, 4) in [2, 3]:
                        newActiveNodes[(x, y, z, w)] = 1
                    elif isActive is False and \
                            CountAdjacentNodes4D((x, y, z, w), activeNodes, 4) == 3:
                        newActiveNodes[(x, y, z, w)] = 1
    return newActiveNodes


def GetActiveCubes4D(puzzleInput):
    # x, y, z, w
    activeNodes = {}
    for y, line in enumerate(puzzleInput.splitlines()):
        for x, node in enumerate(line):
            if node == "#":
                activeNodes[(x, y, 0, 0)] = 1

    for __ in range(6):
        activeNodes = Cycle4D(activeNodes)

    return len(activeNodes.values())
