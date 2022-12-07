import os

def getDirs(lines):
    currentDir = "/"
    dirs = {currentDir: 0}

    for line in lines:
        commands = line.strip().split(" ")
        if commands[0] == "$" and commands[1] == "cd":
            if commands[2] == "/":
                currentDir = "/"
            elif commands[2] == "..":
                currentDir = currentDir.rsplit("/", 2)[0] + "/"
            else:
                currentDir += commands[2] + "/"
                dirs.setdefault(currentDir, 0)
                    
        elif commands[0].isnumeric():
            dirs[currentDir] += int(commands[0])
    return dirs


def getDirTotalSize(dirs):
    dirTotalSize = {}
    for currentDir in dirs.keys():
        dirTotalSize[currentDir] = sum([size for dirName, size in dirs.items()
                                       if dirName.startswith(currentDir)])

    return dirTotalSize


def puzzleA(lines):
    dirs = getDirs(lines)
    dirTotalSize = getDirTotalSize(dirs)

    maxSize = 100000

    return sum([value for value in dirTotalSize.values() if value <= maxSize])


def puzzleB(lines):
    dirs = getDirs(lines)
    dirTotalSize = getDirTotalSize(dirs)

    spaceAvailable = 70000000
    unusedSpaceNeeded = 30000000
    totalSpaceUsed = dirTotalSize.get("/")
    freeUpSpace = unusedSpaceNeeded - (spaceAvailable - totalSpaceUsed) 

    return min([value for value in dirTotalSize.values() if value >= freeUpSpace])


if __name__ == '__main__':
    day = "07"
    currentPath = os.path.dirname(__file__)
    relPath = "input/input_{0}.txt".format(day)
    absPath = os.path.join(currentPath, relPath)
    
    with open(absPath, encoding = 'utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 1325919
    assert b == 2050735
