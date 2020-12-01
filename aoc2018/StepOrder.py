import string


class Step:
    BASE_STEP_TIME = 60

    def __init__(self, name):
        self.name = name
        self.requiredSteps = []
        self.nextSteps = []

        self.stepTime = self.CalculateStepTime()

    def GetName(self):
        return self.name

    def GetStepTime(self):
        return self.stepTime

    def CalculateStepTime(self):
        uc = string.ascii_uppercase
        for i in range(len(uc)):
            if self.name.upper() == uc[i]:
                return self.BASE_STEP_TIME + i + 1

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


class Worker:
    def __init__(self):
        self.currentStep = None
        self.remainingSeconds = 0

    def IsAvailable(self):
        if self.remainingSeconds == 0:
            return True
        return False

    def SetStep(self, step, seconds):
        self.currentStep = step
        self.remainingSeconds = seconds

    def work(self):
        testStepCopy = None if self.currentStep is None else "{:s}".format(self.currentStep)

        if self.remainingSeconds > 0:
            self.remainingSeconds -= 1
        else:
            self.currentStep = None

        return testStepCopy, self.remainingSeconds


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
            if step.GetName() not in executedSteps and step.IsPossibleStep(executedSteps):
                possibleSteps.append(step.GetName())

        if len(possibleSteps) == 0:
            break

        possibleSteps.sort()
        nextStep = possibleSteps[0]
        executedSteps += nextStep

    return executedSteps


def CalculateWorkerTime(stepDict, numberOfWorkers):
    workers = {}
    for i in range(numberOfWorkers):
        workers[i] = Worker()

    seconds = 0
    executedSteps = ""
    currentSteps = ""

    while True:
        possibleSteps = []
        for step in stepDict.values():
            if step.GetName() not in executedSteps \
                    and step.GetName() not in currentSteps \
                    and step.IsPossibleStep(executedSteps):
                possibleSteps.append(step.GetName())

        # termination
        if len(possibleSteps) == 0 and len(currentSteps) == 0:
            break

        # distribute possible steps to available workers
        for ps in possibleSteps:
            for worker in workers.values():
                if worker.IsAvailable():
                    worker.SetStep(stepDict[ps].GetName(), stepDict[ps].GetStepTime())
                    break

        # work
        currentSteps = ""
        for worker in workers.values():
            cs, rs = worker.work()
            if cs is not None:
                if rs == 0:
                    executedSteps += cs
                elif rs > 0:
                    currentSteps += cs

        seconds += 1

    return seconds
