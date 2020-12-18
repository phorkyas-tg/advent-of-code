import re


def CalculateSubExpression(subExpression):
    result = int(subExpression[0])
    add = True
    for operator in subExpression[1:]:
        if operator == "+":
            add = True
        elif operator == "*":
            add = False
        else:
            if add:
                result += int(operator)
            else:
                result *= int(operator)
    return result


def CalculateSubExpressionAdvanced(subExpression):
    while True:
        for i, operator in enumerate(subExpression):
            if operator == "+":
                subresult = int(subExpression[i-1]) + int(subExpression[i+1])
                break
        else:
            break
        subExpression.pop(i+1)
        subExpression.pop(i)
        subExpression[i-1] = subresult

    return CalculateSubExpression(subExpression)


def Evaluate(expression, func=CalculateSubExpression):
    while True:
        subExpressions = re.findall(r"\((.*?)\)", expression)
        if len(subExpressions) == 0:
            break
        for subExpression in subExpressions:
            left = subExpression.rfind("(")
            if left >= 0:
                subExpression = subExpression[left + 1:]
            right = subExpression.find(")")
            if right >= 0:
                subExpression = subExpression[:right]
            result = func(subExpression.split(" "))
            expression = expression.replace("({0})".format(subExpression), "{0}".format(result))
    return func(expression.split(" "))


def GetSumOfCalculations(puzzleInput):
    result = 0
    for line in puzzleInput:
        result += Evaluate(line)
    return result


def GetSumOfCalculationsAdvanced(puzzleInput):
    result = 0
    for line in puzzleInput:
        result += Evaluate(line, CalculateSubExpressionAdvanced)
    return result
