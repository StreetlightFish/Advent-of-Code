import re

redMax  = 12
greenMax = 13
blueMax = 14
idSum = 0
powerSum = 0

with open('input.txt') as input:
    for games in input:
        gameNumber, record = games.split(":")
        gameNumber = gameNumber.split()
        
        goodGame = True
        redMin = 0
        greenMin = 0
        blueMin = 0

        match = record.split(";")
        for result in match:
            round = result.split(",")
            
            red = 0
            green = 0
            blue = 0

            for color in round:
                end = color.split()
                if end[1] == "green":
                    green += int(end[0])
                elif end[1] == "blue":
                    blue += int(end[0])
                elif end [1] == "red":
                    red += int(end[0])
            
            if redMax < red or greenMax < green or blueMax < blue:
                goodGame = False
            
            if redMin < red:        redMin = red
            if greenMin < green:    greenMin = green
            if blueMin < blue:      blueMin = blue
        
        if goodGame:
            idSum += int(gameNumber[1])
        
        powerSum += redMin * greenMin * blueMin

    print("Challenge 1 (Sum ID): " + str(idSum))
    print("Challenge 2 (Sum of Power): " + str(powerSum))