from re import split
with open("input.txt", 'r') as f:
    lines = f.read().split('\n')

rules = {"red": 12, "blue": 14, "green": 13}

# Part 1
def part1():   
    error = False
    gameIDs = 0
    for line in lines:
        gameInfo, data = line.split(": ")
        gameId = int(gameInfo.split()[1])
        sets = split(',|;', data)
        colors = {}
        for set in sets:
            amount, color = set.split()
            amount = int(amount)
            if color not in colors.keys() or colors[color] < amount:
                colors[color] = amount
        for key in colors.keys():
            if colors[key] > rules[key]:
                error = True
                break
        if not error:
            gameIDs += gameId
        else:
            error = False
    return gameIDs

#Part 2
def part2():
    cubesSum = 0
    for line in lines:
        data = line.split(": ")[1]
        sets = split(',|;', data)
        colors = {}
        cubesMult = 1
        for set in sets:
            amount, color = set.split()
            amount = int(amount)
            if color not in colors.keys() or colors[color] < amount:
                colors[color] = amount

        for key in colors.keys():
            cubesMult *= colors[key]
        cubesSum += cubesMult

    return cubesSum

print(part2())