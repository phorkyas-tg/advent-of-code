import unittest

from AOCBase import AOCTestCases
from aoc2018 import *


class TestAdventOfCode2018(AOCTestCases.TestAdventOfCode):

    def testDayOne(self):
        frequency = CalculateFrequency(d1Input.copy())
        print("Day One - Part One: {0}".format(frequency))
        self.assertEqual(frequency, 599)

        duplicateFrequency = CalculateFrequencyDuplicate(d1Input.copy())
        print("Day One - Part Two: {0}".format(duplicateFrequency))
        self.assertEqual(duplicateFrequency, 81204)

    def testDayTwo(self):
        checksum = CalculateChecksum(d2Input.copy())
        print("Day Two - Part One: {0}".format(checksum))
        self.assertEqual(checksum, 6150)

        commonChars = GetCommonCharsFromIds(d2Input.copy())
        print("Day Two - Part Two: {0}".format(commonChars))
        self.assertEqual(commonChars, "rteotyxzbodglnpkudawhijsc")

    def testDayThree(self):
        multipleClaimedSquares = GetMultipleClaimedSquares(d3Input.copy())
        print("Day Three - Part One: {0}".format(multipleClaimedSquares))
        self.assertEqual(multipleClaimedSquares, 108961)

        ClaimedId = GetIntactClaimId(d3Input.copy())
        print("Day Three - Part Two: {0}".format(ClaimedId))
        self.assertEqual(ClaimedId, 681)

    def testDayFour(self):
        guardSchedule = GenerateGuardSchedule(d4Input.copy())
        st1 = CalculateStrategyOne(guardSchedule)
        print("Day Four - Part One: {0}".format(st1))
        self.assertEqual(st1, 35184)

        st2 = CalculateStrategyTwo(guardSchedule)
        print("Day Four - Part Two: {0}".format(st2))
        self.assertEqual(st2, 37886)

    def testDayFive(self):
        lenAfterReactions = CalculateLenAfterReactions("{:s}".format(d5Input))
        print("Day Five - Part One: {0}".format(lenAfterReactions))
        self.assertEqual(lenAfterReactions, 9526)

        lenAfterImprovement = GetShortestPolymerAfterImprovement("{:s}".format(d5Input))
        print("Day Five - Part Two: {0}".format(lenAfterImprovement))
        self.assertEqual(lenAfterImprovement, 6694)

    def testDaySix(self):
        largestArea = GetLargestFiniteArea(d6Test1.copy())
        self.assertEqual(largestArea, 17)

        largestArea = GetLargestFiniteArea(d6Input.copy())
        print("Day Six - Part One: {0}".format(largestArea))
        self.assertEqual(largestArea, 4290)

        largestArea = GetLargestAreaWithManhattanDistance(d6Test1.copy(), 32)
        self.assertEqual(largestArea, 16)

        largestArea = GetLargestAreaWithManhattanDistance(d6Input.copy(), 10000)
        print("Day Six - Part Two: {0}".format(largestArea))
        self.assertEqual(largestArea, 37318)

    def testDaySeven(self):
        stepDict = GenerateStepDict(d7Input.copy())
        stepExecution = CalculateStepOrder(stepDict)
        print("Day Seven - Part One: {0}".format(stepExecution))
        self.assertEqual(stepExecution, "AHJDBEMNFQUPVXGCTYLWZKSROI")

        seconds = CalculateWorkerTime(stepDict, 5)
        print("Day Seven - Part Two: {0}".format(seconds))
        self.assertEqual(seconds, 1031)

    def testDayFifteen(self):
        battleOutcome = CalculateBattleOutcome(d15test1.copy(), log=False)
        self.assertEqual(battleOutcome, 27730)
        battleOutcome = CalculateBattleOutcome(d15test2.copy(), log=False)
        self.assertEqual(battleOutcome, 36334)
        battleOutcome = CalculateBattleOutcome(d15test3.copy(), log=False)
        self.assertEqual(battleOutcome, 39514)
        battleOutcome = CalculateBattleOutcome(d15test4.copy(), log=False)
        self.assertEqual(battleOutcome, 27755)
        battleOutcome = CalculateBattleOutcome(d15test5.copy(), log=False)
        self.assertEqual(battleOutcome, 28944)
        battleOutcome = CalculateBattleOutcome(d15test6.copy(), log=False)
        self.assertEqual(battleOutcome, 18740)

        battleOutcome = CalculateBattleOutcome(d15Input.copy(), log=False)
        print("Day Fifteen - Part One: {0}".format(battleOutcome))
        self.assertEqual(battleOutcome, 228730)

        battleOutcome = BattleTillElfsWin(d15test1.copy(), log=False)
        self.assertEqual(battleOutcome, 4988)
        battleOutcome = BattleTillElfsWin(d15test2.copy(), log=False)
        self.assertEqual(battleOutcome, 29064)
        battleOutcome = BattleTillElfsWin(d15test3.copy(), log=False)
        self.assertEqual(battleOutcome, 31284)
        battleOutcome = BattleTillElfsWin(d15test4.copy(), log=False)
        self.assertEqual(battleOutcome, 3478)
        battleOutcome = BattleTillElfsWin(d15test5.copy(), log=False)
        self.assertEqual(battleOutcome, 6474)
        battleOutcome = BattleTillElfsWin(d15test6.copy(), log=False)
        self.assertEqual(battleOutcome, 1140)
        battleOutcome = BattleTillElfsWin(d15Input.copy(), log=False)
        print("Day Fifteen - Part Two: {0}".format(battleOutcome))
        self.assertEqual(battleOutcome, 33621)


if __name__ == '__main__':
    unittest.main()

