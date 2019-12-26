from aoc2019.AocInput import d12Input


test = [{"x": -8, "y": -10, "z": 0},
        {"x": 5, "y": 5, "z": 10},
        {"x": 2, "y": -7, "z": 3},
        {"x": 9, "y": -8, "z": -3}]

test2 = [{"x": -1, "y": 0, "z": 2},
         {"x": 2, "y": -10, "z": -7},
         {"x": 4, "y": -8, "z": 8},
         {"x": 3, "y": 5, "z": -1}]


class Moon:
    def __init__(self, input):
        self.pos = [{"x": input["x"], "y": input["y"], "z": input["z"]}]
        self.vel = {"x": 0, "y": 0, "z": 0}
        self.energy = [0]
        self.otherMoons = None

    def GetLastPosition(self):
        return self.pos[-1]

    def SetOtherMoons(self, otherMoons):
        self.otherMoons = otherMoons

    def UpdateEnergy(self):
        pot = 0
        kin = 0
        for dimension in ["x", "y", "z"]:
            pot += abs(self.pos[-1][dimension])
            kin += abs(self.vel[dimension])
        self.energy.append(pot * kin)

    def UpdateVelocity(self, step):
        currentPos = self.GetLastPosition()
        for om in self.otherMoons:
            for dimension in ["x", "y", "z"]:
                if om.pos[step][dimension] > currentPos[dimension]:
                    self.vel[dimension] += 1
                elif om.pos[step][dimension] < currentPos[dimension]:
                    self.vel[dimension] -= 1

        newPos = {"x": 0, "y": 0, "z": 0}
        for dimension in ["x", "y", "z"]:
            newPos[dimension] = currentPos[dimension] + self.vel[dimension]
        self.pos.append(newPos)

        self.UpdateEnergy()


def GetTotalEnergy(puzzleInput, steps=1000):
    moons = []
    for input in puzzleInput:
        moons.append(Moon(input))

    for m in range(len(moons)):
        otherMoons = [x for i, x in enumerate(moons) if i != m]
        moons[m].SetOtherMoons(otherMoons)

    for step in range(steps):
        for m in range(len(moons)):
            moons[m].UpdateVelocity(step)

    totalEnergy = 0
    for moon in moons:
        totalEnergy += moon.energy[-1]

    return totalEnergy

if __name__ == '__main__':
    print(GetTotalEnergy(test2, 4686774924))





