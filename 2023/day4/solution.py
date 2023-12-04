with open("input.txt", 'r') as f:
    lines = f.read().split('\n')

# part 1
def part1():
    total = 0
    for line in lines:
        _, numbers = line.split(": ")
        winningNums, myNums = numbers.split(" | ")
        winningNums = winningNums.split()
        myNums = myNums.split()
        amount = 0
        for num in myNums:
            if num in winningNums:
                amount += 1
        if amount:
            total += pow(2, amount -1)
    return total

# part 2
def part2():
    cards = {i+1: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        _, numbers = line.split(": ")
        winningNums, myNums = numbers.split(" | ")
        winningNums = winningNums.split()
        myNums = myNums.split()
        for j in range(cards[i+1]):
            amount = 0
            for num in myNums:
                if num in winningNums:
                    amount += 1
            for a in range(amount):
                cards[i+2+a] += 1
    return sum(cards.values())

print(part2())
