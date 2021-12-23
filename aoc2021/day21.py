import collections
from itertools import permutations, combinations_with_replacement


def roll(pos, die):
    moves = 0
    for i in range(3):
        moves += die[0]
        die.rotate(-1)

    return (pos + moves) % 10, die


def getDieCombinations(die):
    combinations = []
    for combi in combinations_with_replacement(die, len(die)):
        for permutation in permutations(combi):
            if permutation not in combinations:
                combinations.append(permutation)

    combisPerRoll = {}
    for combi in combinations:
        combisPerRoll.setdefault(sum(combi), 0)
        combisPerRoll[sum(combi)] += 1
    return combisPerRoll


def quantumRoll(boardState, combisPerRoll, player):
    newBoardState = {}
    for moves, numberOfMoves in combisPerRoll.items():
        for currentPos, numberOfUniverses in boardState.items():
            nPos = (currentPos[player] + moves) % 10
            nScore = nPos + 1
            nPos = (nPos, currentPos[1], currentPos[2] + nScore, currentPos[3]) if player == 0 \
                else (currentPos[0], nPos, currentPos[2], currentPos[3] + nScore)

            newBoardState.setdefault(nPos, 0)
            newBoardState[nPos] += numberOfUniverses * numberOfMoves

    return newBoardState


def reduceBoardState(boardState, player):
    wins = 0
    scoresToDelete = []
    for score in boardState.keys():
        if score[2 + player] >= 21:
            scoresToDelete.append(score)

    for score in scoresToDelete:
        wins += boardState.pop(score)

    return boardState, wins


def puzzleA(lines):
    pos1 = int(lines[0].strip().split(" ")[-1]) - 1
    pos2 = int(lines[1].strip().split(" ")[-1]) - 1

    die = collections.deque([i + 1 for i in range(100)])
    score = [0, 0]
    pos = [pos1, pos2]
    rolls = 0
    player = 0

    while True:
        pos[player], die = roll(pos[player], die)
        rolls += 3
        score[player] += pos[player] + 1
        if score[player] >= 1000:
            break

        player = 1 if player == 0 else 0

    return rolls * min(score)


def puzzleB(lines):
    pos1 = int(lines[0].strip().split(" ")[-1]) - 1
    pos2 = int(lines[1].strip().split(" ")[-1]) - 1

    die = [1, 2, 3]
    combisPerRoll = getDieCombinations(die)

    # boardState: key = position/score, value = number of universes
    # (posPlayer1, posPlayer2, scorePlayer1, scorePlayer2)
    boardState = {(pos1, pos2, 0, 0): 1}
    win = [0, 0]
    player = 0

    while len(boardState) > 0:
        boardState = quantumRoll(boardState, combisPerRoll, player)
        boardState, wins = reduceBoardState(boardState, player)
        win[player] += wins
        player = 1 if player == 0 else 0

    return max(win)


if __name__ == '__main__':
    day = "21"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 576600
    assert b == 131888061854776
