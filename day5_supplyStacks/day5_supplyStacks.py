# Task 1 ---------------------------------------------------

stack_dict = {
    '1': ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
    '2': ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
    '3': ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
    '4': ['R', 'S', 'C', 'L'],
    '5': ['M', 'V', 'T', 'P', 'F', 'B'],
    '6': ['T', 'R', 'Q', 'N', 'C'],
    '7': ['G', 'V', 'R'],
    '8': ['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
    '9': ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']
 }

with open("day5_input.txt") as commands:
    for line in commands:
        command_list = line.split()
        
        for i in range(int(command_list[1])):
            val_to_move = stack_dict[command_list[3]].pop(-1)
            stack_dict[command_list[5]].append(val_to_move)

final_word = ''
for i in range(1, 10):
    final_word += stack_dict[str(i)][-1]

print('Task 1:', final_word)



# Task 2 ---------------------------------------------------

stack_dict = {
    '1': ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
    '2': ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
    '3': ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
    '4': ['R', 'S', 'C', 'L'],
    '5': ['M', 'V', 'T', 'P', 'F', 'B'],
    '6': ['T', 'R', 'Q', 'N', 'C'],
    '7': ['G', 'V', 'R'],
    '8': ['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
    '9': ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']
 }

with open("day5_input.txt") as commands:
    for line in commands:
        command_list = line.split()
        
        list_to_move = []
        for i in range(int(command_list[1])):
            val_to_move = stack_dict[command_list[3]].pop()
            list_to_move.append(val_to_move)

        list_to_move.reverse()
        for i in range(len(list_to_move)):
            stack_dict[command_list[5]].append(list_to_move[i])

final_word = ''
for i in range(1, 10):
    final_word += stack_dict[str(i)][-1]

print('Task 2:', final_word)