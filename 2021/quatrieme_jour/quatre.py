# how many pairs fully contain the other?

full_pairs = 0

with open('pairs.txt', 'r') as f:
    pairs = f.readlines()

    for i in range(len(pairs)):
        set = pairs[i].split(',')

        # split the string and convert to int
        first = set[0].split('-')
        first[0] = int(first[0])
        first[1] = int(first[1])

        second = set[1].split('-')
        second[0] = int(second[0])
        second[1] = int(second[1])

        # check if the first pair contains the second
        if first[0] <= second[0] and first[1] >= second[1]:
            full_pairs += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            full_pairs += 1
        
print(full_pairs)

        