
with open('input.txt') as sectionIDs:
    contain_count = 0
    overlap_count = 0
    for line in sectionIDs:
        set1, set2 = line.split(',')
        set1l, set1h = set1.split('-')
        set2l, set2h = set2.split('-')
        list1 = set(range(int(set1l), int(set1h) + 1))
        list2 = set(range(int(set2l), int(set2h) + 1))

        if set(list1).issubset(list2) or set(list2).issubset(list1):
            contain_count += 1
        if list1.intersection(list2):
            overlap_count += 1

        
    print(contain_count)
    print(overlap_count)