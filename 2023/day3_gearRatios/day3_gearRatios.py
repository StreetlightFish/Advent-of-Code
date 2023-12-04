import re
import math
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
    # print(numbers)
    numberIndex = 0
    skipDigit = 0

    # Search lines for digit for start/end of numbers
    for character in line:
        j = 0
        if skipDigit == 0 and character == numbers[numberIndex][0]:
            # print("Found Number: " + str(numbers[numberIndex]))
            skipDigit = int(math.log10(int(numbers[numberIndex])))+1
            # print("Number Length: " + str(skipDigit))
            # print(character)

            # TODO: Insert loop to look for symbols at partList[i][j] +- 1 in all directions based on skipDigit

            skipDigit -= 1
            if numberIndex < len(numbers) - 1:
                numberIndex += 1
        elif skipDigit != 0:
            # print(character)
            skipDigit -= 1
            