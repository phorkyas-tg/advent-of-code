class MapObject:
    def __init__(self, objectId):
        self.objectId = objectId

    def GetObjectId(self):
        return self.objectId

    def GetObjectName(self):
        return self.objectId

    def IsSolid(self):
        return True


class MapObjectBuilder:
    @staticmethod
    def GetMapObjectFromChar(char):
        return MapObject(char)


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

    def DeadEndFill(self, wallId, pathId):
        while True:
            for pos, elementId in self.mapDict.items():
                if elementId == pathId:
                    adjacentTiles = self.GetAdjacentTiles(pos[0], pos[1], objectNames=[wallId])
                    if len(adjacentTiles) == 3:
                        self.Move(pos, wallId)
                        break
            else:
                break

    def PrintMap(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.mapObjects[self.mapDict[(x, y)]].GetObjectName()
            print(line)

    def PrintMapId(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.mapObjects[self.mapDict[(x, y)]].GetObjectId()
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

    def GetSurroundingTiles(self, x, y, visitedTiles=[], objectNames=[]):
        tiles = []
        # # # # #
        # 1 2 3 #
        # 4 o 5 #
        # 6 7 8 #
        # # # # #
        for pos in [(x-1, y-1), (x, y-1), (x+1, y-1),
                    (x-1, y), (x+1, y),
                    (x-1, y+1), (x, y+1), (x+1, y+1)]:
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

    def IsHigherPrioPath(self, path1, path2):
        return False

    def IsHigherPrioPos(self, pos1, pos2):
        return False

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
        if results is None:
            results = []
        isPossiblePath = False

        visitedPathsTemp = []

        visitedTiles = {}
        for visitedPath in visitedPaths:
            for tile in visitedPath:
                visitedTiles[tile] = None

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
                for i in range(len(visitedPathsTemp)):
                    if visitedPathsTemp[i][-1] == newRoute[-1]:
                        # check if this path has a higher priority - Overwrite this function
                        if self.IsHigherPrioPath(newRoute, visitedPathsTemp[i]):
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

    def GetManhattanDistance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
