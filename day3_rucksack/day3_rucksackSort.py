abc_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
    's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x':24,
    'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30,
    'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
    'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42,
    'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 
    'W': 49, 'X':50, 'Y': 51, 'Z': 52}
priority_sum = 0

with open('day3_rucksack.txt') as rucksack:
    for line in rucksack:
        letter_list = []
        first_half = slice(0, len(line)//2)
        second_half = slice(len(line)//2, len(line))
        #print(line[first_half], line[second_half])
        for letterfh in line[first_half]:
            for lettersh in line[second_half]:
                if letterfh == lettersh and letterfh not in letter_list:
                    #print(letterfh)
                    priority_sum += abc_dict[lettersh]
                    letter_list.append(letterfh)
                    # print(letterfh, priority_sum)

print('The sum of item priority is:', priority_sum)

with open('day3_rucksack.txt') as rucksack:
    line1 = ''
    line2 = ''
    line3 = ''
    #the_letter = ''
    priority_sum = 0
    counter = 0
    for line in rucksack:
        if counter % 3 == 0:
            line1 = line.strip('\n')
            counter += 1
        elif counter % 3 == 1:
            line2 = line.strip('\n')
            counter += 1
        elif counter % 3 == 2:
            line3 = line.strip('\n')
            letter_found = False
            for letter1 in line1:
                for letter2 in line2:
                    for letter3 in line3:
                        if letter1 == letter2 == letter3 and letter_found == False:
                            priority_sum += abc_dict[letter1]
                            letter_found = True
            counter += 1
    print('Three Elf Group Priority:', priority_sum)