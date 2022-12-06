file_path = 'inputs/day_3.txt'
        
def get_item(first, second):
    for i in first:
        for j in second:
            if i == j:
                return i
            
def get_priority(item):
    return ord(item) - 38 if item.isupper() else ord(item) - 96

sum_of_priorities = 0

with open(file_path, 'r') as f:
    for line in f:
        line = line.rstrip()
        first_compartment = line[0:len(line)//2]
        second_compartment = line[len(line)//2:len(line)]
        sum_of_priorities += get_priority(get_item(first_compartment, second_compartment))
        
print(sum_of_priorities)

with open(file_path, 'r') as f:
    content = [set(line.rstrip()) for line in f]
    
sum_of_priorities_part_two = 0

i = 0
while i < len(content) // 3:
    sum_of_priorities_part_two += get_priority(''.join(set.intersection(content[3*i], content[3*i + 1], content[3*i + 2])))
    i += 1

print(sum_of_priorities_part_two)