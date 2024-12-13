import re
import math
sumParts = 0
sumGearRatio = 0
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
            iUpperBound = len(partList) if (i + 2 > len(partList)) else (i + 2)
            
            # Define horizontal bounds of symbol search to not exceed size of "line"
            jLowerBound = 0 if (j - 1 < 0) else (j - 1)
            jUpperBound = len(line) if (j + 1 > len(line)) else (j + len(numbers[numberIndex]) + 1)
            # print("Number: " + numbers[numberIndex])
            # print(iLowerBound, iUpperBound, jLowerBound, jUpperBound)

            # Check for symbol matches within the bounds defined around the number
            symbols = "!@#$%^&*()-=_+[]\{\};:\'\"<,>/?\\|"
            match = False
            for iIndex in range(iLowerBound, iUpperBound):
                if match is False:
                    for jIndex in range(jLowerBound, jUpperBound):
                        # print(iIndex, jIndex)
                        if match is False and (partList[iIndex][jIndex] in symbols):
                            print(f"Match! Found {partList[iIndex][jIndex]} symbol. Adding {numbers[numberIndex]} to sumParts ({sumParts})")
                            match = True
                            sumParts += int(numbers[numberIndex])
            
            # Part two: check for gears
            symbols = "*"
            match = False
            for iIndex in range(iLowerBound, iUpperBound):
                if match is False:
                    for jIndex in range(jLowerBound, jUpperBound):
                        if match is False and (partList[iIndex][jIndex] in symbols):
                            # print("Found a potential gear!")
                            iStarLowerBound = iIndex
                            iStarUpperBound = len(partList) if (iIndex + 2 > len(partList)) else (iIndex + 2)
                            
                            jStarLowerBound = 0 if (jIndex - 1 < 0) else (jIndex - 1)
                            jStarUpperBound = len(line) if (j + 2 > len(line)) else (j + 2)
                            numMatch = False
                            print(iIndex, jIndex)
                            print(iStarLowerBound, iStarUpperBound, jStarLowerBound, jStarUpperBound)
                            for iStarIndex in range(iStarLowerBound, iStarUpperBound):
                                if numMatch is False:
                                    for jStarIndex in range(jStarLowerBound, jStarUpperBound):
                                        if numMatch is False and re.match(r'\d',partList[iStarIndex][jStarIndex]):
                                            print("Found a gear!")
                                            numMatch = True
                                jStarLowerBound -= 1

            skipDigit -= 1
            if numberIndex < len(numbers) - 1:
                numberIndex += 1
        elif skipDigit != 0:
            # print(character)
            skipDigit -= 1

        j += 1
    i += 1

print(f"SOLUTION! Parts Sum: {sumParts}")
print(f"SOLUTION! Gear Ratio Sum: {sumGearRatio}")