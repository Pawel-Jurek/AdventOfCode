import re
with open("input.txt", 'r') as f:
    lines = f.read().split()

# part1
def findNumbers(line):
    number=""
    for char in line:
        if char.isdigit():
            number += char
            break
    for char in line[::-1]:
        if char.isdigit():
            number += char
            break
    return int(number) if number!="" else 0

#print(sum(findNumbers(line) for line in lines))



# part2
nums = {
    "one":1,
    "two":2, 
    "three":3, 
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9
}

def findNumbers2(line):
    stringNums = {match.start(): str(nums[key]) for key in nums.keys() if key in line for match in re.finditer(re.escape(key), line)}
    firstNumber= stringNums[min(stringNums.keys())]
    lastNumber= stringNums[max(stringNums.keys())]
    
    return int(firstNumber + lastNumber)

print(sum(findNumbers2(line) for line in lines))