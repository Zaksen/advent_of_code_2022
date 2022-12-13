class Directory:
    instances = []
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent if parent else None
        self.__class__.instances.append(self)
        
    def create_child(self, child):
        self.children.append(child)
    
    def get_child(self, name):
        if name == '..':
            return self.parent
        for c in self.children:
            if isinstance(c, Directory):
                if c.name == name:
                    return c

    def get_size(self):
        size = 0
        for c in self.children:
            if isinstance(c, File):
                size += int(c.size)
            else:
                size += int(c.get_size())
        return size
                
        
    def __repr__(self):
        return(f'Directory {self.name}')
            
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
        
    def __repr__(self):
        return(f'File {self.name} of size {self.size}')
        
