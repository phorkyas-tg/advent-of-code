from datetime import datetime, timedelta


class Guard:
    MINUTES = 60

    def __init__(self, guardId):
        self.guardId = guardId
        self.dutySchedule = {}

    def AddDayOfDuty(self, day):
        self.dutySchedule[day] = [0] * self.MINUTES

    def ManipulateSequence(self, day, startMinute, value):
        for i in range(startMinute, self.MINUTES):
            self.dutySchedule[day][i] = value

    def AddSleepSequence(self, day, startMinute):
        self.ManipulateSequence(day, startMinute, 1)

    def AddWakeSequence(self, day, startMinute):
        self.ManipulateSequence(day, startMinute, 0)

    def GetGuardIdAsNumber(self):
        return int(self.guardId[1:])

    def CountMinutesAsleep(self):
        mntAsleep = 0
        for schedule in self.dutySchedule.values():
            mntAsleep += sum(schedule)
        return mntAsleep

    def GetMostAsleepOnMinute(self):
        maxMostAsleep = 0
        maxMostAsleepMinute = 0

        for i in range(self.MINUTES):
            asleep = 0
            for ds in self.dutySchedule.values():
                if ds[i] == 1:
                    asleep += 1
            if asleep > maxMostAsleep:
                maxMostAsleep = asleep
                maxMostAsleepMinute = i

        return maxMostAsleepMinute, maxMostAsleep


def ParseGuardRecord(inputString):
    timeString, record = inputString.split("] ", 1)

    time = datetime.strptime(timeString, '[%Y-%m-%d %H:%M')

    if record.startswith("Guard"):
        status = record.split(" ")[1]
    elif record == "wakes up":
        status = "wake"
    else:
        status = "asleep"

    return time, status


def GenerateGuardSchedule(input):
    input.sort()

    guardSchedule = {}
    currentGuard = None

    for record in input:
        time, status = ParseGuardRecord(record)

        hour = time.hour
        minute = time.minute
        # if the guard starts before 00:00, the day mus be increased because the day is the KEY
        # for the dict
        if hour == 23:
            time += timedelta(days=1)
        day = time.strftime("%Y-%m-%d")

        if status == "wake":
            guardSchedule[currentGuard].AddWakeSequence(day, minute)
        elif status == "asleep":
            guardSchedule[currentGuard].AddSleepSequence(day, minute)
        else:
            currentGuard = status
            if currentGuard not in guardSchedule:
                guardSchedule[currentGuard] = Guard(currentGuard)
            guardSchedule[currentGuard].AddDayOfDuty(day)

    return guardSchedule


def CalculateStrategyOne(guardSchedule):
    bestGuard = None
    maxSleepTime = 0

    for gs in guardSchedule.values():
        sleepTime = gs.CountMinutesAsleep()
        if sleepTime > maxSleepTime:
            maxSleepTime = sleepTime
            bestGuard = gs

    maxMostAsleepMinute, maxMostAsleep = bestGuard.GetMostAsleepOnMinute()
    return bestGuard.GetGuardIdAsNumber() * maxMostAsleepMinute


def CalculateStrategyTwo(guardSchedule):
    bestGuard = None
    maxMostAsleep = 0

    for gs in guardSchedule.values():
        maxMostAsleepMinute, mostAsleep = gs.GetMostAsleepOnMinute()
        if mostAsleep > maxMostAsleep:
            maxMostAsleep = mostAsleep
            bestGuard = gs

    maxMostAsleepMinute, maxMostAsleep = bestGuard.GetMostAsleepOnMinute()
    return bestGuard.GetGuardIdAsNumber() * maxMostAsleepMinute

