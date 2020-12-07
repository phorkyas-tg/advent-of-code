class Bag:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = {}


def GetBagsFromInput(puzzleInput):
    result = {}
    for bagDescription in puzzleInput:
        bags = bagDescription.split(" ")
        # name
        name = bags[0] + " " + bags[1]

        if name not in result:
            result[name] = Bag(name)

        bags = bagDescription.split("contain")[1].split(",")

        # children:
        for i in range(len(bags)):
            temp = bags[i].split(" ")
            number = temp[1]
            if number == "no":
                break
            number = int(number)
            childName = temp[2] + " " + temp[3]

            if childName not in result:
                result[childName] = Bag(childName)
            result[childName].parents.append(name)

            result[name].children[childName] = number

    return result


def CountBags(bagDict, currentBag, possibleNames=[]):
    for parent in bagDict[currentBag].parents:
        if parent not in possibleNames:
            possibleNames.append(parent)
            possibleNames = CountBags(bagDict, parent, possibleNames)
    return possibleNames


def CountChildBags(bagDict, currentBag, count=1):
    tempCount = count
    for child, cnt in bagDict[currentBag].children.items():
        count += tempCount * CountChildBags(bagDict, child, cnt)
    return count


def CountPossibleBags(puzzleInput):
    result = GetBagsFromInput(puzzleInput)
    possibleNames = []
    possibleNames = CountBags(result, "shiny gold", possibleNames=possibleNames)
    return len(possibleNames)


def CountChildrenBags(puzzleInput):
    result = GetBagsFromInput(puzzleInput)
    count = 1
    count = CountChildBags(result, "shiny gold", count=count)
    return count-1


