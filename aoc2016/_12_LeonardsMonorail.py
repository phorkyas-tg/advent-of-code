class ALU:
    def __init__(self, instructions):
        self.register = {}
        self.instructions = []
        self.InitInstructions(instructions)

    def InitInstructions(self, instructions):
        for instruction in instructions:
            commands = instruction.replace("\n", "").split(" ")
            cmd = commands[0]

            if cmd == "cpy":
                cmd = self.Cpy
            elif cmd == "inc":
                cmd = self.Inc
            elif cmd == "dec":
                cmd = self.Dec
            elif cmd == "jnz":
                cmd = self.Jnz
            elif cmd == "tgl":
                cmd = self.Tgl
            else:
                raise NotImplemented

            p1 = commands[1] if commands[1].isalpha() else int(commands[1])
            p2 = commands[2] if len(commands) == 3 else None
            if p2 is not None:
                p2 = p2 if p2.isalpha() else int(p2)

            if isinstance(p1, str):
                self.register.setdefault(p1, 0)
            if isinstance(p2, str):
                self.register.setdefault(p2, 0)

            self.instructions.append({"cmd": cmd, "p1": p1, "p2": p2})

    def SetRegister(self, r, value):
        self.register.setdefault(r, 0)
        self.register[r] = value

    def Run(self):
        i = 0

        while i < len(self.instructions):
            instruction = self.instructions[i]
            command = instruction["cmd"]
            p1 = instruction["p1"]
            p2 = instruction["p2"]
            i += command(p1, p2, i)

        return self.register

    def Cpy(self, p1, p2, i):
        self.register[p2] = self.register.get(p1, p1)
        return 1

    def Inc(self, p1, p2, i):
        return self.Add(p1, 1)

    def Dec(self, p1, p2, i):
        return self.Add(p1, -1)

    def Add(self, p1, a):
        self.register[p1] += a
        return 1

    def Jnz(self, p1, p2, i):
        p2 = self.register.get(p2, p2)

        # optimise (add)
        if p2 == -2:
            instMin1 = self.instructions[i - 1]
            instMin2 = self.instructions[i - 2]
            if instMin1["cmd"] == self.Dec and instMin1["p1"] == p1 and instMin2["cmd"] == self.Inc:
                self.Add(instMin2["p1"], self.register.get(p1, p1))
                self.Cpy(0, p1, None)
                return 1
            elif instMin2["cmd"] == self.Dec and instMin2["p1"] == p1 and instMin1["cmd"] == self.Inc:
                self.Add(instMin1["p1"], self.register.get(p1, p1))
                self.Cpy(0, p1, None)
                return 1

        # optimise (mlt)
        if p2 == -5:
            instMin1 = self.instructions[i - 1]
            instMin2 = self.instructions[i - 2]
            instMin3 = self.instructions[i - 3]
            instMin4 = self.instructions[i - 4]
            instMin5 = self.instructions[i - 5]

            if instMin5["cmd"] == self.Cpy:
                self.Cpy(instMin5["p1"], instMin5["p2"], None)
                self.register[instMin4["p1"]] += self.register[instMin1["p1"]] * self.register[
                    instMin3["p1"]]
                self.Cpy(0, instMin1["p1"], None)
                self.Cpy(0, instMin3["p1"], None)
                return 1

        p1 = self.register.get(p1, p1)
        return p2 if p1 != 0 else 1

    def Tgl(self, p1, p2, i):
        p1 = self.register.get(p1, p1) + i

        try:
            instruction = self.instructions[p1]
        except IndexError:
            return 1

        cmd = instruction.get("cmd", None)
        if cmd == self.Cpy:
            instruction["cmd"] = self.Jnz
        elif cmd == self.Inc:
            instruction["cmd"] = self.Dec
        elif cmd == self.Dec:
            instruction["cmd"] = self.Inc
        elif cmd == self.Jnz:
            instruction["cmd"] = self.Cpy
        elif cmd == self.Tgl:
            instruction["cmd"] = self.Inc

        return 1

def RegisterA(inputFile):
    file1 = open(inputFile, 'r')
    lines = file1.readlines()
    file1.close()

    alu = ALU(lines)
    register = alu.Run()
    return register["a"]


def RegisterAWithInitRegisterC(inputFile):
    file1 = open(inputFile, 'r')
    lines = file1.readlines()
    file1.close()

    alu = ALU(lines)
    alu.SetRegister("c", 1)
    register = alu.Run()
    return register["a"]
