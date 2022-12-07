import string
import math

priorities = list(string.ascii_letters)
total_priority = 0

with open("priority.txt", "r") as f:
    sacks = f.read().splitlines()

    for i in range(0, len(sacks), 3):
        badge = ""

        first_sack = sacks[i]
        second_sack = sacks[i + 1]
        third_sack = sacks[i + 2]


        # find duplicate character
        for letter in first_sack:
            if letter in second_sack and letter in third_sack:
                badge = letter

        # declare numerical priority 
        total_priority += priorities.index(badge) + 1

print(total_priority)