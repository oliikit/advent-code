large_food = 0
elf_num = 0

with open("food.txt", "r") as f:
    data = f.read()
    
    total_calories = [ 0 ]

    for line in data.splitlines():
        cals = 0

        if len(line) == 0:
            elf_num += 1
            total_calories.append(0)
            next
        else:
            cals = int(line)

        #  adds the calories to the total
        total_calories[elf_num] += cals

    total_calories.sort()
    print(total_calories[-1])

    