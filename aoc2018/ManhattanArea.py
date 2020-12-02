import string

from aocLib.Map import MapObject, Map, MapObjectBuilder


class Wall(MapObject):
    def IsSolid(self):
        return True


class Space(MapObject):
    def IsSolid(self):
        return False


class Shared(MapObject):
    def IsSolid(self):
        return True


class Interferance(MapObject):
    def __init__(self, objectId, centerPos=None):
        super(Interferance, self).__init__(objectId)
        self.centerPos = centerPos
        self.isInfinite = False

    def IsSolid(self):
        return True

    def SetInfinite(self, inifinite):
        self.isInfinite = inifinite

    def GetInfinite(self):
        return self.isInfinite

    def SetCenterPos(self, centerPos):
        self.centerPos = centerPos

    def GetCenterPos(self):
        return self.centerPos

    def GetObjectName(self):
        return "I"


class InterferanceMapObjectBuilder(MapObjectBuilder):
    @staticmethod
    def GetMapObjectFromChar(char):
        if char == "#":
            return Wall("#")
        elif char == ".":
            return Space(".")
        return Interferance(char)


class InterferanceMap(Map):
    def __init__(self, coordinates):
        mapInput = self.GetMapInputFromCoordinates(coordinates)
        super(InterferanceMap, self).__init__(mapInput,
                                              mapObjectBuilderClass=InterferanceMapObjectBuilder)

        self.mapObjects["*"] = Interferance("*")

    def GetMapInputFromCoordinates(self, coordinates):
        xMin = min([coordinate[0] for coordinate in coordinates]) - 1
        xMax = max([coordinate[0] for coordinate in coordinates]) + 1
        yMin = min([coordinate[1] for coordinate in coordinates]) - 1
        yMax = max([coordinate[1] for coordinate in coordinates]) + 1

        mapInput = []
        i = 0
        uc = string.ascii_uppercase + string.ascii_lowercase
        for y in range(yMin, yMax+1):
            line = ""
            for x in range(xMin, xMax+1):
                if x == xMax or x == xMin or y == yMin or y == yMax:
                    line += "#"
                elif (x, y) in coordinates:
                    line += uc[i]
                    i += 1
                else:
                    line += "."
            mapInput.append(line)
        return mapInput

    def Step(self, lastTiles, visitedTiles={}):
        newTiles = {}
        for pos in lastTiles:
            currentTileId = self.mapDict[pos]
            adjacentTiles = self.GetAdjacentTiles(pos[0], pos[1], visitedTiles=visitedTiles,
                                                  objectNames=[".", "#"])
            for tile in adjacentTiles:
                tileId = self.mapDict[tile]
                if self.mapObjects[tileId].GetObjectName() == "#":
                    self.mapObjects[currentTileId].SetInfinite(True)
                else:
                    if tile in newTiles and newTiles[tile] != currentTileId:
                        newTiles[tile] = "*"
                    else:
                        newTiles[tile] = currentTileId

        nextTiles = []
        for tile, tileId in newTiles.items():
            visitedTiles[tile] = tileId
            nextTiles.append(tile)
            self.Move(tile, tileId)

        return nextTiles

    def RunSteps(self):
        nextTiles = []
        visitiedTiles = {}
        for pos, elementID in self.mapDict.items():
            if self.mapObjects[elementID].GetObjectName() == "I":
                nextTiles.append(pos)
                visitiedTiles[pos] = elementID

        while len(nextTiles) > 0:
            nextTiles = self.Step(nextTiles, visitiedTiles)

        result = {}
        for mapId in self.mapDict.values():
            mapObj = self.mapObjects[mapId]
            if mapObj.GetObjectName() == "I" and \
                    mapObj.GetObjectId() != "*" and \
                    not mapObj.GetInfinite():
                if mapId not in result:
                    result[mapId] = 1
                else:
                    result[mapId] += 1

        return max(result.values())


def GetLargestFiniteArea(coordinates):
    iMap = InterferanceMap(coordinates)
    return iMap.RunSteps()

