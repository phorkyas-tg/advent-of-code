import math


def CalculateFuelRequirement(mass):
    return math.floor(mass / 3) - 2


def CalculateFuelRequirementRecursive(mass):
    rest = CalculateFuelRequirement(mass)
    if rest > 0:
        return rest + CalculateFuelRequirementRecursive(rest)
    else:
        return 0


# Part One
def GetSumOfFuel(input):
    sumOfFuelRequirement = 0
    for i in input:
        sumOfFuelRequirement += CalculateFuelRequirement(i)
    return sumOfFuelRequirement


# Part Two
def GetSumOfFuelRecursive(input):
    sumOfFuelRequirement = 0
    for i in input:
        fuelmass = CalculateFuelRequirement(i)
        sumOfFuelRequirement += fuelmass + CalculateFuelRequirementRecursive(fuelmass)
    return sumOfFuelRequirement
