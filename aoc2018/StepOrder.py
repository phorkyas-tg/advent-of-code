class Step:
    def __init__(self, name):
        self.name = name
        self.requiredSteps = []
        self.nextSteps = []

    def GetName(self):
        return self.name

    def AddRequiredStep(self, stepName):
        self.requiredSteps.append(stepName)

    def AddNextStep(self, stepName):
        self.nextSteps.append(stepName)

    def IsPossibleStep(self, alreadyExecutedSteps):
        isPossibleStep = True
        for rs in self.requiredSteps:
            if rs not in alreadyExecutedSteps:
                isPossibleStep = False
                break
        return isPossibleStep


def ParseStepInstruction(instruction):
    result = instruction.split(" ")
    return result[1], result[7]


def GenerateStepDict(input):
    stepDict = {}

    for instruction in input:
        parent, child = ParseStepInstruction(instruction)

        if parent not in stepDict:
            stepDict[parent] = Step(parent)
        stepDict[parent].AddNextStep(child)

        if child not in stepDict:
            stepDict[child] = Step(child)
        stepDict[child].AddRequiredStep(parent)

    return stepDict


def CalculateStepOrder(stepDict):
    executedSteps = ""

    while True:
        possibleSteps = []
        for step in stepDict.values():
            if step.GetName() not in executedSteps and \
                    step.IsPossibleStep(executedSteps):
                possibleSteps.append(step.GetName())

        if len(possibleSteps) == 0:
            break

        possibleSteps.sort()
        nextStep = possibleSteps[0]
        executedSteps += nextStep

    return executedSteps
