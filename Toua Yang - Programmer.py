class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age):
        super(Employee, self).__init__(name, age)

    def pay(self):
        print("%s got paid" % self.name)


class Programmer(Employee):
    def __init__(self, name, age):
        super(Programmer, self).__init__(name, age)

    def old(self):
        print("%s is %s " % self.name, self.age)


John = Employee('John', 32)
Jay = Programmer('Jay', 35)
Employee.pay(John)
