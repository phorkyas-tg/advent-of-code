import uuid
from aocLib.Map import MapObject, Map, MapObjectBuilder


class Seat(MapObject):
    def __init__(self, objectId=None):
        if objectId is None:
            objectId = uuid.uuid4()
        super(Seat, self).__init__(objectId)
        self.isSolid = False

    def IsSolid(self):
        return self.isSolid

    def SwitchSolid(self):
        if self.isSolid is True:
            self.isSolid = False
        else:
            self.isSolid = True

    def GetObjectName(self):
        if self.isSolid is True:
            return "#"
        return "L"


class Path(MapObject):
    def IsSolid(self):
        return False


class SeatMapObjectBuilder(MapObjectBuilder):
    @staticmethod
    def GetMapObjectFromChar(char):
        if char == "L":
            return Seat()
        elif char == ".":
            return Path(".")


class SeatMap(Map):
    def __init__(self, mapInput, log=False):
        super(SeatMap, self).__init__(mapInput, mapObjectBuilderClass=SeatMapObjectBuilder,
                                      log=log)

    def GetSeatsThatChanges(self):
        changingSeats = []
        for pos, seatId in self.mapDict.items():
            if seatId == ".":
                continue

            self.CountSurroundingTiles(pos[0], pos[1], objectNames=["#"])

            currentSeatStatus = self.mapObjects[seatId].GetObjectName()
            if currentSeatStatus == "L":
                if self.CountSurroundingTiles(pos[0], pos[1], objectNames=["#"],
                                              termination=1) == 0:
                    changingSeats.append(seatId)
            elif currentSeatStatus == "#":
                if self.CountSurroundingTiles(pos[0], pos[1], objectNames=["#"],
                                              termination=5) >= 4:
                    changingSeats.append(seatId)
        return changingSeats

    def GetSeatsThatChangesBySight(self):
        changingSeats = []
        for pos, seatId in self.mapDict.items():
            if seatId == ".":
                continue

            currentSeatStatus = self.mapObjects[seatId].GetObjectName()

            tiles = self.GetTilesInSight(pos[0], pos[1], objectNames=["#", "L"])

            occopiedTiles = 0
            for tilePos, tileId in tiles:
                if self.mapObjects[tileId].GetObjectName() == "#":
                    occopiedTiles += 1

            if currentSeatStatus == "L" and occopiedTiles == 0:
                changingSeats.append(seatId)
            elif currentSeatStatus == "#" and occopiedTiles >= 5:
                changingSeats.append(seatId)
        return changingSeats

    def ChangeSeats(self, seatIds):
        for seatId in seatIds:
            self.mapObjects[seatId].SwitchSolid()

    def GetOccupiedSeatsAfterRounds(self, changedSeatsMethod):
        rounds = 0
        sumOfChangedSeats = 0

        while True:
            seatIds = changedSeatsMethod()

            if len(seatIds) == 0:
                break

            self.ChangeSeats(seatIds)
            rounds += 1
            sumOfChangedSeats += len(seatIds)

        if self.log:
            print("Rounds: {0}\tSum of ChangedSeats: {1}\tMap Size: {2}*{3}".
                  format(rounds, sumOfChangedSeats, self.width, self.height))

        occupiedSeats = 0
        for mapObj in self.mapObjects.values():
            if mapObj.GetObjectName() == "#":
                occupiedSeats += 1
        return occupiedSeats


def GetOccupiedSeats(puzzleInput):
    sMap = SeatMap(puzzleInput)
    return sMap.GetOccupiedSeatsAfterRounds(sMap.GetSeatsThatChanges)


def GetOccupiedSeatsBySide(puzzleInput):
    sMap = SeatMap(puzzleInput)
    return sMap.GetOccupiedSeatsAfterRounds(sMap.GetSeatsThatChangesBySight)
