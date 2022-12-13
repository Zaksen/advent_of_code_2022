from inputs.classes import File, Directory

def parseInstruction(line, active_directory):
    if line.rstrip().endswith('ls'):
        return active_directory
    arg1, arg2 = [x for x in line.rstrip().split('$ ') if x != ''][0].split(' ')
    if arg1 == 'cd':
        active_directory = active_directory.get_child(arg2)
    elif arg1 == 'dir':
        active_directory.create_child(Directory(arg2, parent=active_directory))
    else:
        active_directory.create_child(File(arg2, arg1))
    return active_directory
        
with open('inputs/day_7.txt', 'r') as f:
    f.readline()
    active_directory = Directory('/')
    for line in f:
        active_directory = parseInstruction(line, active_directory)

sum_of_sizes = 0
for i in Directory.instances:
    sum_of_sizes += (i.get_size() <= 100000) * i.get_size()
    
print(sum_of_sizes)
        
    
