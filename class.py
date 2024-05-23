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
    def __init__(self,age):
        self.age = age
    def __str__(self):
        return (f" {self.age}")
    def __float__(self):
        return float(self.age)
# a = int(input("values ;"))
# b = int(input("values ;"))


print(f"my name is {p1.name}")
print(f"and i am {p1.age} years old")
# print(f"the division of {a} and {b} {p1}")


class Employee:
   "Common base class for all employees"
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
person1 = person(38)
print(float(person1))


class person:
    def __init__(self,loan,inheritance):
        self.laon= loan
        self.inheritance = inheritance

class child:
    def __init__(self):
        return
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = person(" 200 dollars", 300000000)
c1 = child ("jhon", 30)
print(c1.name)
print(c1.age)
print( f"pay for the loan :{p1.inheritance}")
print(p1.laon)

