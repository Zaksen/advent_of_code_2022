class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent if parent else None
        
    def create_child(self, child):
        self.children.append(child)
    
    def get_child(self, name):
        if name == '..':
            return self.parent
        for c in self.children:
            if isinstance(c, Directory):
                if c.name == name:
                    return c
                    
    def __repr__(self):
        return(f'Directory {self.name}')
            
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def __repr__(self):
        return(f'File {self.name} of size {self.size}')
        
