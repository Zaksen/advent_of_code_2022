file_path = 'inputs/day_6.txt'

with open(file_path, 'r') as f:
    content = f.read()
    
def get_marker(s, nb_characters):
    for i in range(len(s)):
        if len(set(s[i:i+nb_characters])) == len(s[i:i+nb_characters]):
            return i+nb_characters
         
print(get_marker(content, 4))
print(get_marker(content, 14))