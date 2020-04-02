def readfiles(filename):
    for line in open(filename):
        yield line.strip()

def grep(filename):
    for pattern in readfiles(filename):
        count = 0
        for line in readfiles(filename):
            if pattern in line:
                count += 1
        if count <= 1:
            yield pattern

def printlines(lines):
    for line in lines:
        print(line)


def main(filename):
    printlines(grep(filename))

main('1.txt')