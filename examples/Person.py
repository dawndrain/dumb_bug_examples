class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        assert False
        print("Hello my name is " + self.name)