file_path = 'inputs/day_4.txt'

def intersection(list1, list2):
    return [value for value in list1 if value in list2]

nb_containers_part_1 = 0
nb_containers_part_2 = 0

with open(file_path, 'r') as f:
    for line in f:
        first, second = line.rstrip().split(',')
        first_section = [i for i in range(int(first.split('-')[0]), int(first.split('-')[1]) + 1)]
        second_section = [i for i in range(int(second.split('-')[0]), int(second.split('-')[1]) + 1)]
        if len(intersection(first_section, second_section)) > 0:
            nb_containers_part_2 += 1
            if intersection(first_section, second_section) == min(first_section, second_section, key=len):
                nb_containers_part_1 += 1
            
print(nb_containers_part_1)
print(nb_containers_part_2)