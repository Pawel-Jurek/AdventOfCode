with open("input.txt", 'r') as f:
    instruction, lines = f.read().split('\n\n')

instruction = instruction.replace("R", '1')
instruction = instruction.replace("L", '0')

lines = lines.split("\n")

# part 1

def part1(lines, instruction):
    network = {}
    for line in lines:
        key, values = line.split(" = (")
        values = values.replace(')', "").split(", ")
        network[key] = values

    currentPos = "AAA"
    destination = "ZZZ"
    moves = 0
    i=0
    while currentPos != destination:
        i %= len(instruction)
        currentPos = network[currentPos][int(instruction[i])]
        moves += 1
        i+=1
    return moves

# part 2

def lcm_of_array(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        num1 = lcm
        num2 = arr[i]
        gcd = 1
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        gcd = num1
        lcm = (lcm * arr[i]) // gcd
    return lcm
    
    
def part2(lines,instruction):
    network = {}
    currentPos = []
    distances = []
    
    for line in lines:
        key, values = line.split(" = (")
        values = values.replace(')', "").split(", ")
        network[key] = values
        if key[2] == "A":
            currentPos.append(key)

    for pos in currentPos:
        positions = []
        for i in range(200000):
            if pos[2] == "Z":
                positions.append(i+1)
            pos = network[pos][int(instruction[i%len(instruction)])]
        distances.append(positions[1]-positions[0])

    return lcm_of_array(distances)



print(part2(lines,instruction))