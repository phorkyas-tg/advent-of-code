import uuid

from aocLib.Map import MapObject, Map, MapObjectBuilder


class ElfIsDeadError(Exception):
    """Raised if an elf is dead"""
    pass


class Wall(MapObject):
    def IsSolid(self):
        return True


class Path(MapObject):
    def IsSolid(self):
        return False


class Warrior(MapObject):
    def __init__(self, objectId=None, hp=200, ap=3):
        if objectId is None:
            objectId = uuid.uuid4()
        super(Warrior, self).__init__(objectId)
        self.hp = hp
        self.ap = ap

    def IsSolid(self):
        return True

    def IsAlive(self):
        if self.hp > 0:
            return True
        return False

    def GetHP(self):
        return self.hp

    def GetAP(self):
        return self.ap

    def SetAP(self, ap):
        self.ap = ap

    def Hit(self, ap):
        self.hp -= ap


class Elf(Warrior):
    def GetObjectName(self):
        return "E"


class Goblin(Warrior):
    def GetObjectName(self):
        return "G"


class BattleMapObjectBuilder(MapObjectBuilder):
    @staticmethod
    def GetMapObjectFromChar(char):
        if char == "#":
            return Wall("#")
        elif char == ".":
            return Path(".")
        elif char == "E":
            return Elf()
        elif char == "G":
            return Goblin()


class BattleMap(Map):
    def __init__(self, mapInput, log=False, raiseElfIsDeadError=False):
        super(BattleMap, self).__init__(mapInput, mapObjectBuilderClass=BattleMapObjectBuilder,
                                        log=log)
        self.raiseElfIsDeadError = raiseElfIsDeadError
        self.DeadEndFill(wallId="#", pathId=".")

    def GetBattleOrder(self):
        return self.GetOrderedPositionsOfElementsByNames(["E", "G"]).values()

    def GetAttackTiles(self, warrior):
        attackTile = []
        if self.mapObjects[warrior].GetObjectName() == "E":
            for tile in self.GetOrderedPositionsOfElementsByNames(["G"]).keys():
                attackTile.extend(self.GetAdjacentTiles(tile[0], tile[1], objectNames=[".", "E"]))
        else:
            for tile in self.GetOrderedPositionsOfElementsByNames(["E"]).keys():
                attackTile.extend(self.GetAdjacentTiles(tile[0], tile[1], objectNames=[".", "G"]))

        return attackTile

    def ChangeElfsAp(self, ap):
        for element in self.mapObjects.values():
            if element.GetObjectName() == "E":
                element.SetAP(ap)

    def GetBestMoveFromPossiblePaths(self, possiblePaths):
        bestMove = None
        for i in range(len(possiblePaths)):
            nextMove = possiblePaths[i][1]
            if bestMove is None or self.HasHigherPrio(nextMove, bestMove):
                bestMove = nextMove
        return bestMove

    def HasHigherPrio(self, pos1, pos2):
        if (pos1[1] < pos2[1]) or (pos1[1] == pos2[1] and pos1[0] < pos2[0]):
            return True
        return False

    def MoveWarrior(self, warrior):
        warriorPos = self.GetElementPosition(warrior)
        possibleAttackTiles = self.GetAttackTiles(warrior)

        # There is no enemy left
        if len(possibleAttackTiles) == 0:
            return False

        # warrior is already on a attack position
        if warriorPos in possibleAttackTiles:
            return True

        bestPaths = self.GetShortestPathsToMultipleTiles(warriorPos, possibleAttackTiles)
        if len(bestPaths) == 0:
            return True

        bestMove = self.GetBestMoveFromPossiblePaths(bestPaths)
        # move the warrior to the destination
        self.Move(warriorPos, ".", bestMove, warrior)
        return True

    def GetBestEnemyFromIds(self, enemyIds):
        # Ids need to be in the right priority (highest to lowest)
        bestEnemy = None
        for enemyId in enemyIds:
            if bestEnemy is None or \
                    self.mapObjects[enemyId].GetHP() < self.mapObjects[bestEnemy].GetHP():
                bestEnemy = enemyId
        return bestEnemy

    def Attack(self, warriorId, enemyId):
        self.mapObjects[enemyId].Hit(self.mapObjects[warriorId].GetAP())
        if self.log:
            print("[{0}]({1} AP) HIT [{2}]({3} HP - {4})".format(
                    self.mapObjects[warriorId].GetObjectName(),
                    self.mapObjects[warriorId].GetAP(),
                    self.mapObjects[enemyId].GetObjectName(),
                    self.mapObjects[enemyId].GetHP(),
                    self.GetElementPosition(enemyId)))

    def AttackWarrior(self, warrior):
        warriorPos = self.GetElementPosition(warrior)

        enemyIsElf = False
        if self.mapObjects[warrior].GetObjectName() == "E":
            adjacentTiles = self.GetAdjacentTiles(warriorPos[0], warriorPos[1], objectNames=["G"])
        else:
            adjacentTiles = self.GetAdjacentTiles(warriorPos[0], warriorPos[1], objectNames=["E"])
            enemyIsElf = True

        if len(adjacentTiles) == 0:
            return

        if adjacentTiles == 1:
            enemyId = self.mapDict[adjacentTiles[0]]
        else:
            # adjacend tiles gave back the right prio position (up, left, right down)
            enemyId = self.GetBestEnemyFromIds([self.mapDict[pos] for pos in adjacentTiles])

        self.Attack(warrior, enemyId)
        if not self.mapObjects[enemyId].IsAlive():
            if enemyIsElf and self.raiseElfIsDeadError:
                raise ElfIsDeadError
            enemyPos = self.GetElementPosition(enemyId)
            self.Move(enemyPos, ".")

    def BattleRound(self):
        battleOrder = self.GetBattleOrder()
        for warrior in battleOrder:
            # the warrior is dead now
            if not self.mapObjects[warrior].IsAlive():
                continue
            # phase one: move
            hasEnemy = self.MoveWarrior(warrior)
            # no complete battle round
            if hasEnemy is False:
                return False
            # phase two: attack
            self.AttackWarrior(warrior)

        # complete battle round
        return True

    def Battle(self):
        i = 0
        if self.log:
            print("######## ROUND 0 #########")
            self.PrintMap()

        while True:
            completeRound = self.BattleRound()
            if completeRound:
                i += 1

            aliveElfs = 0
            aliveGoblins = 0
            for element in self.mapObjects.values():
                if element.GetObjectName() == "E" and element.IsAlive():
                    aliveElfs += element.GetHP()
                elif element.GetObjectName() == "G" and element.IsAlive():
                    aliveGoblins += element.GetHP()

            if self.log:
                print("######## ROUND {0} #########".format(i))
                self.PrintMap()

            # termination
            if aliveElfs == 0 or aliveGoblins == 0:
                break

        if self.log:
            print("End after {0} rounds with E {1} HP and G {2} HP".format(i, aliveElfs,
                                                                           aliveGoblins))

        return i * (aliveElfs + aliveGoblins)


def CalculateBattleOutcome(input, log=False):
    battleMap = BattleMap(input, log)
    battleResult = battleMap.Battle()
    return battleResult


def BattleTillElfsWin(input, log=False):
    minVal = 4
    maxVal = 200

    bestResult = 0

    while True:
        i = int((maxVal + minVal) / 2)
        if log:
            print("min-max {0}/{1}: {2}".format(minVal, maxVal, i))
        inputTemp = input.copy()
        battleMap = BattleMap(inputTemp, log=log, raiseElfIsDeadError=True)
        battleMap.ChangeElfsAp(i)
        try:
            battleResult = battleMap.Battle()
        except ElfIsDeadError:
            if maxVal - 1 == i or (maxVal == i and minVal == i):
                return bestResult

            minVal = i
            continue

        bestResult = battleResult

        if maxVal - 1 == i or (maxVal == i and minVal == i):
            return bestResult

        maxVal = i
