import re


def ParsePassport(passportInput):
    passport = {}

    entries = passportInput.split(" ")
    for entry in entries:
        key, value = entry.split(":")
        passport[key] = value
    return  passport


def CountValidPassports(passportInputs):
    count = 0
    for pi in passportInputs:
        passport = ParsePassport(pi)
        #  byr (Birth Year)
        #  iyr (Issue Year)
        #  eyr (Expiration Year)
        #  hgt (Height)
        #  hcl (Hair Color)
        #  ecl (Eye Color)
        #  pid (Passport ID)
        #  cid (Country ID)
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in passport:
                break
        else:
            count += 1

    return count


def CountValidPassportsAdvanced(passportInputs):
    count = 0
    for pi in passportInputs:
        try:
            passport = ParsePassport(pi)

            # byr (Birth Year) - four digits; at least 1920 and at most 2002
            key = "byr"
            if not 1920 <= int(passport[key]) <= 2002:
                continue

            # iyr (Issue Year) - four digits; at least 2010 and at most 2020
            key = "iyr"
            if not 2010 <= int(passport[key]) <= 2020:
                continue

            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030
            key = "eyr"
            if not 2020 <= int(passport[key]) <= 2030:
                continue

            # hgt (Height) - a number followed by either cm or in:
            #     If cm, the number must be at least 150 and at most 193
            #     If in, the number must be at least 59 and at most 76
            key = "hgt"
            unit = passport[key][-2:]
            if unit == "cm":
                number = int(passport[key][:3])
                if not 150 <= number <= 193:
                    continue
            elif unit == "in":
                number = int(passport[key][:2])
                if not 59 <= number <= 76:
                    continue
            else:
                continue

            # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
            key = "hcl"
            pattern = re.compile("#[a-f|0-9]{6}")
            if pattern.fullmatch(passport[key]) is None:
                continue

            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
            key = "ecl"
            if passport[key] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue

            # pid (Passport ID) - a nine-digit number, including leading zeroes
            key = "pid"
            pattern = re.compile("[0-9]{9}")
            if pattern.fullmatch(passport[key]) is None:
                continue

            count += 1

        except (KeyError, ValueError):
            continue

    return count
