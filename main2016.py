import unittest

from AOCBase import AOCTestCases
from aoc2016 import *


class TestAdventOfCode2020(AOCTestCases.TestAdventOfCode):

    def testDayOne(self):
        result = GetDistanceFromStart("aoc2016/input/input_01.txt")
        self.assertEqual(result, 279)

        result = GetDistanceVisitedTwice("aoc2016/input/input_01.txt")
        self.assertEqual(result, 163)

    def testDayTwo(self):
        result = GetKeyCode("aoc2016/input/input_02.txt")
        self.assertEqual(result, 69642)

        result = GetAdvancedKeyCode("aoc2016/input/input_02.txt")
        self.assertEqual(result, "8CB23")

    def testDayThree(self):
        result = GetValidTriangles("aoc2016/input/input_03.txt")
        self.assertEqual(result, 993)

        result = GetValidVerticalTriangles("aoc2016/input/input_03.txt")
        self.assertEqual(result, 1849)

    def testDayFour(self):
        result = SumValidRoomIds("aoc2016/input/input_04.txt")
        self.assertEqual(result, 245102)

        result = ShiftCypher("aoc2016/input/input_04.txt")
        self.assertEqual(result, 324)

    def testDayTwelve(self):
        result = RegisterA("aoc2016/input/input_12_test.txt")
        self.assertEqual(result, 42)

        result = RegisterA("aoc2016/input/input_12.txt")
        self.assertEqual(result, 318009)

        result = RegisterAWithInitRegisterC("aoc2016/input/input_12.txt")
        self.assertEqual(result, 9227663)

    def testDayTwentyThree(self):
        result = RegisterAWithToggleA("aoc2016/input/input_23_test.txt")
        self.assertEqual(result, 3)

        result = RegisterAWithToggleA("aoc2016/input/input_23.txt")
        self.assertEqual(result, 14160)

        result = RegisterAWithToggleB("aoc2016/input/input_23.txt")
        self.assertEqual(result, 479010720)


if __name__ == '__main__':
    unittest.main()
