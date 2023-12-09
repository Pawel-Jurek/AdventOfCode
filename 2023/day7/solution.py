import pdb
with open("input.txt", 'r') as f:
    lines = f.read().split('\n')

#part 1
'''
cardPower = [str(i) for i in range(1, 10)] + ["T", "J", "Q", "K", "A"]
def checkPower(cards):
    repetitions = {}
    for letter in set(cards):
        repetitions[letter] = cards.count(letter)
    values = repetitions.values()
    if max(values) > 3:
        return max(values)+2
    if 3 in values:
        if 2 in values:
            return 5
        else:
            return 4
    if 2 in values:
        if len(values) == 3:
            return 3
        else:
            return 2
    else:
        return 1
'''


#part 2
cardPower = ["J"] + [str(i) for i in range(1, 10)] + ["T", "Q", "K", "A"]

def checkPower(cards):
    jokers = cards.count("J")
    repetitions = {}
    for letter in set(cards):
        if letter != "J":
            repetitions[letter] = cards.count(letter)
    values = repetitions.values() if len(repetitions)> 0 else [0]
    if max(values) + jokers > 3:
        return max(values)+ 2 + jokers
    if 3 in values:
        if 2 in values:
            return 5
        else:
            return 4
    if 2 in values and jokers > 0:
        jokers -= 1
        if jokers or len(values) == 2:
            return 5
        else: 
            return 4 

    if jokers > 1:
        jokers -= 2
        if jokers or len(values) == 2:
            return 5
        else: 
            return 4 
    if jokers:
        jokers-=1
        if 2 in values:
            return 3
        else: 
            return 2
    elif 2 in values:
        if len(values) == 3:
            return 3
        else:
            return 2
    else:
        return 1

    

hands = {}
power = {}
ranking = {}
for line in lines:
    cards, bid = line.split()
    hands[cards] = int(bid)
    power[cards] = checkPower(cards)

keys = list(power.keys())
for i in range(len(keys)):
    #pdb.set_trace()
    first = [k for k in keys if k not in ranking.keys()][0]
    rank = len(power)-i
    maximus = first
    for j in range(0, len(keys)):
        if keys[j] != first and keys[j] not in ranking.keys():
            firstValue = power[maximus]
            second = keys[j]
            secondValue = power[second]
            if firstValue <= secondValue:
                if firstValue == secondValue:
                    for it in range(5):
                        if cardPower.index(maximus[it]) < cardPower.index(second[it]):
                            maximus = second
                            break
                        elif cardPower.index(maximus[it]) > cardPower.index(second[it]):
                            break
                else:
                    maximus = second
    ranking[maximus] = rank

result = 0
for key in keys:
    result += hands[key] * ranking[key]

print(result)