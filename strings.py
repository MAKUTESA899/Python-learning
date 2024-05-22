class student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def displayName (self):
        
        print(f"{self.name}, {self.course}")
student1 = student("alex", "python")
student1.displayName()