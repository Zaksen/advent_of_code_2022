file_path = 'inputs/day_2.txt'

def circular(el:int, nb_times) -> int:
    return list(range(0, 3))[(el+nb_times) % 3]

def get_result(a:int, b:int) -> int:
    return 3 if a == b else (circular(a, 1) == b) * 6

def get_shape(a:int, result:int) -> int:
    return circular(a, result)

score_part_1 = score_part_2 = 0

with open(file_path, 'r') as f:
    for line in f:
        a, b = line.strip().split(' ')
        score_part_1 += get_result(['A', 'B', 'C'].index(a), ['X', 'Y', 'Z'].index(b)) + ['X', 'Y', 'Z'].index(b) + 1
        score_part_2 += get_shape(['A', 'B', 'C'].index(a), ['X', 'Y', 'Z'].index(b)) + 1 + ['Y', 'X', 'Z'].index(b) * 3
        
print(score_part_1, score_part_2)
