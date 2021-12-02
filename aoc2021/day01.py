def puzzleA(lines):
    count = 0
    lastNumber = lines[0]
    for i in range(1, len(lines)):
        if lines[i] > lastNumber:
            count += 1
        lastNumber = lines[i]
    return count


def puzzleB(lines):
    newArray = []
    for i in range(len(lines) - 2):
        newArray.append(lines[i] + lines[i+1] + lines[i+2])
    return puzzleA(newArray)


if __name__ == '__main__':
    file = open("input\\input_01.txt", 'r')
    inputLines = file.readlines()
    nums = list(map(int, inputLines))
    file.close()

    print(puzzleA(nums))
    print(puzzleB(nums))
