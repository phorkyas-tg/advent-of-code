import re


def GetDigits(number):
    return [int(i) for i in str(number)]


def DigitsBruteForce(min, max, regex="{2}"):
    counter = 0

    for i in range(min, max + 1):
        digits = GetDigits(i)

        lastDigit = None
        for digit in digits:
            if lastDigit is not None and digit < lastDigit:
                break
            lastDigit = digit

        else:
            expression = r'0{0}|1{0}|2{0}|3{0}|4{0}|5{0}|6{0}|7{0}|8{0}|9{0}'.format(regex)
            out = re.findall(expression, str(i))
            if out:
                for o in out:
                    if len(o) == 2:
                        counter += 1
                        break
    return counter
