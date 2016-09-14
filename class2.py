"""
class Iter:
    def __init__(self, value, stop):
        self.value = value
        self.stop = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        else:
            self.value += 1
            return self.value

class Range:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop - 1
    def __iter__(self):
        return Iter(self.value, self.stop)

"""

class Ito:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return Iter(self.value)

class Iter:
    def __init__(self, value):
        self.value = value
        self.index = 0
        self.stop = len(self.value)

    def __next__(self):
        if self.index == self.stop:
            raise StopIteration
        else:
            item = self.value[self.index].upper()
            self.index += 1
            return item

s = Ito("String")

for i in s:
    for j in s:
        print(i, j, sep = "", end = " ")
