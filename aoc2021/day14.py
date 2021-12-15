def step(polymer, rules, count):
    newPolymer = {}
    for pair, value in polymer.items():
        if pair in rules:
            newPolymer.setdefault(pair[0] + rules[pair], 0)
            newPolymer[pair[0] + rules[pair]] += value

            newPolymer.setdefault(rules[pair] + pair[1], 0)
            newPolymer[rules[pair] + pair[1]] += value

            count.setdefault(rules[pair], 0)
            count[rules[pair]] += value
        else:
            newPolymer.setdefault(pair, 0)
            newPolymer[pair] += value

    return newPolymer, count


def readPolymerAndRules(lines):
    line = lines[0].strip()
    polymer = {}
    for i in range(1, len(line)):
        pair = line[i - 1] + line[i]
        polymer.setdefault(pair, 0)
        polymer[pair] += 1

    count = {}
    for c in line:
        count.setdefault(c, 0)
        count[c] += 1

    rules = {}
    for i in range(2, len(lines)):
        l, r = lines[i].strip().split(" -> ")
        rules[l] = r

    return polymer, count, rules


def puzzleA(lines):
    polymer, count, rules = readPolymerAndRules(lines)

    for i in range(10):
        polymer, count = step(polymer, rules, count)

    return max(count.values()) - min(count.values())


def puzzleB(lines):
    polymer, count, rules = readPolymerAndRules(lines)

    for i in range(40):
        polymer, count = step(polymer, rules, count)

    return max(count.values()) - min(count.values())


if __name__ == '__main__':
    day = "14"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 3284
    assert b == 4302675529689
