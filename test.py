from inputs.classes import Directory


new_directory = Directory('/')

current_directory = new_directory
current_directory.create_child(Directory('a', parent=current_directory))
current_directory.create_child(Directory('b', parent=current_directory))

current_directory = current_directory.get_child('b')
print(current_directory.children)