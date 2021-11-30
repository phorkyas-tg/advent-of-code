from aoc2016._12_LeonardsMonorail import ALU


def RegisterAWithToggleA(inputFile):
    file1 = open(inputFile, 'r')
    lines = file1.readlines()
    file1.close()

    alu = ALU(lines)
    alu.SetRegister("a", 7)
    register = alu.Run()
    return register["a"]

def RegisterAWithToggleB(inputFile):
    file1 = open(inputFile, 'r')
    lines = file1.readlines()
    file1.close()

    alu = ALU(lines)
    alu.SetRegister("a", 12)
    register = alu.Run()
    return register["a"]
