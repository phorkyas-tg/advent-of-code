import itertools
from collections import deque


def Play(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        if player1[0] > player2[0]:
            player1.rotate(-1)
            player1.appendleft(player2.popleft())
            player1.rotate(-1)
        else:
            player2.rotate(-1)
            player2.appendleft(player1.popleft())
            player2.rotate(-1)
    return player1, player2


def PlayRecursive(player1, player2):
    played = {}
    while len(player1) > 0 and len(player2) > 0:
        # infinite loop stop
        p = "{0}-{1}".format("".join(list(map(str, player1))), "".join(list(map(str, player2))))
        if p in played:
            return player1, deque([])
        played[p] = 1

        currentCard1 = player1[0]
        currentCard2 = player2[0]

        # sub game
        if currentCard1 < len(player1) and currentCard2 < len(player2):
            player1Sub, player2Sub = PlayRecursive(
                    deque(list(itertools.islice(player1, 1, currentCard1 + 1))),
                    deque(list(itertools.islice(player2, 1, currentCard2 + 1))))

            # make sure that the winner of the sub game wins this round
            if len(player1Sub) > 0:
                currentCard2 = 0
            else:
                currentCard1 = 0

        # winner: put the cards at the end of the deck
        if currentCard1 > currentCard2:
            player1.rotate(-1)
            player1.appendleft(player2.popleft())
            player1.rotate(-1)
        else:
            player2.rotate(-1)
            player2.appendleft(player1.popleft())
            player2.rotate(-1)
    return player1, player2


def GetWinningScore(puzzleInput):
    player1, player2 = puzzleInput.split("\n\n")
    player1 = deque(list(map(int, player1.splitlines()[1:])))
    player2 = deque(list(map(int, player2.splitlines()[1:])))

    player1, player2 = Play(player1, player2)
    player1.extend(player2)
    player1.reverse()
    return sum([player1[i] * (i + 1) for i in range(len(player1))])


def GetRecursiveWinningScore(puzzleInput):
    player1, player2 = puzzleInput.split("\n\n")
    player1 = deque(list(map(int, player1.splitlines()[1:])))
    player2 = deque(list(map(int, player2.splitlines()[1:])))

    player1, player2 = PlayRecursive(player1, player2)
    player1.extend(player2)
    player1.reverse()
    return sum([player1[i] * (i + 1) for i in range(len(player1))])
