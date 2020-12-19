import re


def GetRule(rule, rulesDict, skipChars=[]):
    while True:
        for char in rule.split():
            if char in skipChars:
                continue
            if char.isdigit():
                rule = rule.replace(" {0} ".format(char), " ( {0} ) ".format(rulesDict[char]))
                break
        else:
            break
    return rule


def GetCorrectMessages(messages, rule):
    correctMessages = []
    for m in messages:
        match = re.match(rule, m)
        if match:
            start, stop = match.span()
            if stop - start == len(m):
                correctMessages.append(m)
    return correctMessages


def CountValidMonsterMessages(puzzleInput, rule="0"):
    rules, messages = puzzleInput.split("\n\n")

    messages = messages.splitlines()

    rulesDict = {}
    for r in rules.splitlines():
        key, values = r.split(":")
        rulesDict[key] = " {0} ".format(values.strip().replace('"', ""))

    rule = GetRule(rulesDict[rule], rulesDict).strip().replace(" ", "")

    return len(GetCorrectMessages(messages, rule))


def CountValidMonsterMessagesLoop(puzzleInput, rule="0", depth=5):
    rules, messages = puzzleInput.split("\n\n")

    rules += "\n8: 42 | 42 8" \
             "\n11: 42 31 | 42 11 31"

    rulesDict = {}
    for r in rules.splitlines():
        key, values = r.split(":")
        rulesDict[key] = " {0} ".format(values.strip().replace('"', ""))

    messages = messages.splitlines()
    correctMessages = []

    rules8 = rulesDict["8"].split("|")
    rule8a = GetRule(rules8[0], rulesDict, skipChars=["8", "11"])
    rule8b = GetRule(rules8[1], rulesDict, skipChars=["8", "11"])
    rules11 = rulesDict["11"].split("|")
    rule11a = GetRule(rules11[0], rulesDict, skipChars=["8", "11"])
    rule11b = GetRule(rules11[1], rulesDict, skipChars=["8", "11"])

    rules = rulesDict[rule].split("|")
    possibleRules = [GetRule(r, rulesDict, skipChars=["8", "11"]) for r in rules]

    for __ in range(depth):
        rulesTemp = []
        for possibleRule in possibleRules:
            for rule8, rule11 in [[rule8a, rule11a], [rule8a, rule11b],
                                  [rule8b, rule11a], [rule8b, rule11b]]:
                resultRule = possibleRule.\
                    replace("8", " {0} ".format(rule8)).\
                    replace("11", " {0} ".format(rule11))

                if "8" in rule8 or "11" in rule11:
                    rulesTemp.append(resultRule)
                else:
                    for cm in GetCorrectMessages(messages, resultRule.strip().replace(" ", "")):
                        messages.remove(cm)
                        correctMessages.append(cm)

        possibleRules = rulesTemp.copy()

    return len(correctMessages)
