import unittest
from aoc2019 import *


class TestAdventOfCode(unittest.TestCase):

    def testDayOne(self):
        sumOfFuelRequirements = GetSumOfFuel(d1Input.copy())
        print("Day One - Part One: {0}".format(sumOfFuelRequirements))
        self.assertEqual(sumOfFuelRequirements, 3423511)

        sumOfFuelRequirements = GetSumOfFuelRecursive(d1Input.copy())
        print("Day One - Part Two: {0}".format(sumOfFuelRequirements))
        self.assertEqual(sumOfFuelRequirements, 5132379)

    def testDayTwo(self):
        intCode = IntCodeComputer(d2Input.copy())[0][0]
        print("Day Two - Part One: {0}".format(intCode))
        self.assertEqual(intCode, 7210630)

        verbNoun = FindVerbNoun(d2Input, d2Output)
        print("Day Two - Part Two: {0}".format(verbNoun))
        self.assertEqual(verbNoun, 3892)

    def testDayThree(self):
        commandList1, commandList2, intersection = ReadIntersections(d3Input_1, d3Input_2)
        manhattanDistance = GetLowestManhattanDistance(intersection)
        print("Day Three - Part One: {0}".format(manhattanDistance))
        self.assertEqual(manhattanDistance, 1337)

        distanceFromStart = GetLowestDistanceFromStart(commandList1, commandList2, intersection)
        print("Day Three - Part Two: {0}".format(distanceFromStart))
        self.assertEqual(distanceFromStart, 65356)

    def testDayFour(self):
        numberOfPasswords2Plus = DigitsBruteForce(d4Input[0], d4Input[1], "{2}")
        print("Day Four - Part One: {0}".format(numberOfPasswords2Plus))
        self.assertEqual(numberOfPasswords2Plus, 2050)

        numberOfPasswords2 = DigitsBruteForce(d4Input[0], d4Input[1], "{2,}")
        print("Day Four - Part Two: {0}".format(numberOfPasswords2))
        self.assertEqual(numberOfPasswords2, 1390)

    def testDayFive(self):
        outputIn1 = IntCodeComputer(d5Input.copy(), 1)[1]
        print("Day Five - Part One: {0}".format(outputIn1))
        self.assertEqual(outputIn1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 16225258])

        outputIn5 = IntCodeComputer(d5Input.copy(), 5)[1]
        print("Day Five - Part Two: {0}".format(outputIn5))
        self.assertEqual(outputIn5, [2808771])

    def testDaySix(self):
        pass


if __name__ == '__main__':
    unittest.main()

