file_path = 'inputs/day_2.txt'

shape_scores = [1, 2, 3]
shape_alphabet = ['A', 'B', 'C']
result_alphabet = ['X', 'Y', 'Z']
result_scores = [0, 3, 6]

score = 0

def get_shape_to_match_result(shape, result):
    shape_index = shape_alphabet.index(shape)
    if result == 'Z':
        return (shape_index + 1) % 3
    if result == 'Y':
        return shape_index
    else:
        return shape_index - 1

with open(file_path, 'r') as f:
    for line in f:
        a, b = line.strip().split(' ')
        shape_to_choose = get_shape_to_match_result(a, b)
        score += shape_scores[shape_to_choose] + result_scores[result_alphabet.index(b)]
        
print(score)