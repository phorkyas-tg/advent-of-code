from collections import deque
from aocLib.Array import JumpIndexRollingBuffer


def GetBestScore(puzzleInput):
    players = puzzleInput[0]
    rounds = puzzleInput[1] + 1

    marbles = deque([0])
    marbleIndex = 0

    result = {}
    for r in range(1, rounds):
        if r % 23 == 0:
            currentPlayer = r % players
            # jump 7 to the left
            marbleIndex = JumpIndexRollingBuffer(marbleIndex, -7, len(marbles))
            fetchedMarble = marbles[marbleIndex+1]
            marbles.remove(fetchedMarble)
            result.setdefault(currentPlayer, 0)
            result[currentPlayer] += fetchedMarble + r

        else:
            # Jump 2 to the right
            marbleIndex = JumpIndexRollingBuffer(marbleIndex, 2, len(marbles))
            marbles.insert(marbleIndex+1, r)

    return max(result.values()) if result else 0


def GetBestScoreFast(puzzleInput):
    players = puzzleInput[0]
    rounds = puzzleInput[1] + 1

    marbles = deque([0])

    result = {}
    for r in range(1, rounds):
        if r % 23 == 0:
            currentPlayer = r % players
            # jump 7 to the left
            marbles.rotate(7)
            fetchedMarble = marbles.pop()
            result.setdefault(currentPlayer, 0)
            result[currentPlayer] += fetchedMarble + r
            # jump 1 to the right
            marbles.rotate(-1)
        else:
            # Jump 1 to the right
            marbles.rotate(-1)
            marbles.append(r)

    return max(result.values()) if result else 0



