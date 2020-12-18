import re


def GetBoundingBox(stars):
    firstStar = next(iter(stars.keys()))

    xmin = xmax = firstStar[0]
    ymin = ymax = firstStar[1]

    for pos in stars.keys():
        if pos[0] < xmin:
            xmin = pos[0]
        if pos[0] > xmax:
            xmax = pos[0]
        if pos[1] < ymin:
            ymin = pos[1]
        if pos[1] > ymax:
            ymax = pos[1]

    return [xmin, xmax, ymin, ymax], abs(xmax - xmin) * abs(ymax - ymin)


def Move(stars):
    newStars = {}
    for pos, vels in stars.items():
        for vel in vels:
            x = pos[0] + vel[0]
            y = pos[1] + vel[1]
            newStars.setdefault((x, y), [])
            newStars[(x, y)].append(vel.copy())
    return newStars


def PrintStars(stars, boundingBox, log=False):
    result = []
    for y in range(boundingBox[2], boundingBox[3] + 1):
        line = ""
        for x in range(boundingBox[0], boundingBox[1] + 1):
            if (x, y) in stars:
                line += "#"
            else:
                line += "."
        result.append(line)
        if log:
            print(line)
    if log:
        print("\n")
    return result


def GetStarMessage(puzzleInput):
    stars = {}
    for line in puzzleInput.splitlines():
        pos, vel = re.findall(r"\<(.*?)\>", line)
        pos = tuple(map(int, pos.split(",")))
        vel = list(map(int, vel.split(",")))
        stars.setdefault(pos, [])
        stars[pos].append(vel)

    boundingBox, area = GetBoundingBox(stars)

    time = 0
    while True:
        newStars = Move(stars)
        newBoundingBox, newArea = GetBoundingBox(newStars)
        if newArea > area:
            break
        boundingBox = newBoundingBox
        area = newArea
        stars = newStars.copy()
        time += 1

    return PrintStars(stars, boundingBox), time

