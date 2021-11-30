import unittest

from AOCBase import AOCTestCases
from aoc2016 import *


class TestAdventOfCode2020(AOCTestCases.TestAdventOfCode):

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
