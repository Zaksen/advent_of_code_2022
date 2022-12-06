from helpers.h_day_2 import correspondances

file_path = 'inputs/day_2.txt'

def circular(el):
    return list(range(0, 3))[(el+1) % 3]

def get_result(a, b):
    return 3 if a == b else (circular(a) == b) * 6

def get_shape(a, result):
    if result == 1:
        return a
    elif result == 2:
        return circular(a)
    else:
        return circular(circular(a))

score_part_1 = 0
score_part_2 = 0

with open(file_path, 'r') as f:
    for line in f:
        a, b = line.strip().split(' ')
        score_part_1 += get_result(['A', 'B', 'C'].index(a), ['X', 'Y', 'Z'].index(b)) + ['X', 'Y', 'Z'].index(b) + 1
        score_part_2 += get_shape(['A', 'B', 'C'].index(a), ['X', 'Y', 'Z'].index(b)) + 1 + ['X', 'Y', 'Z'].index(b) * 3
        
print(score_part_1)
print(score_part_2)
