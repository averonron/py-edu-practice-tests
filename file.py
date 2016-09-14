class Person:
    """
Person database realization
"""
    def __init__(self, name, job = "nonwork", pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def __str__(self):
        return "[{}: {}, {}]".format(self.name, self.job, self.pay)

    def lastName(self):
        return self.name.split()[-1]

    def raisePay(self, perc):
        self.pay = int(self.pay * (1 + perc))


class Manager(Person):
    job = 'manager'
    def __init__(self, name, pay):
        Person.__init__(self, name, self.job, pay)

    def raisePay(self, perc, bonus=.10):
        Person.raisePay(self, perc+bonus)

class Counter:
    count = 0
    def __init__(self):
        self.__class__.count += 1
        


# test #
if __name__ == "__main__":
    bob = Person("Bob Taylor")
    sue = Person("Sue Magica", "developer", 5450)
    print(sue)
    print(bob)

    jason = Manager("Jason Collins", 5000)
    jason.raisePay(.10, .40)
    print(jason)
    print(jason.job)

    print(Counter.count)
    c = Counter()
    print(Counter.count, c.count)
    d = Counter()
    print(Counter.count, c.count, d.count)
