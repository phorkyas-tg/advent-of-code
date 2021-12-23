def intersection(cube1, cube2):
    xmin, xmax = max(cube1[0], cube2[0]), min(cube1[1], cube2[1])
    ymin, ymax = max(cube1[2], cube2[2]), min(cube1[3], cube2[3])
    zmin, zmax = max(cube1[4], cube2[4]), min(cube1[5], cube2[5])

    if xmin <= xmax and ymin <= ymax and zmin <= zmax:
        return xmin, xmax, ymin, ymax, zmin, zmax

    return None


def getVoulme(cube):
    return (cube[1] - cube[0] + 1) * (cube[3] - cube[2] + 1) * (cube[5] - cube[4] + 1)


def puzzleA(lines):
    cubes = {}
    for line in lines:
        state, pos = line.strip().split(" ")

        x, y, z = pos.split(",")
        xmin, xmax = list(map(int, x[2:].split("..")))
        ymin, ymax = list(map(int, y[2:].split("..")))
        zmin, zmax = list(map(int, z[2:].split("..")))

        newSign = 1 if state == "on" else -1
        newCube = (xmin, xmax, ymin, ymax, zmin, zmax)
        newCube = intersection(newCube, (-50, 50, -50, 50, -50, 50))
        if newCube is None:
            continue

        intersections = {}
        for cube, sign in cubes.items():
            inter = intersection(newCube, cube)
            if inter is None:
                continue
            intersections.setdefault(inter, 0)
            intersections[inter] -= sign

        for inter, sign in intersections.items():
            if sign == 0:
                continue
            cubes[inter] = cubes.get(inter, 0) + sign

        if newSign == 1:
            cubes.setdefault(newCube, 0)
            cubes[newCube] += newSign

    return sum(sign * getVoulme(cube) for cube, sign in cubes.items())


def puzzleB(lines):
    cubes = {}
    for line in lines:
        state, pos = line.strip().split(" ")

        x, y, z = pos.split(",")
        xmin, xmax = list(map(int, x[2:].split("..")))
        ymin, ymax = list(map(int, y[2:].split("..")))
        zmin, zmax = list(map(int, z[2:].split("..")))

        newSign = 1 if state == "on" else -1
        newCube = (xmin, xmax, ymin, ymax, zmin, zmax)

        intersections = {}
        for cube, sign in cubes.items():
            inter = intersection(newCube, cube)
            if inter is None:
                continue
            intersections.setdefault(inter, 0)
            intersections[inter] -= sign

        for inter, sign in intersections.items():
            if sign == 0:
                continue
            cubes[inter] = cubes.get(inter, 0) + sign

        if newSign == 1:
            cubes.setdefault(newCube, 0)
            cubes[newCube] += newSign

    return sum(sign * getVoulme(cube) for cube, sign in cubes.items())


if __name__ == '__main__':
    day = "22"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 601104
    assert b == 1262883317822267
