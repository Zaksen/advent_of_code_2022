from day_2_helpers.helpers import correspondances


file_path = 'inputs/day_2.txt'


def get_result(a, b):
    if a == b:
        return 3
    if a == 'Rock':
        return 6 if b == 'Scissors' else 0
    if a == 'Paper':
        return 6 if b =='Rock' else 0
    if a == 'Scissors':
        return 6 if b == 'Paper' else 0
 
 def get_shape_to_match_result(shape, result):
    if shape == 'Paper':
         pass
    return 0


score = 0    

with open(file_path, 'r') as f:
    for line in f:
        a, b = line.strip().split(' ')
        score += get_result(correspondances[b]['shape'], correspondances[a]['shape']) + correspondances[b]['score']

print(score)
        
        

