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

    def testDayEight(self):
        acc = GetLastAcc(d8Test1.copy())
        self.assertEqual(acc, 5)

        acc = GetLastAcc(d8Input.copy())
        print("Day Eight - Part One: {0}".format(acc))
        self.assertEqual(acc, 1744)

        acc = GetLastAccAfterTermination(d8Test1.copy())
        self.assertEqual(acc, 8)

        acc = GetLastAccAfterTermination(d8Input.copy())
        print("Day Eight - Part Two: {0}".format(acc))
        self.assertEqual(acc, 1174)

    def testDayNine(self):
        wn = GetFirstWrongNumber(d9Test1.copy(), 5)
        self.assertEqual(wn, 127)

        wn = GetFirstWrongNumber(d9Input.copy(), 25)
        print("Day Nine - Part One: {0}".format(wn))
        self.assertEqual(wn, 57195069)

        cn = GetContiguousNumber(d9Test1.copy(), 127)
        self.assertEqual(cn, 62)

        cn = GetContiguousNumber(d9Input.copy(), 57195069)
        print("Day Nine - Part Two: {0}".format(cn))
        self.assertEqual(cn, 7409241)

    def testDayTen(self):
        result = CountJolts(d10Test1.copy())
        self.assertEqual(result, 35)
        result = CountJolts(d10Test2.copy())
        self.assertEqual(result, 220)

        result = CountJolts(d10Input.copy())
        print("Day Ten - Part One: {0}".format(result))
        self.assertEqual(result, 2080)

        self.assertEqual(len(GetCombinations([1, 2, 3, 4])), 4)
        self.assertEqual(len(GetCombinations([1, 2, 3, 4, 5])), 7)
        self.assertEqual(len(GetCombinations([1, 2, 3, 4, 5, 6])), 13)
        self.assertEqual(len(GetCombinations([1, 2, 3, 4, 5, 6, 7])), 24)
        self.assertEqual(len(GetCombinations([1, 3, 5])), 1)
        self.assertEqual(len(GetCombinations([1, 2, 4, 5])), 3)

        result = CountPossibleArrangements(d10Test1.copy())
        self.assertEqual(result, 8)
        result = CountPossibleArrangements(d10Test2.copy())
        self.assertEqual(result, 19208)

        result = CountPossibleArrangements(d10Input.copy())
        print("Day Ten - Part Two: {0}".format(result))
        self.assertEqual(result, 6908379398144)


if __name__ == '__main__':
    unittest.main()

