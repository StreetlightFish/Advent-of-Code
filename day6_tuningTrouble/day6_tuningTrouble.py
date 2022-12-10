with open('day6_input.txt') as line:
    for string in line:
        for i in range(len(string)):
            unique_char = []
            if i >= 3:
                last4 = string[i-3:i+1]
                for j in range(4):
                    if string[i - j] not in unique_char:
                        unique_char.append(string[i - j])
                if len(unique_char) == 4:
                    # print(unique_char)
                    print('Start of packet marker:', i + 1)
                    break

with open('day6_input.txt') as line:
    for string in line:
        for i in range(len(string)):
            unique_char = []
            if i >= 13:
                last4 = string[i-13:i+1]
                for j in range(14):
                    if string[i - j] not in unique_char:
                        unique_char.append(string[i - j])
                if len(unique_char) == 14:
                    # print(unique_char)
                    print('Start of message marker:', i + 1)
                    break