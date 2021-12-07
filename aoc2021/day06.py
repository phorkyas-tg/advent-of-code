import math


def getBreedCount(firstDay, days):
    # Number of fish this fish is gonna breed till the end
    return math.floor((days - firstDay) / 7) + 1


def countFishRecursive(firstDay, days, cacheDict):
    count = 0
    breeds = getBreedCount(firstDay, days)
    count += breeds

    # loop over all child fish
    for i in range(breeds):
        # get the first day this child is gonna breed
        newFirstDay = firstDay + (i * 7) + 9

        if newFirstDay <= days:
            # search in cache for this start day
            if newFirstDay in cacheDict:
                count += cacheDict[newFirstDay]
            else:
                # call recursive function with new first day
                newCount = countFishRecursive(newFirstDay, days, cacheDict)
                cacheDict[newFirstDay] = newCount
                count += newCount
        else:
            break

    return count


def countFish(fish, days=256):
    # initial count day 0
    count = len(fish)
    cacheDict = {}
    for f in fish:
        firstDay = f + 1
        count += countFishRecursive(firstDay, days, cacheDict)
    return count


def puzzleA(lines):
    fish = [int(i) for i in lines[0].strip().split(",")]
    return countFish(fish, 80)


def puzzleB(lines):
    fish = [int(i) for i in lines[0].strip().split(",")]
    return countFish(fish, 256)


if __name__ == '__main__':
    day = "06"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 395627
    assert b == 1767323539209
