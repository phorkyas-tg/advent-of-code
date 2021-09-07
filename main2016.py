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


if __name__ == '__main__':
    unittest.main()
