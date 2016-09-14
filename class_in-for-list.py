class Handler:
    def __init__(self, value):
        self.data = value
    
    def __getitem__(self, index):
        print("__getitem__", end=" ")
        return self.data[index]

    def __iter__(self):
        return Iter(self.data)

    def __contains__(self, x):
        print("__contains__", end=" ")
        return x in self.data

class Iter:
    def __init__(self, value):
        self.data = value
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        print("__iter__", end=" ")
        item = self.data[self.index]
        self.index += 1
        return item
"""
string = "asdf"
x = Handler(string)

##-----------------##
##  'in' semantic  ##

the_sym = "d"

# 'in' default
print("'in' default")
print(the_sym in x)

# 'in' using '__contains__' (as default)
print("\n'in' using '__contains__' method")
print(x.__contains__(the_sym))

# 'in' using '__iter__'
print("\n'in' using '__iter__' method")
i = iter(x)
while True:
    try:
        sym = next(i)
        if sym == the_sym:
            print(True)
            break
    except StopIteration:
        print(False)
        break
        
# 'in' using '__getitem__'
print("\n'in' using '__getitem__' method")
i = 0
while True:
    try:
        if x[i] == the_sym:
            print(True)
            break
        i += 1
    except IndexError:
        print(False)
        break

##  'in' semantic  ##
##-----------------##

print()

##------------------##
##  'for' semantic  ##

# 'for' default
print("'for' default")
for i in x:
    print(i)

# 'for' using '__iter__'
print("\n'for' using '__iter__' method")
i = iter(x)
while True:
    try:
        print(next(i))
    except StopIteration:
        break

# 'for' using '__getitem__'
print("\n'for' using '__getitem__' method")
i = 0
while True:
    try:
        print(x[i])
        i += 1
    except IndexError:
        break

##  'for' semantic  ##
##------------------##
"""

s = "string"

def foo(x):
    print(x, end="|")

for ch in s:
    foo(ch)

print()

i = iter(s)
while True:
    try:
        ch = next(i)
        foo(ch)
    except StopIteration:
        break





































