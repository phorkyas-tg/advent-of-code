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

    def testDayEight(self):
        sumOfMetaData = GetSumOfMetaData(d8Test1.copy())
        self.assertEqual(sumOfMetaData, 138)

        sumOfMetaData = GetSumOfMetaData(d8Input.copy())
        print("Day Eight - Part One: {0}".format(sumOfMetaData))
        self.assertEqual(sumOfMetaData, 38722)

        sumOfMetaData = GetSumOfMetaDataAdvanced(d8Test1.copy())
        self.assertEqual(sumOfMetaData, 66)

        sumOfMetaData = GetSumOfMetaDataAdvanced(d8Input.copy())
        print("Day Eight - Part Two: {0}".format(sumOfMetaData))
        self.assertEqual(sumOfMetaData, 13935)

    def testDayNine(self):
        from aocLib.Array import JumpIndexRollingBuffer
        self.assertEqual(JumpIndexRollingBuffer(1, 2, 6), 3)
        self.assertEqual(JumpIndexRollingBuffer(1, 3, 6), 4)
        self.assertEqual(JumpIndexRollingBuffer(1, 4, 6), 5)
        self.assertEqual(JumpIndexRollingBuffer(5, 2, 6), 1)
        self.assertEqual(JumpIndexRollingBuffer(5, 3, 6), 2)
        self.assertEqual(JumpIndexRollingBuffer(5, 4, 6), 3)

        self.assertEqual(JumpIndexRollingBuffer(1, -2, 6), 5)
        self.assertEqual(JumpIndexRollingBuffer(1, -3, 6), 4)
        self.assertEqual(JumpIndexRollingBuffer(1, -4, 6), 3)
        self.assertEqual(JumpIndexRollingBuffer(5, -2, 6), 3)
        self.assertEqual(JumpIndexRollingBuffer(5, -3, 6), 2)
        self.assertEqual(JumpIndexRollingBuffer(5, -4, 6), 1)

        self.assertEqual(GetBestScore([9, 25]), 32)
        self.assertEqual(GetBestScore([10, 1618]), 8317)
        self.assertEqual(GetBestScore([13, 7999]), 146373)
        self.assertEqual(GetBestScore([17, 1104]), 2764)
        self.assertEqual(GetBestScore([21, 6111]), 54718)
        self.assertEqual(GetBestScore([30, 5807]), 37305)

        bestScore = GetBestScoreFast(d9Input.copy())
        print("Day Nine - Part One: {0}".format(bestScore))
        self.assertEqual(bestScore, 375465)

        self.assertEqual(GetBestScoreFast([9, 25]), 32)
        self.assertEqual(GetBestScoreFast([10, 1618]), 8317)
        self.assertEqual(GetBestScoreFast([13, 7999]), 146373)
        self.assertEqual(GetBestScoreFast([17, 1104]), 2764)
        self.assertEqual(GetBestScoreFast([21, 6111]), 54718)
        self.assertEqual(GetBestScoreFast([30, 5807]), 37305)

        times100 = d9Input.copy()
        times100[1] = times100[1] * 100
        bestScore = GetBestScoreFast(times100)
        print("Day Nine - Part Two: {0}".format(bestScore))
        self.assertEqual(bestScore, 3037741441)

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

