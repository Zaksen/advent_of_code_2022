class Directory:
    def __init__(self, name, isFile=False):
        self.name = name
        self.size = 0
        self.children = []
        self.isFile = isFile

    def create_directory(self, child):
        self.children.append(child)

    def __str__(self): return self.name

main_directory = Directory('/')
main_directory.create_directory(Directory('a'))

print(main_directory.children)

