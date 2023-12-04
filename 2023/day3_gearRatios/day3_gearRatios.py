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
i = 0
for line in partList:
    j = 0
    
    # Find all the numbers in the current line in the order they appear
    numbers = re.findall(r'\d+',line)
    # print(numbers)
    numberIndex = 0
    skipDigit = 0

    # Search lines for digit for start/end of numbers
    for character in line:
        if skipDigit == 0 and character == numbers[numberIndex][0]:
            # print("Found Number: " + str(numbers[numberIndex]))
            skipDigit = int(math.log10(int(numbers[numberIndex])))+1
            # print("Number Length: " + str(skipDigit))
            # print(character)

            # TODO: Insert loop to look for symbols at partList[i][j] +- 1 in all directions based on skipDigit
            # Define vertical bounds of symbol search to not exceed size of "partList"
            iLowerBound = 0 if (i - 1 < 0) else (i - 1)
            iUpperBound = len(partList) if (i +1 > len(partList)) else (i + 1)
            
            # Define horizontal bounds of symbol search to not exceed size of "line"
            jLowerBound = 0 if (j - 1 < 0) else (i - 1)
            jUpperBound = len(line) if (i + 1 > len(line)) else (j + 1)
            
            # Check for symbol matches within the bounds defined around the number
            symbols = "!@#$%^&*()-+?_=,<>/"
            match = False
            for iIndex in range(iLowerBound, iUpperBound+1):
                if match is False:
                    for jIndex in range(jLowerBound, jUpperBound+1):
                        if (partList[iIndex][jIndex] in symbols):
                            print("Match! Adding " + str(numbers[numberIndex]) + " to sumParts (" + str(sumParts) + ")")
                            match = True
                            sumParts += int(numbers[numberIndex])
                            break
                


            skipDigit -= 1
            if numberIndex < len(numbers) - 1:
                numberIndex += 1
        elif skipDigit != 0:
            # print(character)
            skipDigit -= 1

        j += 1
    i += 1

print("Parts Sum = " + str(sumParts))