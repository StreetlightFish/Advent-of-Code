# Part one ----------------------------------------------------------

them_dict = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
us_dict = {'X': ['rock', 1], 'Y': ['paper', 2], 'Z': ['scissors', 3]}
result_dict = {
    'rock rock': 3, 'rock paper': 6, 'rock scissors': 0,
    'paper rock': 0, 'paper paper': 3, 'paper scissors': 6,
    'scissors rock': 6, 'scissors paper': 0, 'scissors scissors': 3
    }

total_score = 0

with open('day2_gameResults.txt') as gmRslts:
    for line in gmRslts:
        them, us = line.split(' ')
        us = us[0]
        # print(them, us)
        them_resolved = them_dict[them]
        us_resolved, us_score = us_dict[us]
        key = them_resolved + " " + us_resolved
        # print(them_resolved, us_resolved, us_score)
        total_score += us_score
        total_score += result_dict[key]

print('Your total score is (Part 1):', total_score)

#  ------------------------------------------------------------------

# Part two ----------------------------------------------------------
throw_dict = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
expected_dict = {'X': ['lose', 0], 'Y': ['draw', 3], 'Z': ['win', 6]}
new_result_dict = {
    'rock lose': 3, 'rock draw': 1, 'rock win': 2,
    'paper lose': 1, 'paper draw': 2, 'paper win': 3,
    'scissors lose': 2, 'scissors draw': 3, 'scissors win': 1
    }

new_total_score = 0

with open('day2_gameResults.txt') as gmRslts:
    for line in gmRslts:
        them, us = line.split(' ')
        us = us[0]
        # print(them, us)
        them_resolved = throw_dict[them]
        us_resolved, us_score = expected_dict[us]
        key = them_resolved + " " + us_resolved
        # print(them_resolved, us_resolved, us_score)
        new_total_score += us_score
        new_total_score += new_result_dict[key]

print('Your total score is (Part 2):', new_total_score)