with open("input.txt", 'r') as f:
    lines = f.read().split('\n')


def part1():
    total = 0
    for line in lines:
        line = [int(l) for l in line.split(" ")]
        differences = [line]
        while line.count(0) != len(line):
            line = [line[i+1]-line[i] for i in range(len(line)-1)]
            differences.append(line)
        differences[-1].append(0)
        for i in range(len(differences)-2,-1,-1):
            lenght = len(differences[i]) - 1
            differences[i].append(differences[i][lenght]+differences[i+1][lenght])
        total += differences[0][-1]
    return total


def part2():
    total = 0
    for line in lines:
        line = [int(l) for l in line.split(" ")]
        differences = [line[::-1]]
        while line.count(0) != len(line):
            line = [line[i+1]-line[i] for i in range(len(line)-1)]
            differences.append(line[::-1])
        differences[-1].append(0)
        for i in range(len(differences)-2,-1,-1):
            lenght = len(differences[i]) - 1
            differences[i].append(differences[i][lenght]-differences[i+1][lenght])
        total += differences[0][-1]
    return total


print(f'total: {part2()}')