import re
from aocLib.Array import RotateLeft, FlipVertical, ConcatPieces, RemoveBorder


def GetCornerTiles(puzzleInput):
    puzzlePieces = {}

    pieces = puzzleInput.split("\n\n")
    for piece in pieces:
        piece = piece.splitlines()
        pieceId = int(re.findall(r"\d+|$", piece[0])[0])

        top = piece[1]
        buttom = piece[len(piece) - 1]
        left = ""
        right = ""
        for p in piece[1:]:
            left += p[0]
            right += p[len(p) - 1]

        puzzlePieces[pieceId] = [top, right, buttom, left]

    cornerTiles = []
    for puzzleId1, corners1 in puzzlePieces.items():
        matchedCorners = [0, 0, 0, 0]
        for puzzleId2, corners2 in puzzlePieces.items():
            if puzzleId1 == puzzleId2:
                continue
            for i, corner1 in enumerate(corners1):
                if corner1 in corners2 or corner1[::-1] in corners2:
                    matchedCorners[i] = 1
                    break
        if sum(matchedCorners) == 2:
            cornerTiles.append(puzzleId1)

    result = 1
    for tileId in cornerTiles:
        result *= tileId
    return result


def GetCorners(puzzleArray):
    top = puzzleArray[0]
    buttom = puzzleArray[len(puzzleArray) - 1]
    left = ""
    right = ""
    for p in puzzleArray[0:]:
        left += p[0]
        right += p[len(p) - 1]

    return [top, right, buttom, left]


def MatchPieces(piece1, piece2, corner1, corner2):
    c1 = GetCorners(piece1)[corner1]
    c2 = GetCorners(piece2)[corner2]

    if c2 == c1:
        return piece2
    # rotate 3 times
    piece = piece2.copy()
    for __ in range(3):
        piece = RotateLeft(piece.copy())
        c2 = GetCorners(piece)[corner2]
        if c2 == c1:
            return piece

    # flip vertical
    piece = FlipVertical(piece2.copy())
    c2 = GetCorners(piece)[corner2]
    if c2 == c1:
        return piece
    # rotate 3 times
    for __ in range(3):
        piece = RotateLeft(piece.copy())
        c2 = GetCorners(piece)[corner2]
        if c2 == c1:
            return piece

    return None


def CountSeaMonster(puzzleArray):
    seeMonster = [r"(.|#){18}#(.|#)",
                  r"#(.|#){4}##(.|#){4}##(.|#){4}###",
                  r"(.|#)#(.|#){2}#(.|#){2}#(.|#){2}#(.|#){2}#(.|#){2}#(.|#){3}"]

    count = 0
    for i in range(len(puzzleArray[:-2])):
        for i2 in range(len(puzzleArray[0]) - 19):
            if re.match(seeMonster[0], puzzleArray[i][i2:i2+20]) and \
                    re.match(seeMonster[1], puzzleArray[i+1][i2:i2+20]) and \
                    re.match(seeMonster[2], puzzleArray[i+2][i2:i2+20]):
                count += 1

    return count


def CountAllSeaMonster(puzzleArray):
    count = CountSeaMonster(puzzleArray)
    if count > 0:
        return count
    # rotate
    for __ in range(3):
        puzzleArray = RotateLeft(puzzleArray)
        count = CountSeaMonster(puzzleArray)
        if count > 0:
            return count

    # flip
    puzzleArray = FlipVertical(puzzleArray)
    count = CountSeaMonster(puzzleArray)
    if count > 0:
        return count

    # rotate
    for __ in range(3):
        puzzleArray = RotateLeft(puzzleArray)
        count = CountSeaMonster(puzzleArray)
        if count > 0:
            return count

    return 0


def GetWaterRoughness(puzzleInput):
    puzzlePieces = {}

    pieces = puzzleInput.split("\n\n")
    for piece in pieces:
        piece = piece.splitlines()
        pieceId = int(re.findall(r"\d+|$", piece[0])[0])
        puzzlePieces[pieceId] = piece[1:]

    correctPuzzle = {}
    firstPieceKey = next(iter(puzzlePieces))
    firstPiece = puzzlePieces.pop(firstPieceKey)
    correctPuzzle[(0, 0)] = firstPiece

    while len(puzzlePieces) > 0:
        for loacation, piece in correctPuzzle.items():
            for nextPieceId, nextPiece in puzzlePieces.items():

                combinations = [[(loacation[0] + 1, loacation[1]), 1, 3],
                                [(loacation[0] - 1, loacation[1]), 3, 1],
                                [(loacation[0], loacation[1] - 1), 0, 2],
                                [(loacation[0], loacation[1] + 1), 2, 0]]

                for nextLocation, c1, c2 in combinations:
                    if nextLocation not in correctPuzzle:
                        newPiece = MatchPieces(piece.copy(), nextPiece.copy(),
                                               corner1=c1, corner2=c2)
                        if newPiece is not None:
                            correctPuzzle[nextLocation] = newPiece
                            puzzlePieces.pop(nextPieceId)
                            break
                else:
                    continue
                break
            else:
                continue
            break

    xMin = xMax = yMin = yMax = 0
    for x, y in correctPuzzle.keys():
        if x > xMax:
            xMax = x
        if x < xMin:
            xMin = x
        if y > yMax:
            yMax = y
        if y < yMin:
            yMin = y

    completePuzzleLines = []
    # concat puzzles pieces and remove border
    for y in range(yMin, yMax + 1):
        line = RemoveBorder(correctPuzzle[(xMin, y)].copy())
        for x in range(xMin + 1, xMax + 1):
            line = ConcatPieces(line, RemoveBorder(correctPuzzle[(x, y)].copy()))
        completePuzzleLines.extend(line)

    # a sea monster consists of 15 tiles
    seamonsterTiles = CountAllSeaMonster(completePuzzleLines) * 15

    countHashes = 0
    for line in completePuzzleLines:
        for char in line:
            if char == "#":
                countHashes += 1

    return countHashes - seamonsterTiles
