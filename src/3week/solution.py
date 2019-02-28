import sys


class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as f:
                return f.read()
        except IOError:
            return ""
        else:
            return ""


path = sys.argv[1]
reader = FileReader(path)
print(reader.read())
