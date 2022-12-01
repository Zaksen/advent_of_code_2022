max_calories = 0
snacks = []

with open('inputs/day_1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            max_calories += int(line)
        else:
            snacks.append(max_calories)
            max_calories=0

sorted_snacks = sorted(snacks, reverse=True)

#First answer
print(max(sorted_snacks))
#second answer
print(sum(sorted_snacks[0:3]))