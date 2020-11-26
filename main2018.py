import unittest
from aoc2018 import *


class TestAdventOfCode2018(unittest.TestCase):

    def testDayOne(self):
        frequency = CalculateFrequency(d1Input.copy())
        print("Day One - Part One: {0}".format(frequency))
        self.assertEqual(frequency, 599)

        duplicateFrequency = CalculateFrequencyDuplicate(d1Input.copy())
        print("Day One - Part Two: {0}".format(duplicateFrequency))
        self.assertEqual(duplicateFrequency, 81204)

    def testDayTwo(self):
        self.skipTest("Not implemented")

    def testDayThree(self):
        self.skipTest("Not implemented")

    def testDayFour(self):
        self.skipTest("Not implemented")

    def testDayFive(self):
        self.skipTest("Not implemented")

    def testDaySix(self):
        self.skipTest("Not implemented")

    def testDaySeven(self):
        self.skipTest("Not implemented")

    def testDayEight(self):
        self.skipTest("Not implemented")

    def testDayNine(self):
        self.skipTest("Not implemented")

    def testDayTen(self):
        self.skipTest("Not implemented")

    def testDayEleven(self):
        self.skipTest("Not implemented")

    def testDayTvelve(self):
        self.skipTest("Not implemented")

    def testDayThirteen(self):
        self.skipTest("Not implemented")

    def testDayFourteen(self):
        self.skipTest("Not implemented")

    def testDayFifteen(self):
        self.skipTest("Not implemented")

    def testDaySixteen(self):
        self.skipTest("Not implemented")

    def testDaySeventeen(self):
        self.skipTest("Not implemented")

    def testDayEighteen(self):
        self.skipTest("Not implemented")

    def testDayNineteen(self):
        self.skipTest("Not implemented")

    def testDayTwenty(self):
        self.skipTest("Not implemented")

    def testDayTwentyone(self):
        self.skipTest("Not implemented")

    def testDayTwentyTwo(self):
        self.skipTest("Not implemented")

    def testDayTwentthree(self):
        self.skipTest("Not implemented")

    def testDayTwentyfour(self):
        self.skipTest("Not implemented")


if __name__ == '__main__':
    unittest.main()

