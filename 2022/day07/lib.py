class FileSystem:
    def __init__(self, root):
        self.pwd = root
        self.root = root

    def cd(self, next_directory):
        if next_directory == self.root.name:
            self.pwd = self.root
        elif next_directory == "..":
            self.pwd = self.pwd.parent
        else:
            self.pwd = self.pwd.directories[next_directory]


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent  # Directory object
        self.files = []
        self.directories = {}
        self.is_directory = True

    def add_directory(self, name):
        self.directories[name] = Directory(name, self)

    def add_file(self, size):
        self.files.append(size)
