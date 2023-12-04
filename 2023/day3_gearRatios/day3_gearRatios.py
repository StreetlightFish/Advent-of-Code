import re
sumParts = 0
partList = []

## Index every character with a list from input.txt
#
# partList[line][character]
#
with open('input.txt') as input:
    for line in input:
        partList.append(line)

# print(partList)
# Loop through partList lines to find numbers.
for line in partList:
    i = 0
    
    # Find all the numbers in the current line in the order they appear
    numbers = re.findall(r'\d+',line)
    print(numbers)
    numberIndex = 0
    skipDigit = 0

    # Search lines for digit for start/end of numbers
    for character in line:
        j = 0

        if skipDigit == 0 and character ==  numbers[numberIndex][0]:
            print("Found one!")
            numberIndex += 1
            skipDigit = len(numbers[numberIndex]) - 1
            print("Number Length: " + str(skipDigit + 1))
            print(character)
        elif skipDigit != 0:
            print(character)
            skipDigit -= 1
            