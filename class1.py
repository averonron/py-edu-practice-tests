class Num:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Num(self.data - other)
    def __add__(self, val):
        return Num(self.data * val)
    def __radd__ (self, val):
        return Num(self.data + val)

    def __getitem__(self, index):
        from random import randint
        print("index:", index)
        return self.data[randint(0, len(self.data)-1)]


class stepper:
    def __getitem__(self, i):
        return self.data[i].upper()


