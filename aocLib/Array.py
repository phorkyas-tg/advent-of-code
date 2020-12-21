def JumpIndexRollingBuffer(index, n, lengthOfArray):
    """
    Return the Index after jumping n steps. If the index reaches the end start at the front of
    the array (rolling buffer).

    Example:
     array = [0, 1, 2, 3, 4, 5]

     JumpIndexRollingBuffer(1, 2, 6) --> 3
     JumpIndexRollingBuffer(1, 3, 6) --> 4
     JumpIndexRollingBuffer(5, -2, 6) --> 1

    :param index: current index
    :type index: int
    :param n: steps
    :type n: int
    :param lengthOfArray: length of the array
    :type lengthOfArray: int
    :return: index after jump
    :rtype: int
    """
    return (index + n) % lengthOfArray


def RotateLeft(puzzleArray):
    """
    Rotate an Array:

    #..     ...
    ... --> ...
    ...     #..

    :type puzzleArray: list(str)
    :rtype: list(str)
    """
    newArray = [""] * len(puzzleArray[0])
    for line in puzzleArray:
        for i, char in enumerate(line):
            newArray[-i - 1] += char
    return newArray


def FlipVertical(puzzleArray):
    """
    Vertical flip an Array:

    #..     ..#
    ... --> ...
    #.#     #.#

    :type puzzleArray: list(str)
    :rtype: list(str)
    """
    newArray = []
    for line in puzzleArray:
        newArray.append(line[::-1])
    return newArray


def FlipHorizontal(puzzleArray):
    """
    Horizontal flip an Array:

    #..     #.#
    ... --> ...
    #.#     #..

    :type puzzleArray: list(str)
    :rtype: list(str)
    """
    return puzzleArray[::-1]


def ConcatPieces(piece1, piece2):
    """
    Concat 2 Arrays:

    ...   ###     ...###
    ... + ### --> ...###
    ...   ###     ...###

    :type piece1: list(str)
    :type piece2: list(str)
    :rtype: list(str)
    """
    for i in range(len(piece1)):
        piece1[i] += piece2[i]
    return piece1


def RemoveBorder(puzzleArray):
    """
    Remove Border:

    ###
    #.# --> .
    ###

    :type puzzleArray: list(str)
    :rtype: list(str)
    """
    newArray = []
    for line in puzzleArray:
        newArray.append(line[1:-1])
    return newArray[1:-1]
