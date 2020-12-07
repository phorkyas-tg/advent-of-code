import unittest

from AOCBase import AOCTestCases
from aoc2020 import *


class TestAdventOfCode2020(AOCTestCases.TestAdventOfCode):

    def testDayOne(self):
        multEntries = MultiplyTwoEntriesWithSum(d1Input.copy(), 2020)
        print("Day One - Part One: {0}".format(multEntries))
        self.assertEqual(multEntries, 1020084)

        multEntries = MultiplyThreeEntriesWithSum(d1Input.copy(), 2020)
        print("Day One - Part Two: {0}".format(multEntries))
        self.assertEqual(multEntries, 295086480)

    def testDayTwo(self):
        validPasswords = CheckValidPasswords(d2Input.copy())
        print("Day Two - Part One: {0}".format(validPasswords))
        self.assertEqual(validPasswords, 524)

        validPasswords = CheckValidPasswordsAdvanced(d2Input.copy())
        print("Day Two - Part Two: {0}".format(validPasswords))
        self.assertEqual(validPasswords, 485)

    def testDayThree(self):
        countTrees = CountTreesWhileTraversing(d3Test1.copy())
        self.assertEqual(countTrees, 7)

        countTrees = CountTreesWhileTraversing(d3Input.copy())
        print("Day Three - Part One: {0}".format(countTrees))
        self.assertEqual(countTrees, 274)

        countTrees = CountMultipleSlopes(d3Test1.copy())
        self.assertEqual(countTrees, 336)

        countTrees = CountMultipleSlopes(d3Input.copy())
        print("Day Three - Part Two: {0}".format(countTrees))
        self.assertEqual(countTrees, 6050183040)

    def testDayFour(self):
        validPasscodes = CountValidPassports(d4Input.copy())
        print("Day Four - Part One: {0}".format(validPasscodes))
        self.assertEqual(validPasscodes, 222)

        validPasscodes = CountValidPassportsAdvanced(d4Test1.copy())
        self.assertEqual(validPasscodes, 0)

        validPasscodes = CountValidPassportsAdvanced(d4Test2.copy())
        self.assertEqual(validPasscodes, 4)

        validPasscodes = CountValidPassportsAdvanced(d4Input.copy())
        print("Day Four - Part Two: {0}".format(validPasscodes))
        self.assertEqual(validPasscodes, 140)

    def testDayFive(self):
        self.assertEqual((44, 5, 357), GetRowColumnIdFromInputStr("FBFBBFFRLR"))
        self.assertEqual((70, 7, 567), GetRowColumnIdFromInputStr("BFFFBBFRRR"))
        self.assertEqual((14, 7, 119), GetRowColumnIdFromInputStr("FFFBBBFRRR"))
        self.assertEqual((102, 4, 820), GetRowColumnIdFromInputStr("BBFFBBFRLL"))

        seatId = GetHighestSeatId(d5Input.copy())
        print("Day Five - Part One: {0}".format(seatId))
        self.assertEqual(seatId, 842)

        seatId = GetMySeatId(d5Input.copy())
        print("Day Five - Part Two: {0}".format(seatId))
        self.assertEqual(seatId, 617)

    def testDaySix(self):
        count = SumOfDeclarationCounts(d6Test1.copy())
        self.assertEqual(count, 11)

        count = SumOfDeclarationCounts(d6Input.copy())
        print("Day Six - Part One: {0}".format(count))
        self.assertEqual(count, 6416)

        count = SumOfDeclarationCountsAdvanced(d6Test1.copy())
        self.assertEqual(count, 6)

        count = SumOfDeclarationCountsAdvanced(d6Input.copy())
        print("Day Six - Part Two: {0}".format(count))
        self.assertEqual(count, 3050)

    def testDaySeven(self):
        countBag = CountPossibleBags(d7Test1.copy())
        self.assertEqual(countBag, 4)

        countBag = CountPossibleBags(d7Input.copy())
        print("Day Seven - Part One: {0}".format(countBag))
        self.assertEqual(countBag, 265)

        countBag = CountChildrenBags(d7Test1.copy())
        self.assertEqual(countBag, 32)

        countBag = CountChildrenBags(d7Input.copy())
        print("Day Seven - Part Two: {0}".format(countBag))
        self.assertEqual(countBag, 14177)


if __name__ == '__main__':
    unittest.main()

