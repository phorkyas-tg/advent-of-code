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


if __name__ == '__main__':
    unittest.main()

