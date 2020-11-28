import re


def GenerateEmptyCanvas(width, height):
    canvas = {}

    for i1 in range(width + 1):
        for i2 in range(height + 1):
            canvas["{0}-{1}".format(i1, i2)] = []

    return canvas


def ParseRectangleString(rectangeString):
    subStrings = re.findall(r"[\d']+", rectangeString)
    id = int(subStrings[0])
    xPos = int(subStrings[1])
    yPos = int(subStrings[2])
    width = int(subStrings[3])
    height= int(subStrings[4])
    return id, xPos, yPos, width, height


def AddRectangleToCanvas(canvas, rectangeString):
    id, xPos, yPos, width, height = ParseRectangleString(rectangeString)

    for i1 in range(xPos, xPos + width):
        for i2 in range(yPos, yPos + height):
            canvas["{0}-{1}".format(i1, i2)].append(id)


def GetMultipleClaimedSquares(input):
    canvas = GenerateEmptyCanvas(1000, 1000)

    for rectangeString in input:
        AddRectangleToCanvas(canvas, rectangeString)

    multipleClaimedSquares = 0
    for element in canvas.values():
        if len(element) > 1:
            multipleClaimedSquares += 1

    return multipleClaimedSquares


def GetIntactClaimId(input):
    canvas = GenerateEmptyCanvas(1000, 1000)

    for rectangeString in input:
        AddRectangleToCanvas(canvas, rectangeString)

    multipleClaimedSquares = {}
    for element in canvas.values():
        if len(element) > 1:
            for e in element:
                multipleClaimedSquares[e] = e

    for rectangeString in input:
        id, xPos, yPos, width, height = ParseRectangleString(rectangeString)
        if id not in multipleClaimedSquares:
            return id

    return None
