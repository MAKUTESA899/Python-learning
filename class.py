class person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
    def __str__(self):
        return(f"{self.name}, {self.age}")

p1 = person ("jhon", 36)
print(p1)

class person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
    def __str__(self):
        return(f"{self.name}, {self.age}")

p1 = person ("jhon", 36)
print(p1.age)
print(p1.name)


class person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
    def personality(self):
        print("my name is" + self.name)
p1 = person ("alex" , 39)
p1.personality()
print(p1.age, p1.name)


class person:
    def __init__(self , name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return (f"{self.name} {self.age}")
    def __float__(num, a , b):
        num.a = a
        num.b = b
        print(a / b)
a = int(input("values ;"))
b = int(input("values ;"))

p1 = person ("john", 38)

print(f"my name is {p1.name}")
print(f"and i am {p1.age} years old")
print(f"the division of {a} and {b} {p1}")