with open("input.txt", 'r') as f:
    lines = f.read().split('\n')

#part 1
def part1():
    symbolField = []
    numberPos = {}
    endNumber = True
    total = 0
    for i, line in enumerate(lines):  
        for j, char in enumerate(line):
            if char.isdigit():           
                if endNumber:
                    xy = []
                    number = char
                    endNumber = False
                else:
                    number += char
                if j == len(line)-1:
                    endNumber = True
                    numberPos[tuple(xy)] = int(number)
                xy.append((i,j))
            else:
                if not endNumber:
                    endNumber = True
                    numberPos[tuple(xy)] = int(number)

                if char != '.':
                    for sY in range(i, i+3):
                        for sX in range (j, j+3):
                            if sY-1 >=0 and sY-1 < len(lines) and sX-1 >=0 and sX-1 < len(line):
                                symbolField.append((sY-1, sX-1))

    if not endNumber:
        numberPos[tuple(xy)] = int(number)

    for key, value in numberPos.items():
        for pos in key:
            if pos in symbolField:
                total += value
                break
    return total

# part 2
def part2():
    symbolFields = {}
    numberPos = {}
    endNumber = True
    total = 0
    for i, line in enumerate(lines):  
        for j, char in enumerate(line):
            if char.isdigit():           
                if endNumber:
                    xy = []
                    number = char
                    endNumber = False
                else:
                    number += char
                if j == len(line)-1:
                    endNumber = True
                    numberPos[tuple(xy)] = int(number)
                xy.append((i,j))
            else:
                if not endNumber:
                    endNumber = True
                    numberPos[tuple(xy)] = int(number)

                if char == '*':
                    symbolField = []
                    for sY in range(i, i+3):
                        for sX in range (j, j+3):
                            if sY-1 >=0 and sY-1 < len(lines) and sX-1 >=0 and sX-1 < len(line):
                                symbolField.append((sY-1, sX-1))
                    symbolFields[tuple(symbolField)]=0

    if not endNumber:
        numberPos[tuple(xy)] = int(number)

    found = False
 
    for key, value in numberPos.items():
        for pos in key:
            for key2 in symbolFields.keys():
                if pos in key2:
                    symbolFields[key2] += 1
                    found = True
                    break
            if found:
                found = False
                break

    
    for key, value in symbolFields.items():
        mult = 1
        if value == 2:
            for key2, value2 in numberPos.items():
                for pos2 in key2:
                    if pos2 in key:
                        mult*=value2
                        break
            total += mult
    
    return total

print(f'\n\ntotal: \n{part2()}')


