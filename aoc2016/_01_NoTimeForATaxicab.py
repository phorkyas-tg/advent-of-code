def GetDistanceFromStart(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    pos = (0, 0)
    direction = "N"

    helper = {"NL": (0, -1, "W"), "NR": (0, 1, "E"),
              "SL": (0, 1, "E"), "SR": (0, -1, "W"),
              "WL": (1, 0, "S"), "WR": (-1, 0, "N"),
              "EL": (-1, 0, "N"), "ER": (1, 0, "S")}

    for instruction in inputLines[0].strip().split(", "):
        d = instruction[0]
        steps = int(instruction[1:])

        x, y, newDir = helper.get(direction + d)
        direction = newDir

        pos = (pos[0] + (x * steps), pos[1] + (y * steps))

    return abs(pos[0]) + abs(pos[1])


def GetDistanceVisitedTwice(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    pos = (0, 0)
    direction = "N"

    helper = {"NL": (0, -1, "W"), "NR": (0, 1, "E"),
              "SL": (0, 1, "E"), "SR": (0, -1, "W"),
              "WL": (1, 0, "S"), "WR": (-1, 0, "N"),
              "EL": (-1, 0, "N"), "ER": (1, 0, "S")}

    visited = {pos: "#"}

    for instruction in inputLines[0].strip().split(", "):
        d = instruction[0]
        steps = int(instruction[1:])

        x, y, newDir = helper.get(direction + d)
        direction = newDir

        for s in range(1, steps + 1):
            pos = (pos[0] + x, pos[1] + y)
            if pos in visited:
                return abs(pos[0]) + abs(pos[1])
            visited[pos] = "#"

    return None



