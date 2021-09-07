class ALU:
    def __init__(self, instructions):
        self.register = {}
        self.instructions = instructions

    def SetRegister(self, r, value):
        self.register.setdefault(r, value)

    def Run(self):
        i = 0
        while i < len(self.instructions):
            commands = self.instructions[i].replace("\n", "").split(" ")
            command = commands[0]
            p1 = commands[1]
            p2 = commands[2] if len(commands) == 3 else None
            i += self.Command(command, p1, p2)

        return self.register

    def Command(self, cmd, p1, p2):
        if p1.isalpha():
            self.register.setdefault(p1, 0)
        if p2 is not None and p2.isalpha():
            self.register.setdefault(p2, 0)

        if cmd == "cpy":
            self.Cpy(p1, p2)
            return 1
        elif cmd == "inc":
            self.Add(p1, 1)
            return 1
        elif cmd == "dec":
            self.Add(p1, -1)
            return 1
        elif cmd == "jnz":
            return self.Jnz(p1, p2)
        else:
            raise NotImplemented

    def Cpy(self, p1, p2):
        if p1.isalpha():
            self.register[p2] = self.register[p1]
        else:
            self.register[p2] = int(p1)

    def Add(self, p1, a):
        self.register[p1] += a

    def Jnz(self, p1, p2):
        if p1.isalpha():
            p1 = self.register[p1]
        if p1 == 0:
            return 1

        if p2.isalpha():
            p2 = self.register[p2]
        return int(p2)


def RegisterA(inputFile):
    file1 = open(inputFile, 'r')
    lines = file1.readlines()

    alu = ALU(lines)
    register = alu.Run()
    return register["a"]


def RegisterAWithInitRegisterC(inputFile):
    file1 = open(inputFile, 'r')
    lines = file1.readlines()

    alu = ALU(lines)
    alu.SetRegister("c", 1)
    register = alu.Run()
    return register["a"]
