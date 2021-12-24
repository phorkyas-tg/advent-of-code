def GetKeyCode(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    keyPad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    pos = (1, 1)
    helper = {"U": (0, -1),
              "D": (0, 1),
              "L": (-1, 0),
              "R": (1, 0)}

    code = ""
    for line in inputLines:
        for char in line.strip():
            x, y = helper.get(char)

            newX = pos[0] + x
            newY = pos[1] + y
            pos = (newX if 0 <= newX <= 2 else pos[0],
                   newY if 0 <= newY <= 2 else pos[1])

        code += str(keyPad[pos[1]][pos[0]])

    return int(code)


def GetAdvancedKeyCode(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    keyPad = [["#", "#", "1", "#", "#"],
              ["#", "2", "3", "4", "#"],
              ["5", "6", "7", "8", "9"],
              ["#", "A", "B", "C", "#"],
              ["#", "#", "D", "#", "#"]]

    invalidPositions = [(0, 0), (1, 0), (3, 0), (4, 0),
                        (0, 1), (4, 1),
                        (0, 3), (4, 3),
                        (0, 4), (1, 4), (3, 4), (4, 4)]

    pos = (0, 2)
    helper = {"U": (0, -1),
              "D": (0, 1),
              "L": (-1, 0),
              "R": (1, 0)}

    code = ""
    for line in inputLines:
        for char in line.strip():
            x, y = helper.get(char)

            newX = pos[0] + x
            newY = pos[1] + y
            newPos = (newX if 0 <= newX <= 4 else pos[0],
                      newY if 0 <= newY <= 4 else pos[1])

            if newPos not in invalidPositions:
                pos = newPos

        code += str(keyPad[pos[1]][pos[0]])

    return code

