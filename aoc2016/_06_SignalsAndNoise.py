from collections import Counter


def GetErrorCorrectedCode(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    columns = [""] * (len(inputLines[0]) - 1)

    for line in inputLines:
        for i, char in enumerate(line.strip()):
            columns[i] += char

    code = ""
    for col in columns:
        code += Counter(col).most_common(None)[0][0]
    return code


def GetErrorCorrectedCodeLeastCommon(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    columns = [""] * (len(inputLines[0]) - 1)

    for line in inputLines:
        for i, char in enumerate(line.strip()):
            columns[i] += char

    code = ""
    for col in columns:
        code += Counter(col).most_common(None)[-1][0]
    return code

