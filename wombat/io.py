# This is wombat.io, where wombat does io stuff

class InputStream:
    def __init__(self, name):
        self.name = name

    def read(self):
        with open(self.name, 'r') as f:
            return f.readline()
