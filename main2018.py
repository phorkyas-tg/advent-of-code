import unittest

from AOCBase import TestAdventOfCode
from aoc2018 import *


class TestAdventOfCode2018(TestAdventOfCode):

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


if __name__ == '__main__':
    unittest.main()

