import tempfile
from os import path


class File:
    def __init__(self, path):
        self.path = str(path)

    def write(self, str):
        with open(self.path, "w") as f:
            f.write(str)

    def __add__(self, other):
        s = ""
        with open(self.path) as f1:
            s += f1.read()
        with open(other.path) as f2:
            s += f2.read()
        new_file = File(path.join(tempfile.gettempdir(), "new_file.txt"))
        new_file.write(s)
        return new_file

    def __iter__(self):
        self.lines = open(self.path).readlines()
        self.cur_line = 0
        return self

    def __next__(self):
        if self.cur_line >= len(self.lines):
            raise StopIteration
        result = self.lines[self.cur_line]
        self.cur_line += 1
        return result

    def __str__(self):
        return self.path
