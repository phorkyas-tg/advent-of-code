def rotate(p1, rot, axis):
    return p1[rot[0]] * axis[0], p1[rot[1]] * axis[1], p1[rot[2]] * axis[2]


def getScannerPos(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2]


def shift(scannerPos, p1):
    return scannerPos[0] - p1[0], scannerPos[1] - p1[1], scannerPos[2] - p1[2]


def diffScanners(scnr, scannerN, scanner0=0):
    p0Set = set(scnr[scanner0])

    # rotate the axis in all possible ways
    for rot in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        # go through all directions of the axis
        for x in [1, -1]:
            for y in [1, -1]:
                for z in [1, -1]:
                    axis = (x, y, z)
                    # rotate all positions
                    pNRot = [rotate(pN, rot, axis) for pN in scnr[scannerN]]
                    # there are 12 shared beacons - so the last 11 can be skipped
                    scannerPosCount = {}
                    # count all possible scanner positions
                    for pN in pNRot:
                        for p0 in scnr[scanner0]:
                            # calculate where the scanner would be
                            scannerPos = getScannerPos(pN, p0)
                            scannerPosCount.setdefault(scannerPos, 0)
                            scannerPosCount[scannerPos] += 1
                    if max(scannerPosCount.values()) >= 12:
                        for scannerPos, count in scannerPosCount.items():
                            if count == max(scannerPosCount.values()):
                                print("Scanner {0}: {1}".format(scannerN, scannerPos))
                                # shift all rotated points by the scanner position
                                pNShift = set([shift(scannerPos, p1) for p1 in pNRot])
                                scnr[scanner0].extend(list(pNShift - p0Set))
                                return scnr[scanner0], scannerPos
    return None, None


def puzzleA(lines):
    scannerNumber = 0
    scanners = {scannerNumber: []}
    for line in lines:
        if line.startswith("---"):
            continue

        if line == "\n":
            scannerNumber += 1
            scanners.setdefault(scannerNumber, [])
            continue

        pos = tuple(map(int, line.strip().split(",")))
        scanners[scannerNumber].append(pos)

    distances = []
    newBeacon = True
    scannedBeacons = [0]
    while newBeacon:
        newBeacon = False

        for i in scanners.keys():
            if i in scannedBeacons:
                continue

            scanner0, scanner1 = diffScanners(scanners, i)
            if scanner0 is None:
                continue

            newBeacon = True
            distances.append(scanner1)
            scannedBeacons.append(i)
            scanners[0] = scanner0

    return len(scanners[0]), distances


def puzzleB(distances):
    hightestManhattan = 0
    for i1, p1 in enumerate(distances):
        for i2, p2 in enumerate(distances):
            if i1 == i2:
                continue
            manhattan = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
            if manhattan > hightestManhattan:
                hightestManhattan = manhattan
    return hightestManhattan


if __name__ == '__main__':
    day = "19"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    # this one takes a while
    from datetime import datetime
    start = datetime.now()
    a, scannerPositions = puzzleA(inputLines)
    b = puzzleB(scannerPositions)
    stop = datetime.now()
    print("time: {0}", stop - start)
    print(a)
    print(b)
    assert a == 376
    assert b == 10772
