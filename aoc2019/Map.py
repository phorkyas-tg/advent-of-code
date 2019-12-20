from enum import Enum
import re
import itertools
from aoc2019.AocInput import d18Input


class TILETYPE(Enum):
    UNKNOWN = 0
    WALL = 1
    PATH = 2
    KEY = 3
    DOOR = 4

    ME = 100


class Tile:
    def __init__(self, position=None, type=TILETYPE.UNKNOWN, data=None):
        self.position = position
        self.type = type
        self.data = data

    def GetPosition(self):
        return self.position

    def SetPosition(self, position):
        self.position = position

    def GetType(self):
        return self.type

    def SetType(self, type):
        self.type = type

    def GetData(self):
        return self.data

    def SetData(self, data):
        self.data = data


class Map:
    def __init__(self, puzzleInput, inventory=[]):
        self.map = self.GenerateMap(puzzleInput)
        self.inventory = inventory

    def GetInventory(self):
        return self.inventory

    def GenerateMap(self, input):
        map = []
        for row in range(len(input)):
            rowList = []
            for col in range(len(input[row])):
                char = input[row][col]

                if char == "#":
                    rowList.append(Tile((row, col), TILETYPE.WALL, char))
                elif char == ".":
                    rowList.append(Tile((row, col), TILETYPE.PATH, char))
                elif re.findall("[a-z]", char):
                    rowList.append(Tile((row, col), TILETYPE.KEY, char))
                elif re.findall("[A-Z]", char):
                    rowList.append(Tile((row, col), TILETYPE.DOOR, char))
                elif char == "@":
                    rowList.append(Tile((row, col), TILETYPE.ME, char))
                else:
                    rowList.append(Tile((row, col), TILETYPE.UNKNOWN, char))

            map.append(rowList)
        return map

    def GetTilesByType(self, listOfTileType=None):
        tiles = []

        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if listOfTileType is None or self.map[row][col].GetType() in listOfTileType:
                    tiles.append(self.map[row][col])
        return tiles

    def GetMyPositionTile(self):
        me = self.GetTilesByType([TILETYPE.ME])
        if len(me) == 1:
            return me[0]
        raise IndexError

    def Go(self, position, direction):
        row = position[0]
        col = position[1]

        try:
            if direction == "N":
                return self.map[row-1][col]
            elif direction == "E":
                return self.map[row][col+1]
            elif direction == "S":
                return self.map[row+1][col]
            elif direction == "W":
                return self.map[row][col-1]
        except IndexError:
            return None

        raise KeyError

    def CanOpenDoor(self, doorTile):
        if doorTile.GetData().lower() in self.inventory:
            return True
        return False

    def GetRoutesToTile(self, route, tilePosition):
        results = []

        for direction in ["N", "E", "S", "W"]:
            nextStep = self.Go(route[-1], direction)
            if nextStep.GetType() not in (TILETYPE.WALL, TILETYPE.UNKNOWN) and \
                    nextStep.GetPosition() not in route:

                newRoute = route.copy()
                newRoute.append(nextStep.GetPosition())

                if nextStep.GetPosition() == tilePosition:
                    results.append(newRoute)
                    return results

                closedDoor = nextStep.GetType() == TILETYPE.DOOR and not self.CanOpenDoor(nextStep)
                isKey = nextStep.GetType() == TILETYPE.KEY

                if not closedDoor and not isKey:
                    results += self.GetRoutesToTile(newRoute, tilePosition)

        return results

    def GetFastestRouteToTile(self, tile):
        me = self.GetMyPositionTile()
        route = [me.GetPosition()]

        fastestRoute = []
        for r in self.GetRoutesToTile(route, tile.GetPosition()):
            if fastestRoute == [] or len(fastestRoute) > len(r):
                fastestRoute = r
        return fastestRoute

    def MoveToPosition(self, tilePosition):
        # first make my current position to a path tile
        me = self.GetMyPositionTile()
        me.SetData(".")
        me.SetType(TILETYPE.PATH)
        # if new position is a key - put into inventory
        tile = self.map[tilePosition[0]][tilePosition[1]]
        if tile.GetType() == TILETYPE.KEY:
            self.inventory.append(tile.GetData())
        # now put me on this position
        tile.SetData("@")
        tile.SetType(TILETYPE.ME)

    def PrintMap(self):
        print()
        for row in range(len(self.map)):
            line = ""
            for col in range(len(self.map[row])):
                line += self.map[row][col].GetData()
            print(line)
        print()
        print("Inventory: {0}".format(self.inventory))

    def ExportMap(self):
        mapData = []
        for row in range(len(self.map)):
            line = ""
            for col in range(len(self.map[row])):
                line += self.map[row][col].GetData()
            mapData.append(line)
        return mapData


def GetPossiblePaths(puzzleInput, path="", inventory=[], routes=[]):
    results = []

    map = Map(puzzleInput.copy(), inventory)
    keys = map.GetTilesByType([TILETYPE.KEY])
    exportData = map.ExportMap()

    if not keys:
        pathLength = 0
        for r in routes:
            pathLength += len(r) - 1
        results.append([path, pathLength, routes])
        return results

    for key in keys:
        route = map.GetFastestRouteToTile(key)
        if route:
            newRoutes = routes.copy()
            newRoutes.append(route.copy())
            newMap = Map(exportData, map.GetInventory().copy())
            newMap.MoveToPosition(key.GetPosition())

            results += GetPossiblePaths(newMap.ExportMap(),
                                        path+key.GetData(),
                                        newMap.GetInventory().copy(),
                                        newRoutes)

    return results


def GetFastestPath(puzzleInput):
    possiblePaths = GetPossiblePaths(puzzleInput)

    fastestPath = None
    for path in possiblePaths:
        if fastestPath is None or fastestPath[1] > path[1]:
            fastestPath = path
    return fastestPath


if __name__ == '__main__':
    test = [
        "########################",
        "#@..............ac.GI.b#",
        "###d#e#f################",
        "###A#B#C################",
        "###g#h#i################",
        "########################"]

    test2 = [
        "#########",
        "#b.A.@.a#",
        "#########"]

    print(GetFastestPath(d18Input))


