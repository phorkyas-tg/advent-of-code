import re


def HasAbba(s):
    for i in range(len(s) - 3):
        if s[i] != s[i + 1] and \
                s[i] == s[i + 3] and \
                s[i + 1] == s[i + 2]:
            return True
    return False


def GetAba(s):
    aba = []
    for i in range(len(s) - 2):
        if s[i] != s[i + 1] and \
                s[i] == s[i + 2]:
            aba.append(s[i:i+3])
    return aba


def CountTLS(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    count = 0
    for line in inputLines:
        hypernetSequence = re.findall("\[(.*?)\]", line.strip())
        for hs in hypernetSequence:
            line = re.sub(hs, "", line)

        ip = line.strip().split("[]")

        if sum(map(HasAbba, ip)) >= 1 and sum(map(HasAbba, hypernetSequence)) == 0:
            count += 1

    return count


def CountSSL(file):
    file = open(file, 'r')
    inputLines = file.readlines()
    file.close()

    count = 0
    for line in inputLines:
        hypernetSequence = re.findall("\[(.*?)\]", line.strip())
        for hs in hypernetSequence:
            line = re.sub(hs, "", line)

        ips = line.strip().split("[]")

        aba = []
        for hs in hypernetSequence:
            aba.extend(GetAba(hs))

        bab = ["{1}{0}{1}".format(s[0], s[1]) for s in aba]

        hasSSL = False
        for ip in ips:
            for s in bab:
                if s in ip:
                    hasSSL = True

        if hasSSL:
            count += 1

    return count




