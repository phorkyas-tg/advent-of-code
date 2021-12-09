def getCharNotInArrayElement(c, array):
    for element in array:
        if c not in element:
            return element
    return None


def getCharsInArrayElement(c1, c2, array):
    for element in array:
        if c1 in element and c2 in element:
            return element
    return None


def puzzleA(lines):
    outputs = []

    for line in lines:
        d, o = [d.strip().split(" ") for d in line.strip().split(" | ")]
        outputs.extend(o)

    count = sum([1 for o in outputs if len(o) in (2, 3, 4, 7)])
    return count


def puzzleB(lines):
    digits = []
    outputs = []
    for line in lines:
        d, o = [d.strip().split(" ") for d in line.strip().split(" | ")]
        digits.append(d)
        outputs.append(o)

    ret = 0
    for i in range(len(digits)):
        digit = digits[i]

        # .aaaa.
        # b....c
        # b....c
        # .dddd.
        # e....f
        # e....f
        # .gggg.

        # don't bother to fill it all - only c and f is needed
        display = {"a": None, "b": None, "c": None,
                   "d": None, "e": None, "f": None, "g": None}

        # get 1, 4, 7 and 8
        one = [x for x in digit if len(x) == 2][0]
        four = [x for x in digit if len(x) == 4][0]
        seven = [x for x in digit if len(x) == 3][0]
        eight = [x for x in digit if len(x) == 7][0]

        # get 0, 6, 9
        zsn = [x for x in digit if len(x) == 6]
        # get 2, 3, 5
        ttf = [x for x in digit if len(x) == 5]

        # assumption
        display["c"] = one[0]
        display["f"] = one[1]
        # 6 is the one without the c
        six = getCharNotInArrayElement(display["c"], zsn)
        if six is None:
            # assumption was wrong
            display["c"] = one[1]
            display["f"] = one[0]
            six = getCharNotInArrayElement(display["c"], zsn)

        zsn.remove(six)

        # assumption
        zero = zsn[0]
        nine = zsn[1]
        # get b and d by getting the chars that 4 and 1 not have in common
        bd = four.replace(display["c"], "").replace(display["f"], "")
        if bd[0] in zero and bd[1] in zero:
            # b and d cant be both in zero so the assumption was wrong
            nine = zsn[0]
            zero = zsn[1]

        # three has both c and f
        three = getCharsInArrayElement(display["c"], display["f"], ttf)
        ttf.remove(three)

        # assumption
        two = ttf[1]
        five = ttf[0]
        if display["c"] in five:
            # c cant be in 5 so the assumption was wrong
            two = ttf[0]
            five = ttf[1]

        # put everything in a list an sort it
        numbers = ["".join(sorted(n)) for n in [zero, one, two, three, four, five,
                                                six, seven, eight, nine]]

        out = ""
        for output in outputs[i]:
            output = "".join(sorted(output))
            out += str(numbers.index(output))
        ret += int(out)
    return ret


if __name__ == '__main__':
    day = "08"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 493
    assert b == 1010460
