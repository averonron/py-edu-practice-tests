class Super:
    def __init__(self):
        self.data = "Data"

    def hello(self):
        self.hello = "Hello"

class Sub(Super):
    def hola(self):
        self.hola = "Hola"

x = Sub()
x.hello()
