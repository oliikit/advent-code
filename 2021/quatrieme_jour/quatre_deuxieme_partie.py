# how many pairs _just_ overlap

overlap = 0

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

        # beginning of second range is smaller or equal to the end of first range
        # and beginning of first range is smaller or equal to the end of second range
        if second[0] <= first[1] and first[0] <= second[1]:
            overlap += 1

print(overlap)

        