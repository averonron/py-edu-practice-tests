class Counter:
    """The first Python class"""
    def __init__(self, initial = 0):
        self.value = initial

    def increment(self):
        self.value += 1

    def get(self):
        return self.value

c = Counter(5)
for i in range(5):
    c.increment()

print(c.get())
