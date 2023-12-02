import re

with open('input.txt') as art:
    sum = 0
    for line in art:
        line = re.sub('one',    'o1e', line, flags=re.IGNORECASE)
        line = re.sub('two',    't2o', line, flags=re.IGNORECASE)
        line = re.sub('three',  't3e', line, flags=re.IGNORECASE)
        line = re.sub('four',   'f4r', line, flags=re.IGNORECASE)
        line = re.sub('five',   'f5e', line, flags=re.IGNORECASE)
        line = re.sub('six',    's6x', line, flags=re.IGNORECASE)
        line = re.sub('seven',  's7n', line, flags=re.IGNORECASE)
        line = re.sub('eight',  'e8t', line, flags=re.IGNORECASE)
        line = re.sub('nine',   'n9e', line, flags=re.IGNORECASE)
        result = re.findall(r'\d',line)
        sum += int(result[0] + result[-1])

    print(sum)