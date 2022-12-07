import string
import math

priorities = list(string.ascii_letters)
total_priority = 0

with open("priority.txt", "r") as f:
    sacks = f.read().splitlines()

    for i in range(len(sacks)):
        priority_latter = ""
        sack = sacks[i]

        items_in_first_sack = math.floor(len(sack) / 2)
        items_in_second_sack = len(sack) - items_in_first_sack

        first_sack = sack[:items_in_first_sack]
        second_sack = sack[items_in_second_sack:]

        # find duplicate character
        for letter in first_sack:
            if letter in second_sack:
                priority_latter = letter

        # declare numerical priority 
        total_priority += priorities.index(priority_latter) + 1

print(total_priority)