with open('day1_elfCalories.txt') as elfCalories:
    most_Calories = 0
    second_Most_Calories = 0
    third_Most_Calories = 0
    current_elf = 0
    for line in elfCalories:
        if line != '\n':
            current_elf += int(line)
        else:
            if current_elf > most_Calories:
                third_Most_Calories = second_Most_Calories
                second_Most_Calories = most_Calories
                most_Calories = current_elf
            elif most_Calories > current_elf > second_Most_Calories:
                third_Most_Calories = second_Most_Calories
                second_Most_Calories = current_elf
            elif second_Most_Calories > current_elf > third_Most_Calories:
                third_Most_Calories = current_elf
            current_elf = 0

    print('Most Calories:', most_Calories)
    print('Second Most Calories:', second_Most_Calories)
    print('Third Most Calories:', third_Most_Calories)
    print('Top three elves sum:', most_Calories + second_Most_Calories + third_Most_Calories)