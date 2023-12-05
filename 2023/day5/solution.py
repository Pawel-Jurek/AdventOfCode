with open("input.txt", 'r') as f:
    lines = f.read().split('\n\n')


seeds = lines[0].split(": ")[1]
seeds = seeds.split()
seeds = [int(seed) for seed in seeds]

# part 1
def part1(seeds):
    for i in range(1, len(lines)):
        mapping = {}
        _, numbers = lines[i].split(":")
        print(_)
        numsLines = numbers.split("\n")
        for line in numsLines:
            if line != "":
                destination, source, length = line.split()
                destination = int(destination)
                source = int(source)
                length = int(length)
                for seed in seeds:
                    if seed in range(source, source+length):
                        mapping[seed] = destination - source + seed 
                
        for s in seeds:
            if s not in mapping.keys():
                mapping[s]=s

        seeds = [mapping[t] for t in seeds]

    return min(seeds)

# part 2

def part2(seeds):
    
    for i in range(1, len(lines)):
        for k in range(0,len(seeds)-1,2):
            for j in range(1,seeds[k+1]):
                seeds.append(seeds[k]+j)
        mapping = {}
        _, numbers = lines[i].split(":")
        print(_)
        numsLines = numbers.split("\n")
        for line in numsLines:
            if line != "":
                destination, source, length = line.split()
                destination = int(destination)
                source = int(source)
                length = int(length)
                for seed in seeds:
                    if seed in range(source, source+length):
                        mapping[seed] = destination - source + seed 
                
        for s in seeds:
            if s not in mapping.keys():
                mapping[s]=s

        seeds = [mapping[t] for t in seeds]
    
    return min(seeds)


print(part2(seeds))
