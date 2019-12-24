from enum import Enum
import re


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
    def __init__(self, puzzleInput):
        self.rows = len(puzzleInput)
        self.colums = len(puzzleInput[0])

        self.map = self.GenerateMap(puzzleInput)
        self.ReduceMap()

    def ReduceMap(self):
        reduced = True
        while reduced:
            reduced = False
            for row in range(self.rows):
                for col in range(self.colums):
                    tile = self.map[row][col]
                    if tile.GetType() not in (TILETYPE.WALL, TILETYPE.KEY, TILETYPE.ME):
                        neighbourWalls = 0
                        for direction in ["N", "E", "S", "W"]:
                            if self.Go(tile.GetPosition(), direction).GetType() == TILETYPE.WALL:
                                neighbourWalls += 1
                        if neighbourWalls == 3:
                            tile.SetType(TILETYPE.WALL)
                            tile.SetData("#")
                            reduced = True

    def GenerateMap(self, input):
        map = []

        for row in range(self.rows):
            rowList = []
            for col in range(self.colums):
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

        for row in range(self.rows):
            for col in range(self.colums):
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

    def MoveToPosition(self, tilePosition):
        # first make my current position to a path tile
        me = self.GetMyPositionTile()
        me.SetData(".")
        me.SetType(TILETYPE.PATH)
        # if new position is a key - put into inventory
        tile = self.map[tilePosition[0]][tilePosition[1]]
        # now put me on this position
        tile.SetData("@")
        tile.SetType(TILETYPE.ME)

    def PrintMap(self):
        print()
        for row in range(self.rows):
            line = ""
            for col in range(self.colums):
                line += self.map[row][col].GetData()
            print(line)
        print()
        print("Inventory: {0}".format(self.inventory))

    def ExportMap(self):
        mapData = []
        for row in range(self.rows):
            line = ""
            for col in range(self.colums):
                line += self.map[row][col].GetData()
            mapData.append(line)
        return mapData


class MapSolver:
    def __init__(self, puzzleInput):
        self.map = Map(puzzleInput)
        self.keys = self.map.GetTilesByType([TILETYPE.ME, TILETYPE.KEY])
        self.keyNames = set([x.GetData() for x in self.keys])
        self.keyPositions = set([x.GetPosition() for x in self.keys])
        self.keyDistances = self.GetKeyDistances()

        self.bestPath = 1e8

    def GetKeyDistances(self):
        keyDistances = {}
        for key in self.keys:
            keyDistances[key.GetData()] = self.SearchForKeys(key)
        return keyDistances

    def SearchForKeys(self, currentTile, route=None, doors=None, results=None):
        if route is None:
            route = [currentTile.GetPosition()]
        if doors is None:
            doors = []
        if results is None:
            results = {}

        for direction in ["N", "E", "S", "W"]:
            nextStep = self.map.Go(route[-1], direction)

            if nextStep.GetType() != TILETYPE.WALL and nextStep.GetPosition() not in route:
                newRoute = route.copy()
                newRoute.append(nextStep.GetPosition())

                if nextStep.GetType() in(TILETYPE.KEY, TILETYPE.ME):
                    keyTwin = nextStep.GetData()
                    routeLength = len(newRoute) - 1
                    if keyTwin not in results or results[keyTwin][0] > routeLength:
                        results[keyTwin] = [routeLength, newRoute, doors]

                newDoors = doors.copy()
                if nextStep.GetType() == TILETYPE.DOOR:
                    newDoors.append(nextStep.GetData())

                self.SearchForKeys(currentTile, newRoute, newDoors, results)

        return results

    def GetReachableKeys(self, currentTile, collectedKeys):
        reachableKeys = {}
        for key, path in self.keyDistances[currentTile.GetData()].items():
            # if key is already collected
            if key in collectedKeys:
                continue

            # if a uncollected key is on the way
            uncollectedKeys = self.keyNames - set(collectedKeys)
            intersections = set([self.map.map[i[0]][i[1]].GetData() for i in
                                 self.keyPositions.intersection(set(path[1][1:-1]))])
            if uncollectedKeys.intersection(intersections):
                continue

            # if there are doors look if the required keys are available
            isReachable = True
            for door in path[2]:
                if door.lower() not in collectedKeys:
                    isReachable = False
                    break

            if isReachable:
                reachableKeys[key] = path
        return reachableKeys

    def CollectAllKeys(self, currentTile, collectedKeys, steps=0, known=None, result=None):
        if result is None:
            result = {}
        if known is None:
            known = {}

        reachableKeys = self.GetReachableKeys(currentTile, collectedKeys)

        for nextKey, nextPath in reachableKeys.items():
            newCollectedKeys = collectedKeys.copy()

            stepCounter = steps
            stepCounter += nextPath[0]

            if stepCounter >= self.bestPath:
                continue

            sNewCollectedKeys = tuple(sorted(newCollectedKeys) + [nextKey])
            if sNewCollectedKeys in known:
                if known[sNewCollectedKeys] <= stepCounter:
                    continue

            known[sNewCollectedKeys] = stepCounter

            newCollectedKeys.append(nextKey)
            if len(newCollectedKeys) == len(self.keys):
                result[stepCounter] = newCollectedKeys
                self.bestPath = stepCounter
                continue

            nextTilePosition = nextPath[1][-1]
            nextTile = self.map.map[nextTilePosition[0]][nextTilePosition[1]]
            self.CollectAllKeys(nextTile, newCollectedKeys, stepCounter, known, result)

        return result

    def Solve(self):
        self.bestPath = 1e8
        startTile = self.map.GetMyPositionTile()
        self.CollectAllKeys(startTile, [startTile.GetData()])
        return self.bestPath
