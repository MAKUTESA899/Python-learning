class Person:
    def __init__(self,fname,iname):
        self.fname=fname
        self.iname=iname
    def printname(self):
        print(f"My name is {self.fname} {self.iname}")
class Student(Person):
    def __init__(self,iname,fname,age,course):
        self.age=age
        self.course=course
        super().__init__(fname,iname)
    def details(self):
        print(f"{self.fname} studing {self.course} age {self.age}")
student1=Student("alex","maina","python",54)
student1.details()
student1.printname()
        
2 3 1
525
713
956