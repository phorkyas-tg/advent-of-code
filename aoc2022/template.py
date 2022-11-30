import os

def puzzleA(lines):
    return 0


def puzzleB(lines):
    return 0


if __name__ == '__main__':
    day = "01"
    script_dir = os.path.dirname(__file__)
    rel_path = "input/input_{0}.txt".format(day)
    abs_file_path = os.path.join(script_dir, rel_path)
    
    with open(abs_file_path, encoding = 'utf-8') as file:
        inputLines = file.readlines()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 0
    assert b == 0
