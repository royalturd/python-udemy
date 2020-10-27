# mofifiyng object properties
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def firstfunc(self):
    print("hi, my name is: " + self.name)

obj1 = person("Terry" , 45)

# modifiyng the values

obj1.name = "Rudra"
obj1.age = 20

print(obj1.name)
print(obj1.age)