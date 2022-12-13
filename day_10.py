def register(cycle_duration):
    instructions = read_instructions('inputs/day_10.txt')
    x=1
    for line in instructions:
        if cycle_duration <= 0:
            return x 
        if line.startswith('a'):
            _, value = line.rstrip().split(" ")
            if cycle_duration - 2 > 0:
                x += float(value)
            cycle_duration -= 2
        else:
            cycle_duration -= 1
        
def read_instructions(file_name):
    with open(file_name, 'r') as f:
        for row in f:
            yield row.rstrip()


cycles = [i * 20 for i in range(1, 12) if i%2 != 0]
y = [register(j) * j for j in cycles if register(j)]

print(sum(y))
