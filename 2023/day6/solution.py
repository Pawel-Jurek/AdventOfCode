with open("input.txt", 'r') as f:
    lines = f.read().split('\n')

def findMin(time, distance):
    for t in range(1, time+1):
        if (time-t)*t > distance:
            return t
    return -1

def findMax(time, distance):
    for t in range(time,0,-1):
        if (time-t)*t > distance:
            return t
    return -1
# part1
def part1():
    _, times = lines[0].split(": ")
    times = times.split()

    _, distances = lines[1].split(": ")
    distances = distances.split()

    total = 1
    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        total *= (findMax(time, distance) - findMin(time, distance) + 1)

    return total

# part2
def part2():
    _, times = lines[0].split(": ")
    time = int(times.replace(" ",""))

    _, distances = lines[1].split(": ")
    distance = int(distances.replace(" ",""))

    return findMax(time, distance) - findMin(time, distance) + 1
     

print(part2())