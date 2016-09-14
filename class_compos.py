class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def work(self):
        print(self.name, "does work")
    def giveRaise(self, percent):
        self.salary = self.salary*(1 + percent/100)
    def __repr__(self):
        return "<Employee: name = {0}, salary = {1}>".format(self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, "is cook")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "is service")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "does pizzas")


class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "ordered to", server)
    def pay(self, server):
        print(self.name, "paid to", server)

class Oven:
    def bake(self):
        print("Over bakes")

class PizzaShop:
    def __init__(self):
        self.server = Server("Pat")
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()
    scene.order("Homer")
    print("...")
    scene.order("Shaggy")








if __name__ == "__main__-":
    bob = PizzaRobot("Bob")
    print(bob)
    bob.work()
    bob.giveRaise(20)
    print(bob)
    print()

    for klass in (Employee, Chef, Server, PizzaRobot):
        obj = klass(klass.__name__)
        obj.work()







