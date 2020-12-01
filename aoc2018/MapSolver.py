import uuid
import time

class MapObject:
    def __init__(self, objectId):
        self.objectId = objectId

    def GetObjectId(self):
        return self.objectId

    def GetObjectName(self):
        return self.objectId

    def IsSolid(self):
        raise NotImplementedError


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

    def Hit(self, ap):
        self.hp -= ap


class Elf(Warrior):
    def GetObjectName(self):
        return "E"


class Goblin(Warrior):
    def GetObjectName(self):
        return "G"


class MapObjectBuilder:
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


class Map:
    def __init__(self, mapInput, mapObjectBuilderClass=MapObjectBuilder, log=False):
        self.mapObjectBuilderClass = mapObjectBuilderClass
        self.log = log
        self.mapDict, self.mapObjects = self.BuildMapFromInput(mapInput)

        self.width = len(mapInput[0])
        self.height = len(mapInput)

    def BuildMapFromInput(self, mapInput):
        mapDict = {}
        mapObjects = {}

        objectIds = []
        for y in range(len(mapInput)):
            for x in range(len(mapInput[y])):
                char = mapInput[y][x]
                mapObject = self.mapObjectBuilderClass.GetMapObjectFromChar(char)
                mapObjectId = mapObject.GetObjectId()
                mapDict[(x, y)] = mapObjectId
                if char not in objectIds:
                    mapObjects[mapObjectId] = mapObject
                    objectIds.append(mapObjectId)

        return mapDict, mapObjects

    def PrintMap(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.mapObjects[self.mapDict[(x, y)]].GetObjectName()
            print(line)

    def GetOrderedPositionsOfElementsByNames(self, names):
        tempDict = {}
        for pos, elementId in self.mapDict.items():
            if self.mapObjects[elementId].GetObjectName() in names:
                tempDict[pos] = elementId
        return tempDict

    def GetUnsolidAdjacentTiles(self, x, y, visitedTiles=[]):
        tiles = []
        # # # # #
        # . 1 . #
        # 2 o 3 #
        # . 4 . #
        # # # # #
        for pos in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
            if pos not in visitedTiles:
                tileId = self.mapDict.get(pos, None)
                if tileId is not None and self.mapObjects[tileId].IsSolid() is False:
                    tiles.append(pos)
        return tiles

    def GetAdjacentTiles(self, x, y, visitedTiles=[], objectNames=[]):
        tiles = []
        # # # # #
        # . 1 . #
        # 2 o 3 #
        # . 4 . #
        # # # # #
        for pos in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
            if pos not in visitedTiles:
                tileId = self.mapDict.get(pos, None)
                if (tileId is not None) and \
                        (len(objectNames) == 0 or
                         self.mapObjects[tileId].GetObjectName() in objectNames):
                    tiles.append(pos)
        return tiles

    def GetElementPosition(self, elemntId):
        for pos, element in self.mapDict.items():
            if element == elemntId:
                return pos

    def Move(self, startPos, startId, destPos=None, destId=None):
        self.mapDict[startPos] = startId
        if destPos is not None:
            self.mapDict[destPos] = destId

        if self.log:
            if destPos is None:
                destPos = startPos
                destId = startId
            print("[{0}] {1} --> {2}".format(self.mapObjects[destId].GetObjectName(),
                                             startPos, destPos))

    def GetShortestPathsToMultipleTiles(self, currentPosition, destinationTiles):
        """
        [recursive]
        goal: From the current position - get the shortest paths to a
        list of possible destinations. The result is at least one path to at least one of the
        possible destinations.

        :param currentPosition: start position (x, y)
        :type currentPosition: set(int, int)
        :param destinationTiles: a list of destination positions wher you want to go
        :type destinationTiles: list(set(int, int))
        :return: list of lists with the shortest possible paths to one or more destinations
        :rtype: list(list(set(int, int)))
        """
        return self.__GetShortestPathsToMultipleTiles([[currentPosition]], destinationTiles)

    def __GetShortestPathsToMultipleTiles(self, visitedPaths, destinationTiles, results=None):
        # Init phase
        if not isinstance(visitedPaths, list):
            visitedPaths = [[visitedPaths]]
        if results is None:
            results = []
        isPossiblePath = False

        visitedPathsTemp = []

        visitedTiles = []
        for visitedPath in visitedPaths:
            visitedTiles.extend(visitedPath)

        # look at all visited paths
        for visitedPath in visitedPaths:
            # the current pos is always the last po of this path
            currentPos = visitedPath[-1]
            # get all possible directions in which you can go
            nextTiles = self.GetUnsolidAdjacentTiles(currentPos[0], currentPos[1], visitedTiles)

            for nextTile in nextTiles:
                # save the new path into the temp. for every direction there will be a new path
                newRoute = visitedPath.copy()
                newRoute.append(nextTile)
                # reduce paths by not appending duplicates and choosing the better path
                if newRoute not in visitedPathsTemp:
                    for i in range(len(visitedPathsTemp)):
                        if visitedPathsTemp[i][-1] == newRoute[-1]:
                            if (newRoute[1][1] < visitedPathsTemp[i][1][1]) or \
                                    (newRoute[1][1] == visitedPathsTemp[i][1][1] and
                                     newRoute[1][0] < visitedPathsTemp[i][1][0]):
                                visitedPathsTemp[i] = newRoute
                            break
                    else:
                        visitedPathsTemp.append(newRoute)
                # termination - at this point there is a path that reaches one destination but
                # there might be another possible path with the same length. This is why all
                # visited paths must be considered
                if nextTile in destinationTiles:
                    isPossiblePath = True
                    results.append(newRoute)

        # termination if there is no possible Path left
        if len(visitedPathsTemp) == 0:
            return []

        # no possible path was found yet than get through the loop again
        elif isPossiblePath is False:
            self.__GetShortestPathsToMultipleTiles(visitedPathsTemp, destinationTiles, results)

        return results


class BattleMap(Map):
    def __init__(self, mapInput, log=False):
        super(BattleMap, self).__init__(mapInput, log=log)

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

    def GetBestMoveFromPossiblePaths(self, possiblePaths):
        bestMove = None
        for i in range(len(possiblePaths)):
            nextMove = possiblePaths[i][1]
            if bestMove is None or \
                    (nextMove[1] < bestMove[1]) or \
                    (nextMove[1] == bestMove[1] and nextMove[0] < bestMove[0]):
                bestMove = nextMove
        return bestMove

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

        if self.mapObjects[warrior].GetObjectName() == "E":
            adjacentTiles = self.GetAdjacentTiles(warriorPos[0], warriorPos[1], objectNames=["G"])
        else:
            adjacentTiles = self.GetAdjacentTiles(warriorPos[0], warriorPos[1], objectNames=["E"])

        if len(adjacentTiles) == 0:
            return

        if adjacentTiles == 1:
            enemyId = self.mapDict[adjacentTiles[0]]
        else:
            # adjacend tiles gave back the right prio position (up, left, right down)
            enemyId = self.GetBestEnemyFromIds([self.mapDict[pos] for pos in adjacentTiles])

        self.Attack(warrior, enemyId)
        if not self.mapObjects[enemyId].IsAlive():
            enemyPos = self.GetElementPosition(enemyId)
            self.Move(enemyPos, ".")

    def BattleRound(self):
        battleOrder = self.GetBattleOrder()
        for warrior in battleOrder:
            # the warrior is dead now
            if not self.mapObjects[warrior].IsAlive():
                continue
            if self.log:
                print("---> [{0}]{1}".format(self.mapObjects[warrior].GetObjectName(),
                                             self.GetElementPosition(warrior)))
                start = time.time()
            # phase one: move
            hasEnemy = self.MoveWarrior(warrior)
            # no complete battle round
            if hasEnemy is False:
                return False
            # phase two: attack
            self.AttackWarrior(warrior)
            if self.log:
                print("calculation time = {0}".format(time.time() - start))

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
    return battleMap.Battle()
