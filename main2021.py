from aoc2021 import (day01, day02, day03, day04, day05, day06, day07, day08, day09, day10, day11,
                     day12)

if __name__ == '__main__':

    print("results for aoc 2021")
    print("")

    for i in range(24):
        day = "0" + str(i + 1) if i < 9 else str(i + 1)

        try:
            file = open("aoc2021\\input\\input_{0}.txt".format(day), 'r')
        except FileNotFoundError:
            print("Day {0} is not available.".format(day))
            break

        inputLines = file.readlines()
        file.close()

        a = b = None
        exec("a = day{0}.puzzleA(inputLines)".format(day))
        exec("b = day{0}.puzzleB(inputLines)".format(day))

        print("Day {0} - Puzzle A: {1}".format(day, a))
        print("Day {0} - Puzzle B: {1}".format(day, b))
        print("")
