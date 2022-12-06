file_path = 'inputs/day_1.txt'

def get_snacks(file_path):
    calories = 0
    snacks = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                calories += int(line)
            else:
                snacks.append(calories)
                calories=0
    return sorted(snacks, reverse=True)
    
snacks = get_snacks(file_path)
print(max(snacks), sum(snacks[0:3]))
