# creating a greeting function and execute it on the object
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def firstfunc(self):
        print("Hi, my name is : " + self.name)

x = person("Rudra", 20)
x.firstfunc()
