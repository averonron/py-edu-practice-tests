class wrap:
    def __init__(self, wrapped):
        self.wrapobj = wrapped
    def __getattr__(self, attr):
        print("Attr:", attr)
        return getattr(self.wrapobj, attr)
    def htmlPrgr(self):
        for elem in self.wrapobj:
            print("<p>{}</p>".format(elem))
    def letterize(self):
        abc123 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
        for elem in self.wrapobj:
            print(abc123[elem], end=" ")

obj = [1, 2, 3]
x = wrap(obj)
print(x.wrapobj)
x.append(4)
print(x.wrapobj)
print()

f = open(r"C:\Users\Aviator\Desktop\data.txt")
t = f.read().split('\n')
f.close()

x = wrap(t)
x.htmlPrgr()
