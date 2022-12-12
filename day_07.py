from inputs.classes import File, Directory

with open('inputs/day_7.txt', 'r') as f:
    f.readline()
    active_directory = Directory('/')
    for line in f:
        args = line.rstrip().split("$ ")
        if len(args) == 1:
            arg1, arg2 = args[0].split(" ")
            if 'dir' in arg1:
                active_directory.create_child(Directory(arg2, parent=active_directory))
            else:
                active_directory.create_child(File(arg2, int(arg1)))    
        else:
            if 'ls' not in args[1]:
                arg1, arg2 = args[1].split(" ")
                if 'cd' in arg1:
                    if arg2 == '..':
                        active_directory = active_directory.parent 
                    else:
                        active_directory = active_directory.get_child(arg2)

active_directory = active_directory.parent
active_directory = active_directory.parent
